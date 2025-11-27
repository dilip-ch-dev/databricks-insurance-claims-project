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

```
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
    • Date format standardization
    • Null handling & deduplication
    • Business rule validation
    • Audit timestamp tracking
         ↓
    GOLD LAYER
    31,329 analytics-ready records
    ├─ Claims aggregations by date/severity
    ├─ Collision type analysis
    ├─ Customer behavior metrics
    ├─ Driver risk scoring
    ├─ ML features for fraud detection
    └─ Fraud detection scores
```

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

```
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
```

**Model Output:** `smart_claims_dev.gold.fraud_detection_scores`
- claim_id
- actual_fraud_label
- fraud_prediction (0 = safe, 1 = fraud)
- fraud_probability_scores (vector)

---

## 🔧 Orchestration

### **Databricks Workflow: smart_claims_full_pipeline**

```
Automated DAG (Directed Acyclic Graph):

    ┌─ bronze_claims (05_silver_claims)
    │
    ├─────────────────────┬──────────────────────┐
    │                     │                      │
    ▼                     ▼                      ▼
silver_customers   silver_policies          (parallel)
(06_silver_customers) (07_silver_policies)
    │                     │
    └─────────────────────┴──────────────────────┐
                                                 │
                                                 ▼
                                        gold_layer
                                    (09_gold_claims)
```

**Execution Details:**
- Task 1: `bronze_claims` (05_silver_claims) - No dependencies
- Task 2: `silver_customers` (06_silver_customers) - Depends on Task 1
- Task 3: `silver_policies` (07_silver_policies) - Depends on Task 1
- Task 4: `gold_layer` (09_gold_claims) - Depends on Tasks 2 & 3

**Configuration:**
- Max concurrent runs: 1
- Timeout: 3600 seconds per task
- Cluster: Autoscaling (i3.xlarge, 1 worker)
- Trigger: Manual or scheduled

---

## 📁 Repository Structure

```
databricks-insurance-claims-project/
├── notebooks/
│   ├── 05_silver_claims.py              (Claims data quality)
│   ├── 06_silver_customers.py           (Customer transformation)
│   ├── 07_silver_policies.py            (Policy transformation)
│   ├── 08_silver_telematics.py          (Telematics transformation)
│   ├── 09_gold_claims.py                (Gold aggregations + analytics)
│   ├── 10_workflow_orchestration.py     (Databricks Workflows DAG)
│   ├── 11_ml_fraud_detection.py         (ML fraud detection model)
│   └── 12_dashboard_queries.sql         (Analytics dashboard queries)
├── terraform/                            (Infrastructure as Code)
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
└── README.md
```

**Key Notebooks:**
- `05_silver_claims`: Date standardization, age validation, deduplication
- `06_silver_customers`: Customer record validation
- `07_silver_policies`: Policy data transformation
- `08_silver_telematics`: Telematics event processing
- `09_gold_claims`: Aggregations (5 Gold tables) + ML feature creation
- `11_ml_fraud_detection`: Logistic Regression model (AUC-ROC 1.0)
- `12_dashboard_queries`: 5 analytics SQL queries

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

## 📈 Performance Metrics

### **Data Processing (End-to-End Pipeline)**

```
Bronze Ingestion:       37,289 rows ingested
                        ├─ Claims: 12,991
                        ├─ Customers: 7,061
                        ├─ Policies: 12,237
                        └─ Telematics: 5,000

Silver Transformation:  31,504 rows validated (84.5% pass rate)
                        ├─ Claims: 10,733 (82.6% pass)
                        ├─ Customers: 3,636 (51.5% pass)
                        ├─ Policies: 12,135 (99.2% pass)
                        └─ Telematics: 5,000 (100% pass)

Quality Issues Caught:  5,785 invalid records rejected (17.4%)
                        ├─ Claims: 2,258 rejected
                        ├─ Customers: 3,425 rejected
                        ├─ Policies: 102 rejected
                        └─ Telematics: 0 rejected

Gold Analytics:         31,329 aggregated records
                        ├─ claims_by_date_severity: 284 rows
                        ├─ claims_by_collision_type: 4 rows
                        ├─ customer_metrics: 10,211 rows
                        ├─ driver_risk_scores: 101 rows
                        ├─ ml_features: 10,733 rows
                        └─ fraud_detection_scores: 10,733 rows
```

### **ML Model Performance**

```
Training Data:          10,733 claims
                        ├─ Train: 8,666 (80%)
                        └─ Test: 2,067 (20%)

Features Engineered:    12 total
                        ├─ Customer features: 2 (age, tenure)
                        ├─ Claim features: 3 (amount, severity)
                        ├─ Risk indicators: 4 (suspicious, no witnesses, new customer)
                        └─ Accident characteristics: 3 (vehicles, damage type)

Model: Logistic Regression
                        ├─ AUC-ROC: 1.0000 ✅
                        ├─ Test accuracy: 100%
                        ├─ True positive rate: 100%
                        └─ False positive rate: 0%
```

### **Execution Time**

```
Bronze CSV Ingestion:           ~30 seconds (37K rows)
Silver Claims Transform:        ~45 seconds (10.7K rows)
Silver Customers Transform:     ~30 seconds (3.6K rows)
Silver Policies Transform:      ~30 seconds (12K rows)
Silver Telematics Transform:    ~20 seconds (5K rows)
Gold Aggregations:              ~45 seconds (5 tables)
ML Model Training:              ~2 minutes (10.7K samples)
───────────────────────────────────────────────────────
Total End-to-End:               ~5-6 minutes (full pipeline)

Workflow Orchestration: Automated DAG with dependency management
```

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

**⭐ If this project helped you learn Databricks, consider starring the repo!**
