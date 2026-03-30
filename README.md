# customer-churn-analysis

## 📌 Overview
This project predicts customer churn using machine learning models based on customer behavior and usage patterns.

## 📊 Dataset
Telco customer dataset containing customer demographics, tenure, and service usage.

## 🛠 Tools Used
- Python (Pandas, NumPy)
- Scikit-learn
- Matplotlib, Seaborn
- Power BI

## 📈 Results
- Logistic Regression Accuracy: 80.4%
- Random Forest Accuracy: 80.2%

## 🔍 Key Insights
- Customers with higher monthly charges are more likely to churn
- Customers with shorter tenure have higher churn rate
- Contract type significantly impacts churn behavior

## 📎 Project Structure

customer-churn-analysis/
│
├── data/
│   └── customer_churn.csv        # Dataset used for analysis
│
├── notebooks/
│   └── churn_analysis.ipynb      # Jupyter Notebook with full analysis
│
├── images/
│   └── churn_feature_importance.png   # Visualizations
│
├── dashboard/
│   └── churn_dashboard.pbix      # Power BI dashboard (optional)
│
├── requirements.txt              # Python dependencies
│
└── README.md                    # Project documentation
