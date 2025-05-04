# 🚲 NextBike Poland – Trip Prediction using Machine Learning

This project showcases end-to-end machine learning workflows using synthetic bike-sharing data modeled after NextBike usage in Poland. It includes two main predictive tasks:

- 🔢 **Trip Duration Prediction** (Regression)
- 📍 **Trip End Station Prediction** (Classification)

> 📁 The project is designed as a portfolio piece to demonstrate technical proficiency in data preprocessing, feature engineering, and supervised ML modeling.

---

## 📊 Dataset

- **Synthetic Data:** Based on real-world schema of trip data (1M+ records)
- Fields include: `start_date`, `strt_statn`, `end_statn`, `duration`, `birth_date`, `gender`, `subsc_type`, etc.
- Dates were shifted to simulate recent years (2021–2023).

---

## 🧠 ML Tasks

### 1. Trip Duration Prediction
- **Target:** `duration` (in minutes)
- **Models Used:** Linear Regression, Random Forest, XGBoost
- **Features:** Start station, time features, user age, gender, subscription type

### 2. End Station Prediction
- **Target:** `end_statn`
- **Models Used:** Random Forest, XGBoost, LightGBM
- **Features:** Start station, start time, demographics, bike number

---

## ⚙️ Tech Stack

- Python (Pandas, NumPy)
- Scikit-learn
- XGBoost / LightGBM
- Jupyter Notebooks
- Matplotlib / Seaborn
- GitHub for version control

---

## 📁 Project Structure

nextbike-poland-ml/
│
├── data/ # Sample or generated dataset
├── notebooks/ # EDA and modeling notebooks
├── src/ # Modular code for preprocessing and training
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ └── model_training.py
├── models/ # Saved models (optional)
├── requirements.txt # Dependencies
└── README.md # This file


---

## 📈 Results

- Regression models predicted trip duration with high accuracy (RMSE & R² reported).
- Classification models achieved high precision in predicting end stations.
- Clear improvements observed with feature engineering and model tuning.

---

## 💡 Purpose

This project was developed as a portfolio demonstration of practical ML skills and is linked from my CV.

---


