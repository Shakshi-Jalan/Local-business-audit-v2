# Local Business Audit – Restaurant Analysis V2

## 📌 Project Overview

This project analyzes customer reviews, ratings, complaints, sentiment, and menu prices of three local restaurants to understand their competitive performance.

The project is an upgraded version of a previous restaurant audit. Version 2 uses **Python and Pandas for data cleaning and analysis**, **VADER for sentiment analysis**, and **Power BI for interactive visualization and business reporting**.

### Restaurants analyzed

* Dwaraka Grand
* Sri Krishna Aramane
* Udupi Swada

---

## 🎯 Business Question

> **Why is the target restaurant underperforming in customer ratings despite charging a premium price, and what operational or pricing actions could improve its competitive position?**

The analysis focuses on identifying:

* Customer sentiment
* Major complaint categories
* Problems associated with low ratings
* Restaurant-level performance
* Menu price differences
* Potential value-for-money concerns
* Priority areas for improvement

---

## 🎯 Project Objectives

1. Compare the average ratings of the three restaurants.
2. Analyze customer sentiment using VADER.
3. Identify the most common complaint categories.
4. Identify problems appearing in low-rated reviews.
5. Compare negative sentiment across complaint categories.
6. Analyze restaurant-level menu prices.
7. Compare price and rating performance.
8. Create a priority score to identify important problem areas.
9. Prepare analytical datasets for Power BI.
10. Build an interactive three-page business dashboard.

---

## 📂 Data Note

The review dataset used in this project contains **constructed/assumed review data for analysis purposes**.

The reviews and review dates should **not be interpreted as live scraped Google Reviews or verified real-world customer data**.

This project is intended to demonstrate a complete **data analytics workflow**, including data cleaning, sentiment analysis, exploratory analysis, business diagnosis, and dashboard development.

---

# 🔄 Project Workflow

```text
Raw Excel Data
      ↓
Python / Pandas
      ↓
Data Quality Checks
      ↓
Exploratory Data Analysis
      ↓
VADER Sentiment Analysis
      ↓
Complaint Category Analysis
      ↓
Low-Rating Problem Analysis
      ↓
Priority Score
      ↓
Restaurant & Menu Price Benchmarking
      ↓
CSV Export
      ↓
Power BI
      ↓
Interactive Business Dashboard
```

---

# 🛠️ Tech Stack

### Programming & Analysis

* Python
* Pandas

### Sentiment Analysis

* VADER Sentiment Analyzer

### Visualization & Reporting

* Microsoft Power BI
* DAX

### Data Source

* Excel

---

# 🐍 Python Analysis

The Python script performs several stages of analysis.

## 1. Data Loading

The project reads the review and menu data from the Excel workbook using Pandas.

The review dataset contains **300 review records** across the three restaurants. 

---

## 2. Data Quality Check

The script checks:

* Dataset shape
* Column names
* Missing values
* Duplicate rows
* Data types

This ensures that the data is suitable for further analysis. 

---

## 3. Restaurant Analysis

The analysis calculates:

* Number of reviews per restaurant
* Average rating per restaurant

This provides the initial comparison of restaurant performance. 

---

## 4. VADER Sentiment Analysis

VADER is applied to the review text to generate a **compound sentiment score**.

The score is classified into:

* Positive
* Neutral
* Negative

using predefined thresholds. 

---

## 5. Sentiment Validation

The VADER results are compared with the existing manual sentiment labels.

The project calculates the percentage of reviews where the manual sentiment and VADER sentiment agree. 

### Result

**VADER agreement: 79.33%**

This indicates that VADER broadly agrees with the manually assigned sentiment, while also identifying some differences.

---

## 6. Rating–Sentiment Mismatch

The project identifies reviews where:

* Rating is ≤ 2 but VADER sentiment is Positive
* Rating is ≥ 4 but VADER sentiment is Negative

This helps identify cases where **star ratings and review text tell different stories**. 

---

## 7. Complaint Analysis

Complaint categories are analyzed to understand what customers discuss most frequently.

The project calculates:

* Overall complaint distribution
* Complaint distribution by restaurant
* Percentage distribution of complaint categories within each restaurant 

### Major complaint categories

* Food Quality
* Overall Experience
* Hygiene
* Staff Behaviour
* Service
* Ambience
* Pricing

---

## 8. Negative Sentiment by Complaint Category

The project calculates the percentage of negative VADER sentiment within each complaint category.

This helps distinguish between categories that are simply common and categories that are associated with stronger negative sentiment. 

---

## 9. Restaurant + Complaint Analysis

A combined analysis is created using:

* Restaurant
* Complaint Category
* Total Reviews
* Negative Reviews
* Negative Percentage

This provides a restaurant-specific view of customer problems. 

---

# 🚨 Low-Rating Problem Analysis

Reviews with ratings of **1 or 2 stars** are analyzed separately.

For each restaurant and complaint category, the project calculates:

* Number of low-rating reviews
* Number of negative VADER reviews
* Negative percentage

This helps identify problems specifically associated with poor-rated experiences. 

---

# 🧮 Priority Score

A project-defined heuristic is used to prioritize problems:

```text
Priority Score =
Low-Rating Reviews × Negative Percentage
```

The score combines **problem volume** and **negative sentiment**.

> **Note:** This is a project-defined prioritization heuristic, not a formal statistical measure.

The highest-scoring problems can then be used to guide business recommendations. 

---

# ⭐ Key Findings

### Restaurant Ratings

| Restaurant          | Average Rating |
| ------------------- | -------------: |
| Dwaraka Grand       |       **3.34** |
| Sri Krishna Aramane |       **2.93** |
| Udupi Swada         |       **3.34** |

Dwaraka Grand and Udupi Swada have the same average rating, while Sri Krishna Aramane has the lowest average rating.

---

### 😡 Negative Sentiment

| Restaurant          | Negative Reviews |
| ------------------- | ---------------: |
| Dwaraka Grand       |          **27%** |
| Sri Krishna Aramane |          **41%** |
| Udupi Swada         |          **30%** |

Sri Krishna Aramane has the highest percentage of negative reviews among the three restaurants.

---

### 🍽️ Most Common Complaint

**Food Quality** is the most common complaint category, with **153 reviews** across the dataset.

Other important complaint areas include:

* Overall Experience
* Hygiene
* Staff Behaviour
* Service

---

### 💰 Pricing

Average menu prices:

| Restaurant          | Average Menu Price |
| ------------------- | -----------------: |
| Dwaraka Grand       |           **₹114** |
| Udupi Swada         |            **₹98** |
| Sri Krishna Aramane |            **₹88** |

Dwaraka Grand has the highest average menu price.

Dwaraka is approximately **16% more expensive than Udupi Swada while having the same average rating of 3.34**.

This raises a **value-for-money question**, but the analysis does not establish that price causes dissatisfaction.

---

### 🤖 Sentiment Validation

VADER sentiment showed **79.33% agreement** with the existing manual sentiment labels.

The analysis also found some cases where rating and text sentiment did not match, showing that customer ratings and written feedback can provide different signals.

---

# 🔎 Restaurant-Level Problem Areas

### Dwaraka Grand

Key problem areas identified:

* Food Quality
* Service
* Staff Behaviour

### Sri Krishna Aramane

Key problem areas identified:

* Food Quality
* Overall Experience
* Staff Behaviour

### Udupi Swada

Key problem areas identified:

* Hygiene
* Food Quality
* Staff Behaviour

---

# 📊 Power BI Dashboard

The final Power BI dashboard contains **three pages**.

## Page 1 — Executive Overview

The overview page compares the three restaurants using:

* Average Restaurant Rating
* Average Negative Review %
* Average Menu Price
* Average Rating by Restaurant
* Rating Distribution
* Negative Review % by Restaurant
* Price vs. Rating by Restaurant

### Main question answered:

> **How are the three restaurants performing overall?**

---

## Page 2 — Customer Sentiment & Complaints

This page focuses on customer feedback.

It includes:

* Total Reviews
* Negative Reviews
* Customer Sentiment Distribution
* Complaint Category Distribution
* Negative Sentiment % by Complaint Category
* Complaint Categories by Restaurant

### Main question answered:

> **What are customers talking about and complaining about?**

---

## Page 3 — Problem Diagnosis

This page focuses on identifying actionable problem areas.

It includes:

* Low-Rating Reviews
* Negative Low-Rating Reviews
* Highest Priority Problem
* Problem Priority by Restaurant
* Low-Rating Problem Analysis

### Main question answered:

> **Which problems should the restaurant prioritize for improvement?**

---

## Dashboard Preview

### 1. Overview

![Overview Dashboard](screenshots/overview.png)

### 2. Customer Sentiment & Complaints

![Customer Sentiment & Complaints](screenshots/customer_sentiment_complaints.png)

### 3. Problem Diagnosis

![Problem Diagnosis](screenshots/problem_diagnosis.png)

---

# 💡 Business Recommendations

Based on the analysis, the target restaurant should focus on:

### 1. Improve Food Quality

Food Quality is the largest complaint category and appears as a major problem in low-rated reviews.

Possible actions:

* Monitor food consistency
* Review frequently criticized dishes
* Improve preparation and quality checks
* Track recurring food-related complaints

### 2. Improve Service

Service-related complaints should be monitored, particularly where they contribute to low-rated experiences.

### 3. Improve Staff Behaviour

Staff behaviour appears as an important problem area for multiple restaurants.

Training and customer-service monitoring could help improve the overall customer experience.

### 4. Strengthen Value Proposition

Dwaraka Grand has the highest average menu price but the same average rating as Udupi Swada.

Instead of immediately reducing prices, the restaurant could focus on **communicating and improving the value customers receive**.

Possible actions include:

* Value-based meal combinations
* Better portion/value perception
* Promotions on selected dishes
* Highlighting quality improvements

---

# ⚠️ Limitations

This project has several limitations:

* The review dataset is constructed/assumed rather than live scraped customer data.
* The analysis contains only **300 reviews**.
* Only three restaurants are included.
* The sample may not represent the complete customer base.
* VADER is a general sentiment-analysis tool and may not perfectly understand every review.
* Rating and sentiment mismatches show that automated sentiment analysis should be interpreted alongside the original review text.
* The Priority Score is a project-defined heuristic.
* The analysis identifies patterns and associations but does not establish causal relationships.
* Very small complaint categories should not be interpreted strongly.

---

# 🚀 Future Improvements

Possible future improvements include:

* Use a larger real-world review dataset.
* Collect reviews across a longer time period.
* Use NLP models better suited for restaurant reviews.
* Perform topic modeling to automatically discover complaint themes.
* Track sentiment trends over time using verified review dates.
* Add competitor dish-level price benchmarking.
* Build automated data pipelines for regularly updated dashboards.
* Add statistical testing to evaluate relationships between variables.

---

# 📁 Project Structure

```text
Local-Business-Audit-V2/
│
├── analysis.py
│
├── Local business audit.xlsx
│
├── restaurant_benchmark.csv
├── problem_analysis.csv
├── rating_summary.csv
├── review_analysis.csv
├── dish_price_comparison.csv
├── low_rating_analysis.csv
│
├── Local Business Audit V2.pbix
│
├── images/
│   ├── page1_overview.png
│   ├── page2_sentiment.png
│   └── page3_diagnosis.png
│
└── README.md
```

---

# ▶️ How to Run the Python Analysis

### 1. Install the required libraries

```bash
pip install pandas openpyxl vaderSentiment
```

### 2. Keep the Excel file and Python script in the same folder

```text
analysis.py
Local business audit.xlsx
```

### 3. Run the script

```bash
python analysis.py
```

The script will generate the analytical CSV files required for Power BI.

---

# 📤 Output Files

The Python script generates:

| File                        | Purpose                                                    |
| --------------------------- | ---------------------------------------------------------- |
| `restaurant_benchmark.csv`  | Restaurant price, rating and negative-review benchmark     |
| `problem_analysis.csv`      | Restaurant-level complaint and negative sentiment analysis |
| `rating_summary.csv`        | Low-rating and high-rating rates                           |
| `review_analysis.csv`       | Final review-level analytical dataset                      |
| `dish_price_comparison.csv` | Dish-level price comparison                                |
| `low_rating_analysis.csv`   | Low-rating problem and priority analysis                   |

The CSV outputs are then used to build the Power BI dashboard. The export section of the Python script explicitly creates these analytical files. 

---

# 🧰 Skills Demonstrated

This project demonstrates practical skills in:

* Data Cleaning
* Exploratory Data Analysis
* Pandas
* Sentiment Analysis
* VADER
* Data Aggregation
* GroupBy
* Crosstab Analysis
* Business Problem Diagnosis
* Competitor Benchmarking
* Pricing Analysis
* Power BI
* DAX
* Dashboard Design
* Business Recommendations

---

# 👩‍💻 Author

**Shakshi Jalan**

Aspiring Data Analyst | Python | SQL | Power BI | Excel | Data Visualization

---

## ⭐ Project Summary

This project demonstrates how raw customer review and menu data can be transformed into **business insights using Python and Power BI**.

The analysis moves beyond basic dashboarding by combining **customer sentiment, complaint categories, low-rating analysis, pricing, competitor benchmarking, and problem prioritization** to identify areas where a restaurant can improve its competitive position.

---

