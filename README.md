
### 🏠 HousePrediction

**HousePrediction** is a machine learning project that predicts house prices based on various input features such as area, location, number of bedrooms, and more. The project uses a **Streamlit interface** for interactive predictions and visualisation. It also includes complete **data preprocessing, cleaning, and model training** steps using modern data science tools.

---

#### 🚀 Features

* Comprehensive **data cleaning and preprocessing** using `pandas` and `LabelEncoder`
* **Exploratory Data Analysis (EDA)** and visualization with `matplotlib` and `seaborn`
* **Model training** using `XGBoost (XGBRegressor)` for high-performance regression
* **Model evaluation** with metrics like Mean Absolute Error (MAE) and R² Score
* **Streamlit interface** for user-friendly interaction and result visualization
* Model persistence using **joblib**

---

#### 🧠 Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **XGBoost**
* **Joblib**

---

#### 📊 Project Workflow

1. **Dataset Preparation**

   * Data loading and cleaning using `pandas`
   * Encoding categorical variables with `LabelEncoder`
   * Feature selection and transformation
   * Exploratory Data Analysis with `matplotlib` and `seaborn`

2. **Model Training**

   * Splitting dataset using `train_test_split`
   * Training with `XGBRegressor`
   * Evaluating model performance using `mean_absolute_error` and `r2_score`
   * Saving trained model using `joblib`

3. **Deployment**

   * Building a **Flask API** to serve predictions
   * Developing a **Streamlit dashboard** for user interaction

---

#### ⚙️ How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/HousePrediction_flask.git
cd HousePrediction_flask

# Install dependencies
pip install -r requirements.txt

# Run the Flask API
python app.py

# Run the Streamlit interface
streamlit run interface.py
```

---

