LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := libmtkjpeg
LOCAL_SRC_FILES := proprietary/vendor/lib/libmtkjpeg.so
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_MULTILIB := 32
LOCAL_PROPRIETARY_MODULE := true
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := mtk-ril
LOCAL_SRC_FILES_64 := proprietary/vendor/lib64/mtk-ril.so
LOCAL_SRC_FILES_32 := proprietary/vendor/lib/mtk-ril.so
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_PROPRIETARY_MODULE := true
LOCAL_MULTILIB := both
LOCAL_CHECK_ELF_FILES := false
include $(BUILD_PREBUILT)
include $(CLEAR_VARS)
LOCAL_MODULE := librilmtk
LOCAL_SRC_FILES_64 := proprietary/vendor/lib64/librilmtk.so
LOCAL_SRC_FILES_32 := proprietary/vendor/lib/librilmtk.so
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_PROPRIETARY_MODULE := true
LOCAL_MULTILIB := both
LOCAL_CHECK_ELF_FILES := false
include $(BUILD_PREBUILT)
