#!/usr/bin/env python3
"""
Greeble Tool - The "I'm Doing Important Technical Things" Simulator
For Linux terminals. Looks complex, does nothing, scares off copycats.
"""

import os
import sys
import time
import random
import curses
from datetime import datetime

# Technical gibberish dictionaries
VERBS = ["Calibrating", "Syncing", "Handshaking", "Negotiating", "Buffering",
         "Optimizing", "Aligning", "Polling", "Querying", "Validating",
         "Propagating", "Transcoding", "Multiplexing", "Demodulating"]

NOUNS = ["phase array", "Fresnel zone", "carrier signal", "packet stream",
         "quantum buffer", "harmonic resonance", "baseband", "sideband",
         "cryptographic nonce", "handshake token", "CRC checksum",
         "latency profile", "attenuation curve", "spectral density"]

ADJECTIVES = ["adaptive", "dynamic", "orthogonal", "differential", "coherent",
              "asynchronous", "bidirectional", "multi-path", "low-latency",
              "high-gain", "wideband", "narrowband", "spread-spectrum"]

SYSTEMS = ["autonomous subsystem", "CAN bus bridge", "sensor fusion module",
           "telemetry aggregator", "diagnostic relay", "safety interlock",
           "beacon transponder", "mesh node", "gateway controller"]

MENU_OPTIONS = [
    "1. Initialize Autonomous Link",
    "2. Calibrate Sensor Array", 
    "3. Sync Fleet Telemetry",
    "4. Validate Safety Interlocks",
    "5. Run Diagnostic Sweep",
    "6. Optimize Signal Path",
    "7. Reset Mesh Topology",
    "8. Emergency Override (DANGER)"
]

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def fake_progress_bar(label, duration=2.0, width=40):
    """Display a convincing progress bar"""
    start = time.time()
    while time.time() - start < duration:
        elapsed = time.time() - start
        pct = min(100, int((elapsed / duration) * 100))
        filled = int((pct / 100) * width)
        bar = "█" * filled + "░" * (width - filled)
        print(f"\r  {label}: [{bar}] {pct}%", end='', flush=True)
        time.sleep(random.uniform(0.05, 0.15))
    print(f"\r  {label}: [{'█' * width}] 100% ✓")

def random_gibberish_line():
    """Generate a line of plausible technical nonsense"""
    templates = [
        f"{random.choice(VERBS)} {random.choice(ADJECTIVES)} {random.choice(NOUNS)}...",
        f"{random.choice(VERBS)} {random.choice(SYSTEMS)} handshake...",
        f"{random.choice(ADJECTIVES).capitalize()} {random.choice(NOUNS)} detected: {random.randint(1000, 9999)}ms",
        f"Querying {random.choice(SYSTEMS)}... [{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}]",
        f"CRC validation: 0x{random.randint(0x1000, 0xFFFF):04X}",
        f"Latency check: {random.uniform(2.5, 45.3):.2f}ms (acceptable)",
        f"Signal strength: -{random.randint(45, 85)} dBm",
        f"Channel {random.randint(1, 165)}: {random.choice(['clear', 'congested', 'optimal'])}",
    ]
    return random.choice(templates)

def run_sequence(menu_choice):
    """Run the fake technical sequence"""
    clear()
    print("═" * 60)
    print("  G R E E B L E   T O O L   v2.7.1-RC3")
    print("  Autonomous Systems Diagnostic Interface")
    print("═" * 60)
    print(f"  Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Operator: {os.getenv('USER', 'technician')}")
    print(f"  Target: {random.choice(SYSTEMS).upper()}")
    print("═" * 60)
    print()
    
    # Initial delay for drama
    time.sleep(0.5)
    
    # Generate 4-7 lines of gibberish
    steps = random.randint(4, 7)
    for i in range(steps):
        print(f"  [{i+1}/{steps}] {random_gibberish_line()}")
        time.sleep(random.uniform(0.3, 0.8))
    
    print()
    
    # Progress bars
    fake_progress_bar("Establishing secure channel", 1.5)
    fake_progress_bar("Synchronizing clock domains", 1.2)
    fake_progress_bar("Verifying integrity", 1.8)
    
    print()
    print("  Status: LINK ESTABLISHED")
    print(f"  Encryption: AES-{random.choice([128, 256, 512])}-GCM")
    print(f"  Session key: {''.join(random.choices('0123456789ABCDEF', k=32))}")
    print()
    
    # Password prompt
    print("  ╔" + "═" * 48 + "╗")
    print("  ║  AUTHORIZATION REQUIRED                        ║")
    print("  ╠" + "═" * 48 + "╣")
    print("  ║  Enter override code to proceed:               ║")
    print("  ╚" + "═" * 48 + "╝")
    print()
    
    # Any input works
    input("  > ")
    
    # Success message
    print()
    print("  ✓ AUTHORIZATION ACCEPTED")
    print()
    print("  ╔" + "═" * 48 + "╗")
    print("  ║                                                ║")
    print("  ║           OPERATION SUCCESSFUL                 ║")
    print("  ║                                                ║")
    print("  ║   Work safe. Watch your step.                  ║")
    print("  ║   Your family wants you home for dinner.       ║")
    print("  ║                                                ║")
    print("  ╚" + "═" + "═" * 46 + "═" + "╝")
    print()
    input("  Press ENTER to exit...")

def main():
    while True:
        clear()
        print("═" * 60)
        print("  G R E E B L E   T O O L   v2.7.1-RC3")
        print("  Autonomous Systems Diagnostic Interface")
        print("═" * 60)
        print()
        for option in MENU_OPTIONS:
            print(f"  {option}")
        print()
        print("  Q. Quit")
        print()
        print("─" * 60)
        
        choice = input("  Select operation: ").strip().lower()
        
        if choice == 'q':
            clear()
            print("  Greeble Tool terminated.")
            print("  Remember: Safety third.")
            sys.exit(0)
        elif choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
            run_sequence(choice)
        else:
            print("  Invalid selection.")
            time.sleep(0.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("  Aborted. Systems remain in safe state.")
        sys.exit(0)
