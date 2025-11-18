"""
Telematics Data Generator (File-Based)
Reads configuration from config.py (not committed to Git)
"""

import os
import sys
import json
import time
import random
import pandas as pd
from datetime import datetime, timedelta

# ============================================
# IMPORT CONFIGURATION
# ============================================

# Add parent directory to path to import config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from config import (
        AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
        AWS_DEFAULT_REGION,
        KINESIS_STREAM_NAME
    )
    print("✅ Configuration loaded from config.py")
except ImportError:
    print("=" * 70)
    print("❌ ERROR: config.py not found!")
    print("=" * 70)
    print("\nThis project uses a config file for credentials (not committed to Git).")
    print("\nSetup steps:")
    print("1. Copy the template:")
    print("   cp config.template.py config.py")
    print("\n2. Edit config.py and add your AWS credentials")
    print("\n3. Run this script again")
    print("=" * 70)
    sys.exit(1)

# Validate credentials are not placeholder values
if "YOUR_AWS_ACCESS_KEY" in AWS_ACCESS_KEY_ID:
    print("=" * 70)
    print("❌ ERROR: config.py contains placeholder values!")
    print("=" * 70)
    print("\nPlease edit config.py and replace:")
    print('  AWS_ACCESS_KEY_ID = "YOUR_AWS_ACCESS_KEY_HERE"')
    print("with your actual AWS credentials")
    print("=" * 70)
    sys.exit(1)

# ============================================
# SCRIPT CONFIGURATION
# ============================================

OUTPUT_DIR = "telemetry_output"
NUM_VEHICLES = 100
EVENTS_PER_BATCH = 500
NUM_BATCHES = 10
BATCH_INTERVAL_SEC = 2

# ============================================
# CREATE OUTPUT DIRECTORY
# ============================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================
# DATA GENERATION FUNCTION
# ============================================

def generate_telemetry_batch(batch_num, num_events):
    """Generate batch of telemetry events"""
    
    events = []
    base_timestamp = datetime.now() + timedelta(minutes=batch_num * 10)
    
    for i in range(num_events):
        vehicle_id = f"VEH{random.randint(1000, 1000 + NUM_VEHICLES):04d}"
        
        # Realistic speed distribution
        speed = round(random.uniform(0, 60) if random.random() < 0.7 else random.uniform(60, 120), 2)
        
        # Realistic acceleration
        accel = round(random.uniform(-2, 2) if random.random() < 0.9 else random.uniform(-5, 5), 2)
        
        event = {
            'vehicle_id': vehicle_id,
            'speed_mph': speed,
            'latitude': round(random.uniform(25.0, 50.0), 6),
            'longitude': round(random.uniform(-125.0, -65.0), 6),
            'acceleration_mps2': accel,
            'timestamp': (base_timestamp + timedelta(seconds=i)).isoformat()
        }
        events.append(event)
    
    return pd.DataFrame(events)

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    print("="*70)
    print("🚗 TELEMETRY DATA GENERATOR")
    print("="*70)
    print(f"AWS Region: {AWS_DEFAULT_REGION}")
    print(f"Kinesis Stream: {KINESIS_STREAM_NAME}")
    print(f"Batches: {NUM_BATCHES}")
    print(f"Events per batch: {EVENTS_PER_BATCH}")
    print(f"Total events: {NUM_BATCHES * EVENTS_PER_BATCH:,}")
    print("="*70)
    
    for batch_num in range(NUM_BATCHES):
        # Generate batch
        df = generate_telemetry_batch(batch_num, EVENTS_PER_BATCH)
        
        # Write to CSV
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{OUTPUT_DIR}/telemetry_batch_{batch_num:03d}_{timestamp}.csv"
        df.to_csv(filename, index=False)
        
        print(f"✅ Batch {batch_num + 1}/{NUM_BATCHES}: {filename} ({len(df)} events)")
        
        # Wait before next batch
        if batch_num < NUM_BATCHES - 1:
            time.sleep(BATCH_INTERVAL_SEC)
    
    print("\n" + "="*70)
    print("🎉 DATA GENERATION COMPLETE!")
    print("="*70)
