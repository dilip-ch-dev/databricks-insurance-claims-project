# 🚗 Car Insurance Claims Automation with Databricks

**End-to-end Medallion Architecture with ML fraud detection and automated workflows**

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?logo=databricks&logoColor=white)](https://databricks.com)
[![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://python.org)
[![SQL](https://img.shields.io/badge/SQL-4479A1?logo=postgresql&logoColor=white)](https://www.databricks.com/glossary/what-is-sql)

---

## 📋 Project Overview

**Production-grade insurance claims data pipeline** built on Databricks implementing the complete Medallion Architecture (Bronze-Silver-Gold) with automated orchestration, ML fraud detection, and business intelligence analytics.

### 🎯 Business Problem Solved

- ✅ **Unified data platform** - Consolidated customer, claims, policy, and telematics data
- ✅ **Automated claims validation** - Real-time fraud detection and eligibility checks
- ✅ **Data quality framework** - 84.5% clean records with automated rejection of invalid data
- ✅ **ML fraud scoring** - AUC-ROC 1.0 model for fraud detection
- ✅ **Pipeline automation** - End-to-end orchestration with Databricks Workflows

---

## 🏗️ Architecture

### **Medallion Architecture (Bronze → Silver → Gold)**

Raw Data Sources
├─ CSV Ingestion (Auto Loader)
├─ Customer Data
├─ Claims Data
├─ Policy Data
└─ Telematics Events
↓
BRONZE LAYER
37,289 raw records
↓
SILVER LAYER
31,504 validated records (84.5% quality)
- Date format standardization
- Null handling & deduplication
- Business rule validation
- Audit timestamp tracking
↓
GOLD LAYER
31,329 analytics-ready records
├─ Claims aggregations by date/severity
├─ Collision type analysis
├─ Customer behavior metrics
├─ Driver risk scoring
├─ ML features for fraud detection
└─ Fraud detection scores


### **Data Quality Results**

| Layer | Claims | Customers | Policies | Telematics | Total | Pass Rate |
|-------|--------|-----------|----------|-----------|-------|-----------|
| **Bronze** | 12,991 | 7,061 | 12,237 | 5,000 | 37,289 | 100% |
| **Silver** | 10,733 | 3,636 | 12,135 | 5,000 | 31,504 | **84.5%** |
| **Quality Issues Caught** | 17.4% | 48.5% | 0.83% | 0% | - | - |

**Key Validations:**
- Mixed date format handling (MM-DD-YYYY, DD-MM-YYYY, YYYY-MM-DD)
- Age validation (18-120 years old, insurance requirement)
- Temporal logic (claim date after policy issue date)
- Deduplication via window functions

---

## 🤖 Machine Learning

### **Fraud Detection Model**

Training Data: 10,733 claims (8,666 train / 2,067 test)

Features (12):
├─ Customer: age, months_as_customer
├─ Claim: claim_amount, total_loss_flag, major_damage_flag
├─ Indicators: suspicious_flag, fraud_indicator, no_witnesses_flag, new_customer_flag
├─ Accident: number_of_vehicles_involved, number_of_witnesses, multi_vehicle_flag

Algorithm: Logistic Regression
Performance:
├─ AUC-ROC: 1.0000 ✅
├─ True Positives: High detection rate
└─ Predictions: Fraud probability scoring


**Model Output:** `smart_claims_dev.gold.fraud_detection_scores`
- claim_id
- actual_fraud_label
- fraud_prediction (0 = safe, 1 = fraud)
- fraud_probability_scores (vector)

---

## 🔧 Orchestration

### **Databricks Workflow: smart_claims_full_pipeline**

Automated DAG (Directed Acyclic Graph):

bronze_claims (05_silver_claims)
├─ silver_customers (06_silver_customers)
│  └─ gold_layer (09_gold_claims)
└─ silver_policies (07_silver_policies)
   └─ gold_layer (09_gold_claims)

Execution:

~Max concurrent runs: 1 

~Timeout: 3600 seconds

~Cluster: Auto-scaling i3.xlarge

~Trigger: Manual or scheduled


**End-to-end pipeline runs automatically with dependency management.**

---

## 📊 Gold Layer Tables

| Table | Rows | Purpose |
|-------|------|---------|
| **claims_by_date_severity** | 284 | Claims trends by month & severity level |
| **claims_by_collision_type** | 4 | Collision analysis with payout metrics |
| **customer_metrics** | 10,211 | Customer behavior (claim frequency, payout) |
| **driver_risk_scores** | 101 | Telematics-based driver risk scoring |
| **ml_features** | 10,733 | ML-ready features for fraud detection |
| **fraud_detection_scores** | 10,733 | Fraud predictions & probabilities |

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Data Platform** | Databricks (Free Edition) | Lakehouse, SQL, Workflows |
| **Storage** | Delta Lake + AWS S3 | ACID transactions, data versioning |
| **Ingestion** | Auto Loader | Incremental file processing |
| **Processing** | PySpark, SparkSQL | Distributed data transformation |
| **ML** | PySpark ML, Logistic Regression | Fraud detection |
| **Orchestration** | Databricks Workflows | Pipeline automation |
| **Infrastructure** | Terraform | IaC for Databricks + AWS |
| **Version Control** | GitHub + Databricks Repos | Git integration |

---

## 📁 Repository Structure

databricks-insurance-claims-project/
├── notebooks/
│ ├── 01_csv_ingestion.py (Bronze CSV ingestion)
│ ├── 02_elt_pipeline.py (Schema standardization)
│ ├── 03_claims_integration.py (Data reconciliation)
│ ├── 04_bronze_summary.py (Quality validation)
│ ├── 05_silver_claims.py (Claims transformation)
│ ├── 06_silver_customers.py (Customers transformation)
│ ├── 07_silver_policies.py (Policies transformation)
│ ├── 08_silver_telematics.py (Telematics transformation)
│ ├── 09_gold_claims.py (Gold aggregations)
│ ├── 10_workflow_orchestration.py (Workflow setup)
│ ├── 11_ml_fraud_detection.py (ML model training)
│ └── 12_dashboard_queries.sql (Analytics dashboard)
├── terraform/
│ ├── main.tf (Databricks + AWS provisioning)
│ ├── variables.tf (Configuration variables)
│ └── outputs.tf (Resource outputs)
├── scripts/
│ └── data_generator.py (Test data generation)
└── README.md


---

## 🚀 Key Learnings

### **Data Engineering Challenges Solved**

1. **Mixed Date Formats**
   - Problem: Dates in MM-DD-YYYY, DD-MM-YYYY, YYYY-MM-DD formats
   - Solution: `try_to_date()` + SQL CASE WHEN for safe casting
   - Impact: Enabled 82.6% claims quality pass rate

2. **String "null" vs SQL NULL**
   - Problem: Literal "null" strings vs actual NULL values
   - Solution: Explicit CASE WHEN checks for both types
   - Impact: Caught 48.5% invalid customer records

3. **Deduplication at Scale**
   - Problem: Duplicate records across sources
   - Solution: Window functions `row_number() over partitions`
   - Impact: Reduced data redundancy by 17.4%

4. **Production-Grade Quality Tracking**
   - Problem: Understanding data rejection reasons
   - Solution: Audit columns with `current_timestamp()` + rejection tracking
   - Impact: Full data lineage and compliance audit trail

### **Free Edition Optimization**

- ✅ Pivoted from AWS Kinesis to Databricks Auto Loader (eliminated $40/month cost)
- ✅ Used serverless compute (auto-scaling clusters)
- ✅ CPU-friendly ML models (no GPU required)
- ✅ Efficient Workflow orchestration (5-task limit respected)

---

## 📈 Performance Metrics

Pipeline Execution:
├─ Bronze ingestion: ~30 seconds (37,289 rows)
├─ Silver transformation: ~1 minute (per table)
├─ Gold aggregations: ~45 seconds (5 tables)
├─ ML model training: ~2 minutes (10,733 samples)
└─ Total end-to-end: ~5-6 minutes

Data Quality:
├─ Bronze → Silver: 84.5% pass rate
├─ Invalid records identified: 5,785 (17.4%)
├─ Duplicate removal: Window function dedup
└─ Audit coverage: 100% (timestamp on all records)

ML Performance:
├─ Fraud detection AUC-ROC: 1.0000
├─ Test set accuracy: 100%
├─ Features engineered: 12
└─ Training samples: 10,733


---

## 🎓 Interview Talking Points

**Q: Tell me about your data pipeline**
> "I built a complete Medallion Architecture on Databricks processing 37K insurance records. The Bronze layer uses Auto Loader for incremental ingestion. Silver applies production-grade quality validation - I reject 17.4% of records that violate business rules like age constraints and temporal logic. Gold creates analytics tables and ML features. The entire pipeline is orchestrated with Databricks Workflows for automation."

**Q: What was your biggest technical challenge?**
> "Mixed date formats in customer data - some were MM-DD-YYYY, others DD-MM-YYYY. Standard casting failed silently. I implemented a SQL CASE WHEN using try_to_date() that handles all formats simultaneously. This taught me the importance of defensive data engineering - never assume consistent input formats."

**Q: Why Databricks Free Edition?**
> "I optimized for cost and learning. I initially planned AWS Kinesis streaming but pivoted to Auto Loader - same functionality, zero cost. I trained ML models with CPU-friendly algorithms. This shows I think about operational expenses even in development environments."

**Q: How did you approach ML for fraud detection?**
> "I engineered 12 features from claims, customer, and telematics data: suspicious flags, new customer indicators, claim severity markers. I trained a Logistic Regression model achieving AUC-ROC of 1.0 on the test set. The model generates fraud probability scores for every claim, creating a production-ready scoring pipeline."

---

## 📚 Resources & Documentation

- **Databricks Docs:** https://docs.databricks.com
- **Delta Lake:** https://delta.io
- **PySpark API:** https://spark.apache.org/docs/latest/api/python/
- **Terraform:** https://registry.terraform.io/providers/databricks/databricks/latest/docs

---

## 👤 Author

**Dilip Chikatla**  
Data Engineer | AWS • Databricks • Snowflake | Building production lakehouse pipelines

- **GitHub:** https://github.com/dilip-ch-dev
- **LinkedIn:** https://www.linkedin.com/in/dilipchikatla/
- **Email:** dilip77950@gmail.com

---

## 📄 License

Open source for portfolio and learning purposes.

---

**⭐ If this project helped you learn Databricks, consider starring the repo!**
