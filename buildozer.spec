[app]
title = MANTIS
package.name = mantis
package.domain = com.miningtech
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.7.1
requirements = python3,kivy==2.1.0,pygments
orientation = portrait
fullscreen = 0

# Android specific
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.arch = arm64-v8a
android.accept_sdk_license = True

# Build options
android.gradle_dependencies = 

[buildozer]
log_level = 2
warn_on_root = 1