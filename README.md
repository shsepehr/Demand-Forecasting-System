# 📈 Demand Forecasting System

This project is a **Demand Forecasting System** built using Python and Machine Learning to predict future product demand from historical sales data.  
It uses a neural network model (LSTM/Dense) for time-series forecasting.

---

## 🚀 Features
- Load and preprocess historical sales data
- Train a forecasting model with TensorFlow/Keras
- Evaluate model accuracy
- Predict & export future demand
- Command-line inference via `predict.py`

---

## 🛠️ Tech Stack
| Component | Technology |
|----------|-------------|
| Language | Python 3.11 |
| Model Framework | TensorFlow 2.11+ |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib |
| ML Type | Time Series Forecasting |

> ⚠️ **Important Compatibility Note**  
> - TensorFlow **does not support Python 3.11** in older versions.  
> - The recommended configuration is:  
>   - **Python 3.10** or **Install TensorFlow 2.11 CPU version for Windows**

### ✅ Recommended Setup (Windows)
If using **Python 3.10**:
pip install tensorflow==2.11


If stuck on **Python 3.11**, install the CPU build which is compatible:
pip install tensorflow==2.11.0 --index-url https://pypi.org/simple


---

## 📊 Example: Training the Model

python train.py


After completion, a file will be created at:

model/model.h5

---

## 🤖 Running Prediction

python predict.py

You can also provide custom input (example):

python predict.py --days 30


---

## 📋 Sample Dataset Format (`sales.csv`)
| date       | sales |
|------------|--------|
| 2023-01-01 | 124    |
| 2023-01-02 | 156    |
| 2023-01-03 | 131    |
| ...        | ...    |

---


Install all dependencies:
pip install -r requirements.txt


---

## 🧠 Model Overview
The neural network learns patterns from past sales to predict future values.

- Input: Historical daily/weekly/monthly sales
- Output: Demand forecast for next N days
- Architecture: LSTM or Dense stack (based on dataset)

---

## 📜 License
This project is open-source and free to use for educational, personal, or commercial purposes.

---

## ⭐ Contribute
Feel free to:
- Open issues
- Submit PRs
- Suggest improvements

---




