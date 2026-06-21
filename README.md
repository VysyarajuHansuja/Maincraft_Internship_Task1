# 🏠 California House Price Predictor

A Machine Learning project that predicts California house prices using **Linear Regression** and provides real-time predictions through a **Streamlit web application**.

## 📌 Project Overview

This project demonstrates the complete Machine Learning workflow:

* Data Loading
* Exploratory Data Analysis (EDA)
* Data Visualization
* Model Training using Linear Regression
* Model Evaluation
* Streamlit Deployment

The model is trained on the California Housing Dataset available in Scikit-Learn.

---

## 📊 Dataset Information

The California Housing Dataset contains housing-related information collected from the California census.

### Features

* MedInc (Median Income)
* HouseAge (House Age)
* AveRooms (Average Rooms)
* AveBedrms (Average Bedrooms)
* Population
* AveOccup (Average Occupancy)
* Latitude
* Longitude

### Target Variable

* MedHouseVal (Median House Value)

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit

---

## 📈 Exploratory Data Analysis

The following analyses were performed:

* Missing Value Analysis
* Statistical Summary
* House Price Distribution
* Correlation Heatmap
* Actual vs Predicted Visualization
* Residual Analysis

---

## 🤖 Machine Learning Model

### Algorithm Used

**Linear Regression**

Linear Regression was selected because it is simple, interpretable, and suitable for predicting continuous numerical values such as house prices.

### Evaluation Metrics

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## 🚀 Streamlit Application

The project includes an interactive Streamlit web application where users can:

* Enter housing features
* Predict house prices instantly
* View results in a user-friendly interface

### Live Demo

🔗 [Add Your Streamlit Link Here]

---

## 📂 Project Structure

```text
California-House-Price-Predictor/
│
├── app.py
├── task1_ml_linear_regression.ipynb
├── house_price_model.pkl
├── requirements.txt
├── README.md
└── report.pdf
```

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/California-House-Price-Predictor.git
cd California-House-Price-Predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---


## 🎯 Future Improvements

* Random Forest Regressor
* XGBoost Regressor
* Hyperparameter Tuning
* Feature Engineering
* Advanced Model Comparison

---

## 👨‍💻 Author

**Vysyaraju Hansuja**

B.Tech – Computer Science and Engineering
Veer Surendra Sai University of Technology (VSSUT), Burla

GitHub: https://github.com/VysyarajuHansuja
