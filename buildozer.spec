[app]
title = MANTIS
package.name = mantis
package.domain = com.miningtech

source.dir = .
source.include_exts = py

version = 2.7.1
requirements = python3,kivy

# Android specific
android.permissions = 
android.api = 33
android.minapi = 21
android.arch = arm64-v8a
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
android.skip_update = False

# Gradle
android.gradle_dependencies = 

# Python for android (p4a) specific
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1