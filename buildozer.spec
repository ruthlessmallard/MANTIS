[app]

# Title of your application
title = Greeble Tool

# Package name
package.name = greebletool

# Package domain (needed for android/ios packaging)
package.domain = com.greeble

# Source code where the main.py lives
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas

# List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# Application version
version = 2.7.1

# Requirements - Kivy and dependencies
requirements = python3,kivy==2.2.1,android,pyjnius

# Presplash of the application
presplash.filename = %(source.dir)s/assets/presplash.png

# Icon of the application
icon.filename = %(source.dir)s/assets/icon.png

# Supported orientation
orientation = portrait

# OSX/Python3 support
osx.python_version = 3
osx.kivy_version = 2.2.1

# Android specific
android.permissions = INTERNET

# Android API to use
android.api = 33

# Minimum API required
android.minapi = 21

# Android SDK version to use
android.sdk = 33

# Android NDK version to use
android.ndk = 25b

# Android NDK API (should match android.minapi)
android.ndk_api = 21

# Android private storage
android.private_storage = True

# Android app entry point
android.entrypoint = org.kivy.android.PythonActivity

# Android app theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# Android logcat filters
android.logcat_filters = *:S python:D

# Android copy libs
android.copy_libs = 1

# Build as an Android App Bundle (aab)
android.archs = arm64-v8a, armeabi-v7a

# Android release settings
android.release_artifact = apk

# iOS specific (not used for Android builds)
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2

# Minimum iOS version
ios.min_os_version = 13.0

[buildozer]

# Buildozer log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# Display warning if buildozer is run as root
warn_on_root = 1

# Build directory
build_dir = ./.buildozer

# Binaries output directory
bin_dir = ./bin
