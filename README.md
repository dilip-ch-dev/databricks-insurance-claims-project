# 🚗 Databricks Insurance Claims Automation Project

**End-to-end data engineering and ML project for learning Databricks Lakehouse Platform**

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?logo=databricks&logoColor=white)](https://databricks.com)
[![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://python.org)

---

## 📋 Project Overview

Automated car insurance claims processing system demonstrating:
- **Unity Catalog governance** (medallion architecture)
- **Multi-source data ingestion** (SQL Server CDC, Kinesis streams, S3 Auto Loader)
- **ML-based damage classification** (Computer vision with MLflow)
- **Real-time dashboards** (Databricks SQL + AI/BI)
- **Web application** (Databricks Apps for claims portal)

### Business Use Case
**Problem**: Manual insurance claims processing is slow, error-prone, and expensive.

**Solution**: Automated claims validation system that:
- ✅ Verifies driver speed from telematics data
- ✅ Checks policy eligibility for refunds
- ✅ Classifies car damage severity using ML image analysis
- ✅ Provides real-time analytics for claim approval decisions

---

## 🏗️ Architecture

### Medallion Architecture

┌─────────────┐ ┌──────────────┐ ┌─────────────┐
│ SQL Server │ │ Kinesis │ │ S3 Images │
│ (CDC) │ │ (Streaming) │ │(Auto Loader)│
└──────┬──────┘ └──────┬───────┘ └──────┬──────┘
│ │ │
└────────┬────────┴──────────────────┘
│
┌──────▼──────┐
│ LANDING │ (Raw files/volumes)
└──────┬──────┘
│
┌──────▼──────┐
│ BRONZE │ (Raw Delta tables)
└──────┬──────┘
│ Data Quality + Cleaning
┌──────▼──────┐
│ SILVER │ (Validated data)
└──────┬──────┘
│ Aggregations + ML
┌──────▼──────┐
│ GOLD │ (Analytics-ready)
└──────┬──────┘
│
┌─────────┴──────────┐
│ │
┌────▼─────┐ ┌───────▼────┐
│Dashboards│ │Claims Portal│
│ + Genie │ │ (App) │
└──────────┘ └─────────────┘

### Unity Catalog Structure

smart_claims_dev (Catalog)
├── landing - Raw file ingestion
├── bronze - Raw Delta tables
├── silver - Cleaned & validated
└── gold - Analytics aggregates
---

## 🛠️ Technologies

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Cloud Platform** | AWS (Free Tier) | S3, Kinesis, EC2 |
| **Data Platform** | Databricks Free Edition | Lakehouse, Unity Catalog |
| **Storage** | Delta Lake | ACID transactions, time travel |
| **Orchestration** | LakeFlow Pipelines | ETL automation |
| **ML** | MLflow + Mosaic AI | Model tracking, serving |
| **Database** | SQL Server (Docker) | Source data with CDC |
| **Version Control** | Git + GitHub | Code management |

---

## 📁 Project Structure

databricks-insurance-claims-project/
├── sql_queries.sql # Unity Catalog setup + transformations
├── notebooks/ # (Future) Python notebooks
├── pipelines/ # (Future) LakeFlow pipeline configs
├── data/ # (Future) Sample datasets
└── docs/ # (Future) Documentation

---

## 🚀 Progress Tracker

### ✅ Completed
- [x] Unity Catalog created (`smart_claims_dev`)
- [x] Medallion architecture schemas (landing/bronze/silver/gold)
- [x] Git integration with GitHub
- [x] Databricks Free Edition workspace setup

### 🔄 In Progress
- [ ] AWS S3 bucket configuration
- [ ] SQL Server Docker setup with CDC
- [ ] Kinesis data stream ingestion

### 📋 Planned
- [ ] LakeFlow Connect (SQL Server CDC)
- [ ] Auto Loader (S3 file ingestion)
- [ ] Bronze → Silver transformations
- [ ] Silver → Gold aggregations
- [ ] ML model training (car damage classifier)
- [ ] Databricks SQL dashboards
- [ ] Genie AI/BI interface
- [ ] Claims submission portal (Databricks Apps)

---

## 🎓 Learning Outcomes

**Data Engineering**:
- Unity Catalog governance
- Medallion architecture pattern
- Change Data Capture (CDC)
- Stream processing
- Delta Lake optimization

**Machine Learning**:
- Computer vision (ResNet)
- MLflow lifecycle management
- Model serving endpoints

**Cloud & DevOps**:
- AWS integration (S3/Kinesis)
- Docker containerization
- Git version control

---

## 📝 Documentation

- **Setup Guide**: See `sql_queries.sql` for step-by-step Unity Catalog setup
- **Tutorial Reference**: Based on [Thomas Hass - Databricks Zero to Hero](https://youtu.be/gFAnlTM-3Zo)
- **Code Repository**: [GitHub - datamyselfai/databricks-zero-to-hero-course](https://github.com/datamyselfai/databricks-zero-to-hero-course)

---

## 👤 Author

**[Your Name]**  
📧 Email: dilip77950@gmail.com  
💼 LinkedIn: [Add your LinkedIn profile]  
🎯 Goal: Master Databricks for data engineering roles

---

## 📄 License

MIT License - Free to use for learning purposes

---

**⭐ Star this repo if you find it helpful for your Databricks learning journey!**

*Last Updated: November 10, 2025*

