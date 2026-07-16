#!/usr/bin/env python3
"""
Test that MANTIS can import and basic functionality works
"""

import sys
import traceback

def test_terminal_version():
    """Test the terminal version imports"""
    try:
        # Test basic imports
        import os
        import time
        import random
        print("✓ Basic imports work")
        
        # Test that the main script can be imported
        sys.path.insert(0, '.')
        import greeble
        print("✓ Terminal greeble imports successfully")
        
        return True
    except Exception as e:
        print(f"✗ Terminal version failed: {e}")
        traceback.print_exc()
        return False

def test_android_version():
    """Test the Android version can at least be parsed"""
    try:
        # Read the Android version and check for syntax errors
        with open('greeble_android.py', 'r') as f:
            code = f.read()
        
        # Try to compile it (won't run without Kivy, but syntax should be OK)
        compile(code, 'greeble_android.py', 'exec')
        print("✓ Android version compiles (syntax OK)")
        
        return True
    except Exception as e:
        print(f"✗ Android version failed: {e}")
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("MANTIS Test Suite")
    print("=" * 40)
    
    success = True
    success &= test_terminal_version()
    success &= test_android_version()
    
    if success:
        print("\n✓ All tests passed - MANTIS is ready")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed")
        sys.exit(1)