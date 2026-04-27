# 💧 Water Quality Predictor

A Machine Learning-based web application that predicts whether water is **safe or unsafe** using physicochemical parameters. The project uses multiple ML models and deploys the best-performing model via a Streamlit web interface.

---

## 🚀 Live Demo

👉 https://water-quality-predictor-zr35yvd3cfveqpyc8trmix.streamlit.app

---

## 📌 Features

* Predicts water potability (Safe / Unsafe)
* Uses Random Forest model (~96% accuracy)
* Compared multiple ML models to select best performer
* Real-time prediction through web interface
* Clean and interactive UI using Streamlit

---

## 🧠 Machine Learning Models Used

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Decision Tree
* Random Forest (Best Model)

---

## 📊 Tech Stack

* **Python**
* **Pandas, NumPy** (Data Processing)
* **Scikit-learn** (Machine Learning)
* **Matplotlib, Seaborn** (Visualization)
* **Streamlit** (Web App)

---

## 🗂️ Project Structure

```
Water-quality-predictor/
│
├── app/
│   └── app.py
│
├── data/
│   └── waterQualityPrediction.csv
│
├── model/
│   ├── train_model.py
│   └── rf_model.pkl
│
├── utils/
│   ├── __init__.py
│   └── preprocess.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/Water-quality-predictor.git
cd Water-quality-predictor
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the app

```
streamlit run app/app.py
```

---

## 📈 Model Performance

| Model               | Accuracy        |
| ------------------- | --------------- |
| Logistic Regression | ~90%            |
| KNN                 | ~86%            |
| SVM                 | ~87%            |
| Decision Tree       | ~95%            |
| Random Forest       | **~96% (Best)** |

---

## 🧩 How It Works

1. User inputs water parameters
2. Data is processed and fed into ML model
3. Model predicts whether water is safe or unsafe
4. Result is displayed instantly with confidence score

---

## 🎯 Future Improvements

* Add data visualization dashboard
* Store prediction history
* Convert to REST API + React frontend
* Deploy on scalable cloud infrastructure

---

## 👨‍💻 Author

**Nikhil Anand**
B.Tech Mathematics & Computing, DTU

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
