# Greeble Tool - Build Notes

## Files Created

### Fixed Android App
- `greeble_android.py` - Complete Kivy Android app with:
  - Full gibberish generation matching terminal version
  - Animated progress bars
  - Password prompt (accepts any input)
  - Success screen with "Work safe" message
  - Improved UI styling

### GitHub Actions Workflows

Two workflow options provided:

#### 1. Native Build (`.github/workflows/build.yml`)
- Installs Buildozer directly on Ubuntu runner
- Uses caching for faster subsequent builds
- Full control over dependencies

#### 2. Docker Build (`.github/workflows/build-docker.yml`)
- Uses `kivy/buildozer:latest` Docker image
- More reliable for complex dependencies
- Pre-configured Android SDK/NDK

### Configuration Files

#### `buildozer.spec`
Key settings:
- `title = Greeble Tool`
- `package.name = greebletool`
- `package.domain = com.greeble`
- `version = 2.7.1`
- `requirements = python3,kivy==2.2.1,android,pyjnius`
- `android.api = 33`
- `android.minapi = 21`
- `android.archs = arm64-v8a, armeabi-v7a`

## Required Assets

Create these in `assets/` directory:
- `icon.png` - App icon (512x512 recommended)
- `presplash.png` - Splash screen (recommended: 1080x1920)

## Building Locally

```bash
# Install buildozer
pip install buildozer cython

# Build debug APK
buildozer android debug

# Build release APK
buildozer android release

# Deploy to connected device
buildozer android debug deploy run
```

## Troubleshooting

### Common Buildozer Issues

1. **SDK/NDK download failures**
   - Check internet connection
   - Try clearing `~/.buildozer/android/platform/`

2. **Out of memory during build**
   - Increase swap: `sudo fallocate -l 4G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile`

3. **Gradle/Java issues**
   - Ensure Java 17 is installed
   - Set `JAVA_HOME` appropriately

4. **Cache issues**
   - Delete `.buildozer/` directory and rebuild

### GitHub Actions Tips

- The Docker workflow is often more reliable
- Caching significantly speeds up subsequent builds
- First build will take 15-30 minutes (downloads SDK/NDK)
- Subsequent builds: 3-5 minutes with cache

## Recommended Workflow

1. Use the Docker workflow (`build-docker.yml`) as primary
2. Keep the native workflow as fallback
3. Add `icon.png` and `presplash.png` to `assets/`
4. Push to main branch triggers automatic build
5. Create git tags to trigger release uploads

## Testing the APK

```bash
# Install on device
adb install -r bin/greebletool-2.7.1-arm64-v8a_armeabi-v7a-debug.apk

# Or transfer to device and install manually
```
