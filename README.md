# OPPO A37 vendor

All runtime files are under proprietary/, with paths relative to /system.
A37-vendor.mk is generated from the device proprietary-files.txt, following the
Hermes vendor layout. Android.mk defines only blobs needed as linkable build modules.
The Git history retains the SonyCustoms donor and the subsequent A37 fixes;
provenance JSON files record the mixed sources without changing those origins.

Device HALs, daemons, firmware and input mappings live below proprietary/vendor/.
aptX and aptX HD encoders live below proprietary/lib and proprietary/lib64,
matching the Hermes system-library layout and Oreo Bluetooth soname lookup.
ACCDET.kl and mtk-kpd.kl cover headset/physical keypad input. A minimal
mtk-tpd-kpd.kl maps the controller Menu scan code to Recents; other
input configuration and ICU data use platform defaults. Hermes fuelgauged
loads vendor/lib/libfgauge.so directly while retaining the A37 algorithm library.
There are no fingerprint blobs: the A37 has no fingerprint sensor.

The source device tree provides hwcomposer.mt6755 and libgralloc_extra.
USB audio and remote submix use the platform default modules; ClearKey/mock DRM
plugins are also built by the platform. Their redundant donor blobs are removed.
The legacy camera, GPS, sensor, primary audio, gralloc and memtrack libraries
remain required by the HIDL adapters and are not duplicate adapter binaries.
Donor init scripts are excluded; the device tree supplies the validated service
configuration. Blobs registered as native build modules are excluded from the
generated copy rules.

Shim dependencies are embedded in the 46 consuming ELFs with patchelf, rather
than TARGET_LD_SHIM_LIBS. shim-dependencies.json records the original/patched
hashes and complete dependency order. Run `python3 fixup-shims.py` to verify;
use `--apply` to reproduce the changes from original blobs with patchelf 0.18.0.
Historical provenance hashes describe their earlier stages; this manifest records
the final DT_NEEDED-only transformation. Code and read-only data remain unchanged.

Run device/oppo/A37/setup-makefiles.sh to regenerate Android.mk and A37-vendor.mk.
Extraction uses the matching device extract-files.sh and its pinned SHA-1 list;
factory files have no pin, while donor/local files are verified before replacement.
