# Retail Sales Performance Analytics & ETL Pipeline

An end-to-end data analytics and engineering project that transitions exploratory retail analysis into a structured, production-ready data pipeline. This project optimizes raw transactional data extraction using SQL, applies automated data cleansing and KPI calculation in Python, and establishes a modular ETL framework.

##  Business Objective
Retail datasets are frequently plagued by structural anomalies, missing transactional records, and unoptimized schemas. The goal of this project is to build an automated system that ingests raw retail data, cleanses transactional noise, and surfaces high-value KPIs (such as sales trends, customer segmentation, and product performance) for business stakeholders.

---

##  Tech Stack & Tools
*   **Language:** Python 3.x, SQL
*   **Libraries:** Pandas, NumPy, SQLAlchemy (or your database connector)
*   **Environments:** Jupyter Notebook (Exploratory Phase), VS Code (Pipeline Development)
*   **Database:** [Insert Database Name, e.g., PostgreSQL / MySQL / SQLite]

---

## Architecture & Project Structure
The project was migrated from a single, monolithic exploratory Jupyter Notebook into a modular, production-grade script pipeline to support automated execution and scaling.

```text
├── notebooks/
│   └── Retail_Sales_Analysis.ipynb    # Initial exploratory data analysis (EDA)
├── scripts/
│   ├── extract.py                      # Database connection & raw SQL queries
│   ├── transform.py                    # Data cleansing, type casting, & KPI logic
│   └── load.py                         # Targets warehouse ingestion
├── main.py                             # Pipeline orchestrator & execution entry point
├── .env.example                        # Template for secure database credentials
├── requirements.txt                    # Managed Python dependencies
└── README.md                           # Documentation
```

---

## 📊 Key Analytics & Insights Covered
The pipeline processes raw transaction rows to extract critical business metrics:
*   **Sales Performance:** Year-over-Year (YoY) growth, monthly revenue velocity, and peak sales periods.
*   **Product Analytics:** Top-performing categories, inventory turnover anomalies, and basket size tracking.
*   **Customer Cohorts:** Retention indicators and high-value customer segmentation based on purchasing frequency.

---

## ⚙️ Data Pipeline Implementation (ETL)

1. **Extract:** Securely connects to the database via environment variables (`.env`) and executes optimized SQL queries using database-level pushdown aggregations to minimize local memory overhead.
2. **Transform:** Utilizes Python (Pandas) to automatically resolve structural anomalies, standardize null values, cast corrupted data types, and run KPI logic.
3. **Load:** Formats and writes clean analytical tables back to the reporting layer or data warehouse.

---

## Getting Started

### 1. Prerequisites
Clone the repository and navigate to the directory:
```bash
git clone https://github.com
cd Retail_Sales_Analysis
```

### 2. Environment Setup
Install the necessary package dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
Configure your database credentials securely. Copy the template and fill in your details:
```bash
cp .env.example .env
```

### 4. Running the Pipeline
To execute the automated pipeline from extraction to final data load, run:
```bash
python main.py
```
