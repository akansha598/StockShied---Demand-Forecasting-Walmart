import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load datasets
walmart_df = pd.read_csv('pages/walmart_info.csv')
events_df = pd.read_csv('city_venue_concert.csv')

# Clean column names
for df in [walmart_df, events_df]:
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Print for debugging
print("✅ Walmart columns:", walmart_df.columns)
print("✅ Event columns:", events_df.columns)

# Synthetic training data
training_data = []
for _, store in walmart_df.iterrows():
    store_population = store['population_within_5km']
    for _, event in events_df.iterrows():
        event_name = event['event_name']
        event_impact_score = event['event_impact_score']

        # Generate multiple synthetic scenarios
        for _ in range(5):
            attendees = np.random.randint(100, 5000)
            total_population = store_population + attendees

            # Simulate sales as function of population, impact
            noise = np.random.normal(0, 5000)
            sales = total_population * event_impact_score * np.random.uniform(15, 25) + noise

            training_data.append({
                'population': total_population,
                'event_name': event_name,
                'event_impact_score': event_impact_score,
                'sales': sales
            })

df_train = pd.DataFrame(training_data)
print(df_train.head())

# Features and target
X = df_train[['population', 'event_name', 'event_impact_score']]
y = df_train['sales']

# Build pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('event_name', OneHotEncoder(handle_unknown='ignore'), ['event_name'])
    ],
    remainder='passthrough'
)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=200, max_depth=20, random_state=42))
])

pipeline.fit(X, y)
joblib.dump(pipeline, 'sales_model.pkl')
print("✅ Model trained and saved as sales_model.pkl")
