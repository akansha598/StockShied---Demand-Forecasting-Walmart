import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

# ----------------------------------------------------
# Load datasets
walmart_df = pd.read_csv('pages/walmart_info.csv')
events_df = pd.read_csv('pages/city_venue_concert.csv')

# Clean columns
for df in [walmart_df, events_df]:
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Ensure correct dtype
events_df['event_impact_score'] = pd.to_numeric(events_df['event_impact_score'], errors='coerce')
events_df = events_df.dropna(subset=['event_impact_score'])

# ----------------------------------------------------
# Label encoding for event names
all_event_names = events_df['event_name'].str.strip().unique()
event_label_encoder = LabelEncoder()
event_label_encoder.fit(all_event_names)

# ----------------------------------------------------
# Prepare training data row by row
sgd = SGDRegressor(max_iter=1000, tol=1e-3)
scaler = StandardScaler()

X_batch = []
y_batch = []

for store_idx, store in walmart_df.iterrows():
    store_population = store['population_within_5km']
    for event_idx, event in events_df.iterrows():
        event_name = str(event['event_name']).strip()
        event_impact_score = event['event_impact_score']

        if pd.isna(event_impact_score):
            continue

        event_label = event_label_encoder.transform([event_name])[0]

        for _ in range(5):
            attendees = np.random.randint(100, 5000)
            total_population = store_population + attendees
            noise = np.random.normal(0, 5000)
            sales = total_population * event_impact_score * np.random.uniform(15, 25) + noise

            X_batch.append([total_population, event_label, event_impact_score])
            y_batch.append(sales)

# ----------------------------------------------------
# Convert to DataFrame
X_batch = np.array(X_batch)
y_batch = np.array(y_batch)

# Scale inputs
X_scaled = scaler.fit_transform(X_batch)

# Train SGDRegressor on full batch (but you could also partial_fit in loop)
sgd.fit(X_scaled, y_batch)

# ----------------------------------------------------
# Save everything needed for prediction
model_bundle = {
    'regressor': sgd,
    'scaler': scaler,
    'label_encoder': event_label_encoder
}
from sklearn.metrics import r2_score, mean_squared_error

y_pred = sgd.predict(X_scaled)

r2 = r2_score(y_batch, y_pred)

mse = mean_squared_error(y_batch, y_pred)

print("R² Score:", r2)
print("MSE:", mse)


joblib.dump(model_bundle, 'sales2_model.pkl')
print("✅ Model trained and saved as sales2_model.pkl")

