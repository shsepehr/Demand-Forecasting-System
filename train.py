import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import os

# Load dataset
df = pd.read_csv("data/sales.csv")
df['sales'] = df['sales'].astype(float)

# Normalize
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df[['sales']])

# Dataset to sequences
X, y = [], []
window = 3  # previous 3 days predict next day
for i in range(len(scaled)-window):
    X.append(scaled[i:i+window])
    y.append(scaled[i+window])
X, y = np.array(X), np.array(y)

# Model
model = Sequential()
model.add(LSTM(32, activation='relu', input_shape=(window, 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=50, batch_size=4, verbose=1)

os.makedirs("model", exist_ok=True)
model.save("model/model.h5")

# Save scaler
import joblib
joblib.dump(scaler, "model/scaler.pkl")

print("🎉 Model trained and saved!")
