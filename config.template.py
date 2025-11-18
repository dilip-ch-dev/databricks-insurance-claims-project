"""
Configuration Template for Databricks Insurance Claims Project

INSTRUCTIONS:
1. Copy this file to config.py:
   cp config.template.py config.py

2. Fill in your actual credentials in config.py

3. config.py is in .gitignore (never committed to Git)

4. All scripts import from config.py for credentials
"""

# ============================================
# AWS CREDENTIALS
# ============================================

AWS_ACCESS_KEY_ID = "YOUR_AWS_ACCESS_KEY_HERE"
AWS_SECRET_ACCESS_KEY = "YOUR_AWS_SECRET_KEY_HERE"
AWS_DEFAULT_REGION = "us-east-2"

# ============================================
# AWS RESOURCES
# ============================================

S3_BUCKET_NAME = "databricks-claims-dilip-2025"
KINESIS_STREAM_NAME = "insurance-telemetry-stream"

# ============================================
# DATABRICKS CONFIGURATION
# ============================================

DATABRICKS_HOST = "https://dbc-02b6fba9-f3ce.cloud.databricks.com"
DATABRICKS_CATALOG = "smart_claims_dev"

# ============================================
# PROJECT PATHS
# ============================================

LANDING_VOLUME_PATH = "/Volumes/smart_claims_dev/landing/raw_files"
CHECKPOINT_PATH = "/Volumes/smart_claims_dev/landing/raw_files/_checkpoints"
