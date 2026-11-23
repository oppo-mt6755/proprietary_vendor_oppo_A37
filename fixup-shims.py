#!/usr/bin/env python3
"""Apply or verify recorded ABI fixes and shim dependencies on vendor ELFs."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def needed(path):
    return subprocess.check_output(
        ["patchelf", "--print-needed", str(path)], text=True).splitlines()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true",
                        help="patch original blobs; already-patched files are verified")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "shim-dependencies.json").read_text())
    for item in manifest["files"]:
        path = ROOT / "proprietary" / item["path"]
        current = digest(path)
        if current == item["before_sha256"] and args.apply:
            if needed(path) != item["needed_before"]:
                raise SystemExit(f"Unexpected original dependencies: {path}")
            with tempfile.TemporaryDirectory(dir=path.parent) as work:
                staged = Path(work) / path.name
                shutil.copy2(path, staged)
                data = bytearray(staged.read_bytes())
                for patch in item.get("byte_patches", []):
                    offset = patch["offset"]
                    before = bytes.fromhex(patch["before"])
                    after = bytes.fromhex(patch["after"])
                    if len(before) != len(after) or data[offset:offset + len(before)] != before:
                        raise SystemExit(f"Unexpected instruction at {offset:#x}: {path}")
                    data[offset:offset + len(before)] = after
                staged.write_bytes(data)
                for shim in reversed(item["add_needed"]):
                    if shim not in item["needed_before"]:
                        subprocess.run(["patchelf", "--page-size", str(manifest["page_size"]),
                                        "--add-needed", shim, str(staged)], check=True)
                for library in item.get("remove_needed", []):
                    subprocess.run(["patchelf", "--remove-needed", library, str(staged)], check=True)
                for before, after in item.get("replace_needed", {}).items():
                    subprocess.run(["patchelf", "--page-size", str(manifest["page_size"]),
                                    "--replace-needed", before, after, str(staged)], check=True)
                if digest(staged) != item["after_sha256"]:
                    raise SystemExit(f"Patched hash differs; use {manifest['tool']}: {path}")
                staged.replace(path)
        if digest(path) != item["after_sha256"] or needed(path) != item["needed_after"]:
            raise SystemExit(f"Unexpected blob or dependencies: {path}")
    print(f"Verified {len(manifest['files'])} vendor ELFs and their shim dependencies")


if __name__ == "__main__":
    main()
