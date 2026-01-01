from tensorflow.keras.models import load_model
import joblib
import numpy as np

model = load_model("model/model.h5")
scaler = joblib.load("model/scaler.pkl")

def forecast(n_days: int, last_values: list):
    data = scaler.transform(np.array(last_values).reshape(-1, 1))
    window = len(last_values)
    preds = []

    for _ in range(n_days):
        input_data = np.array(data[-window:]).reshape(1, window, 1)
        pred = model.predict(input_data, verbose=0)
        preds.append(pred[0][0])
        data = np.append(data, pred)[-window:]

    preds = scaler.inverse_transform(np.array(preds).reshape(-1, 1))
    return preds.flatten().tolist()
