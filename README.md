# 📊 Olist E-commerce Data Analysis

## 📌 Overview

This project analyzes the **Olist Brazilian E-commerce dataset**, a real-world marketplace dataset, to uncover actionable insights into sales performance, customer behavior, and delivery operations.

The analysis follows a complete data workflow, from data cleaning and preprocessing to exploratory analysis and visualization.

---

## 🎯 Objectives

* Analyze the full order lifecycle
* Understand key drivers of sales and delivery performance
* Identify patterns in customer behavior
* Detect operational issues such as delays and cancellations

---

## 🗂️ Dataset

* Source: Olist Brazilian E-commerce Dataset (Kaggle)
* Type: Multi-table relational dataset
* Main tables:

  * Orders
  * Customers
  * Products
  * Payments
  * Deliveries
  * Reviews

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Matplotlib / Seaborn
* Plotly
* Jupyter Notebook

---

## 🔍 Analysis Performed

### 🧹 Data Cleaning & Preprocessing

* Handling missing values
* Date/time conversion
* Merging multiple relational tables
* Feature engineering (e.g., delivery time calculation)

### 📊 Exploratory Data Analysis (EDA)

* Order trends over time
* Payment analysis (methods and installments)
* Customer review distribution
* Geographic analysis of sales

### 🚚 Delivery & Logistics

* Comparison between estimated and actual delivery dates
* Identification of delayed shipments
* Delivery performance analysis

### 💳 Payments

* Most used payment methods
* Relationship between installments and order value

### ⭐ Customer Experience

* Review score distribution
* Impact of delivery delays on customer satisfaction

---

## 📈 Key Insights

* Delivery times show significant variability
* Delays have a clear negative impact on customer reviews
* A few payment methods dominate the platform
* Sales exhibit clear temporal patterns (trends and seasonality)

---

## 📊 Visualizations

The project includes multiple visualizations to support insights:

* Time series of orders
* Distributions and histograms
* Correlation heatmaps
* Interactive charts using Plotly

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash id="qv9d8n"
git clone https://github.com/your-username/olist-analysis.git
```

2. Navigate to the project folder:

```bash id="1g2y0u"
cd olist-analysis
```

3. Install dependencies:

```bash id="nqv2fd"
pip install -r requirements.txt
```

4. Launch the notebook:

```bash id="s0u9n6"
jupyter notebook
```

---

## 📁 Project Structure

```id="zq7z7g"
├── data/              # dataset files
├── notebooks/         # main analysis notebook
├── images/            # exported visualizations
├── requirements.txt
└── README.md
```

---

## 💡 Future Improvements

* Build an interactive dashboard (Streamlit / Dash)
* Develop predictive models (e.g., delivery delay prediction)
* Customer segmentation (clustering)
* Advanced retention and churn analysis
