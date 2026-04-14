# 🛒 Olist E-commerce Analysis — Customer Intelligence & Logistics

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Portfolio%20Project-2ecc71?style=flat-square)

**End-to-end data analysis on Brazil's largest e-commerce platform — from raw SQL to actionable customer intelligence.**

</div>

---

## 📌 Overview

This project delivers a full analytical pipeline on the **Olist dataset** (100k+ orders, ~1.5M records), covering sales performance, logistics efficiency, customer segmentation, and NLP-based sentiment analysis.

The goal: simulate a real **Data Analyst / Data Scientist workflow** — connecting to a relational database, engineering features, training unsupervised models, and extracting business-ready insights.

---

## 🎯 Key Results

| Area | Finding |
|---|---|
| **Logistics** | 85% of deliveries arrive before the estimated date |
| **Revenue** | Clear seasonal peaks identified in the 2016–2018 trend |
| **Segmentation** | 4 distinct customer clusters via RFM + K-Means |
| **NLP** | Delivery timeliness is the #1 driver of 5-star reviews |
| **Geo-analysis** | Northern states have 2× higher freight costs and delivery times |

---

## 🗂️ Project Structure

```
olist-ecommerce-analysis/
│
├── Portfolio_Olist_Analysis.ipynb   # Main analysis notebook
├── .env.example                     # DB credentials template
├── requirements.txt                 # Python dependencies
└── README.md
```

---

## 🔍 Analysis Modules

### 1. Sales Performance
Monthly revenue trend (2016–2018) with seasonality detection using time-series visualization.

### 2. Logistics Efficiency
Distribution of `delivery_delta` (real vs. estimated date). SQL query joins orders and calculates DATEDIFF at scale.

### 3. RFM Customer Segmentation
- **Recency, Frequency, Monetary** features extracted via SQL aggregations
- `StandardScaler` normalization → `KMeans (k=4)` clustering
- Scatter plot: Recency vs Monetary, colored by cluster

### 4. NLP Sentiment Analysis
- **TextBlob** polarity scoring on ~40k review texts (Portuguese)
- **WordCloud** for 1-star and 5-star reviews separately
- Boxplot: review score vs. NLP polarity correlation

### 5. Geo-spatial Logistics
Bar + line dual-axis chart: average delivery time and freight cost per Brazilian state (`customer_state`).

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **MySQL + SQLAlchemy** | Relational DB queries, data extraction |
| **Pandas / NumPy** | Data wrangling and feature engineering |
| **Seaborn / Matplotlib** | Statistical and exploratory visualization |
| **Scikit-learn** | StandardScaler, KMeans clustering |
| **TextBlob** | Sentiment polarity scoring |
| **WordCloud** | Keyword visualization from review text |

---

## ⚙️ Setup & Run

### 1. Clone the repo
```bash
git clone https://https://github.com/EricaZampella/portfolio_ecommerce/blob/main/Portfolio_Olist_Analysis.ipynb
cd olist-ecommerce-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure database credentials
```bash
cp .env.example .env format:

```
DB_USER=
DB_PASS=
DB_HOST=
```

### 4. Load the dataset
Download the [Olist dataset from Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and import it into a MySQL database named `olist_ecommerce`.

### 5. Run the notebook
```bash
jupyter notebook Portfolio_Olist_Analysis.ipynb
```

---

## 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
sqlalchemy
mysql-connector-python
python-dotenv
scikit-learn
wordcloud
textblob
jupyter
```

---

## 💡 Business Insights

- **Retention campaigns**: The RFM model identifies a "high-value but inactive" segment — ideal target for win-back offers.
- **Regional logistics**: Freight cost optimization is critical for the North and Northeast states; regional fulfillment hubs could reduce delivery times significantly.
- **Product strategy**: Sentiment analysis reveals that late deliveries, not product quality, drive negative reviews — logistics is the primary lever for CSAT improvement.

---

## 🚀 Future Development

- [ ] **Customer Churn Prediction** — supervised classification model (Logistic Regression / XGBoost)
- [ ] **Market Basket Analysis** — association rules (Apriori) for cross-sell recommendations
- [ ] **Interactive Dashboard** — Plotly Dash or Streamlit deployment
- [ ] **Multilingual NLP** — swap TextBlob for a Portuguese-native model (e.g., BERTimbau)

---

## 📄 Dataset

**Brazilian E-Commerce Public Dataset by Olist**
- Source: [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- License: CC BY-NC-SA 4.0
- ~100,000 orders | 2016–2018 | 9 relational tables

---


<div align="center">
<sub>Built with Python, SQL, and a lot of Brazilian data ☕</sub>
</div>
