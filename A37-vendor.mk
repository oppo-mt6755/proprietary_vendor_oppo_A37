# Vendor blobs follow the Hermes layout: paths under proprietary/ map directly
# below /system in the product image.
PRODUCT_COPY_FILES += $(call find-copy-subdir-files,*,vendor/oppo/A37/proprietary,system)
