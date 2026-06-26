import pandas as pd
from sklearn.ensemble import IsolationForest

# Sample telemetry
data = {
    "CPU": [10, 15, 20, 12, 14, 90],
    "Memory": [30, 35, 40, 32, 38, 95]
}

df = pd.DataFrame(data)

model = IsolationForest(contamination=0.1)

model.fit(df)

df["Anomaly"] = model.predict(df)

print(df)