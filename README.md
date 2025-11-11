# 🚗 Car Insurance Claims Automation with Databricks

**End-to-end data engineering and ML project demonstrating modern lakehouse architecture**

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?logo=databricks&logoColor=white)](https://databricks.com)
[![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://python.org)
[![SQL](https://img.shields.io/badge/SQL-4479A1?logo=postgresql&logoColor=white)](https://www.databricks.com/glossary/what-is-sql)

---

## 📋 Project Overview

Automated car insurance claims processing system built on **Databricks Lakehouse Platform**. Ingests multi-source data (SQL Server, Kinesis streams, S3), applies ML-based damage classification, and provides real-time claims validation through dashboards and web applications.

### Business Problem

Manual claims processing is slow, error-prone, and expensive. This system:
- ✅ Automates claims validation (speed, eligibility, damage assessment)
- ✅ Reduces processing time from days to minutes
- ✅ ML-driven fraud detection via image classification
- ✅ Unified data platform for analytics

### Technologies Used

| Layer         | Technology         | Purpose                                |
|---------------|-------------------|----------------------------------------|
| Cloud         | AWS               | S3 storage, Kinesis streaming, RDS     |
| Data Platform | Databricks        | Lakehouse, Unity Catalog, LakeFlow      |
| Storage       | Delta Lake        | ACID transactions, time travel, CDC    |
| Orchestration | LakeFlow Pipelines| ETL/ELT automation                     |
| ML Framework  | MLflow + Mosaic AI| Model training, tracking, serving      |
| BI/Analytics  | Databricks SQL + Genie | Dashboards, natural language queries|
| Applications  | Databricks Apps   | Claims submission portal               |

---

## 🏗️ Architecture

### Medallion Architecture

The Medallion Architecture (Bronze → Silver → Gold) organizes the data pipeline for clarity and governance:

- **Bronze**: Raw ingested data (as-is, no business logic)
- **Silver**: Cleaned and validated data (DQT, business rules)
- **Gold**: Analytics-ready, aggregated data

Flow:
```
SQL Server (CDC)         Kinesis          S3 Images
      |                    |                 |
LakeFlow Connect      LakeFlow Streaming   AutoLoader
      |                    |                 |
               LANDING (raw files)
                       |
              BRONZE (raw Delta tables)
                       |
                Data Cleaning, QA
                       |
               SILVER (validated data)
                       |
           Aggregations, ML/Analytics
                       |
               GOLD (business outputs)
```

---

### Unity Catalog Structure

```
smart_claims_dev (Catalog)
├── landing  # Landing zone/raw files
├── bronze   # Raw Delta tables
├── silver   # Cleaned + validated data
└── gold     # Analytics-ready/aggregates
```

Each "schema" maps to a medallion zone; governance is handled at this level.

---

## 📁 Project Structure

```
databricks-insurance-claims-project/
├── notebooks/
│   ├── 01_setup/              # Unity Catalog, initial scripts
│   ├── 02_ingestion/          # Data pipelines (Kinesis, SQL Server, S3)
│   ├── 03_transformations/    # Bronze → Silver → Gold ETL
│   ├── 04_ml/                 # ML model notebooks
│   └── 05_apps/               # Databricks App notebooks
├── docker/
│   └── sql_server/            # Local SQL Server for CDC
├── data/
│   └── sample_data/           # Demo datasets
├── docs/
│   └── architecture.png       # Diagrams
└── README.md
```

---

## 📊 Features Implemented

#### ✅ Phase 1: Data Ingestion
- [x] SQL Server CDC ingestion (LakeFlow Connect)
- [x] Real-time streaming from Kinesis
- [x] S3 Auto Loader for images & metadata

#### ✅ Phase 2: Data Transformations
- [x] Medallion architecture (Bronze → Silver → Gold)
- [x] Data quality validations (DLT expectations)

#### ✅ Phase 3: Machine Learning
- [ ] Car damage classifier (ResNet, MLflow)
- [ ] Model serving via REST API

#### ✅ Phase 4: Analytics & Apps
- [ ] SQL dashboards (claims KPIs)
- [ ] Genie interface (NLQ)
- [ ] Claims submission portal

---

## 🚀 Getting Started

### Prerequisites

Install:
- Python 3.13+
- Docker Desktop
- AWS CLI v2.24+
- Git

Accounts:
- Databricks Free/Trial Edition
- AWS Free Tier
- GitHub

### Setup Instructions

#### 1. Clone Repository

```bash
git clone https://github.com/dilip-ch-dev/databricks-insurance-claims-project.git
cd databricks-insurance-claims-project
```

#### 2. AWS Configure

```bash
aws configure
# Enter Access/Secret/Region
```

#### 3. Run SQL Server (Docker)
```bash
cd docker/sql_server
docker-compose up -d
```

---

## 🎓 Learning Outcomes

- **Data Engineering**: Medallion patterns, Unity Catalog, CDC, streaming, Delta Lake
- **ML Engineering**: Computer vision, MLflow tracking, model deployment
- **Cloud/DevOps**: AWS integration, Docker, Git/GitHub best practices

---

## 📝 License

MIT License

---

## 👤 Author

**[Your Name]**
- GitHub: [@dilip-ch-dev](https://github.com/dilip-ch-dev)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-profile)

---

**⭐ Star this repo if it helps you!**
