# OPPO A37 vendor

All runtime files are under proprietary/, with paths relative to /system.
A37-vendor.mk maps that subtree into the product image, following the Hermes
vendor layout. Android.mk defines only blobs needed as linkable build modules.
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
