# # import pandas as pd
# # import numpy as np
# # import joblib
# # from sklearn.ensemble import RandomForestRegressor
# # from sklearn.preprocessing import OneHotEncoder
# # from sklearn.compose import ColumnTransformer
# # from sklearn.pipeline import Pipeline

# # # Load datasets
# # walmart_df = pd.read_csv('pages/walmart_info.csv')
# # events_df = pd.read_csv('city_venue_concert.csv')

# # # Clean column names
# # for df in [walmart_df, events_df]:
# #     df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# # # Print for debugging
# # print("✅ Walmart columns:", walmart_df.columns)
# # print("✅ Event columns:", events_df.columns)

# # # Synthetic training data
# # training_data = []
# # for _, store in walmart_df.iterrows():
# #     store_population = store['population_within_5km']
# #     for _, event in events_df.iterrows():
# #         event_name = event['event_name']
# #         event_impact_score = event['event_impact_score']

# #         # Generate multiple synthetic scenarios
# #         for _ in range(5):
# #             attendees = np.random.randint(100, 5000)
# #             total_population = store_population + attendees

# #             # Simulate sales as function of population, impact
# #             noise = np.random.normal(0, 5000)
# #             sales = total_population * event_impact_score * np.random.uniform(15, 25) + noise

# #             training_data.append({
# #                 'population': total_population,
# #                 'event_name': event_name,
# #                 'event_impact_score': event_impact_score,
# #                 'sales': sales
# #             })

# # df_train = pd.DataFrame(training_data)
# # print(df_train.head())

# # # Features and target
# # X = df_train[['population', 'event_name', 'event_impact_score']]
# # y = df_train['sales']

# # # Build pipeline
# # preprocessor = ColumnTransformer(
# #     transformers=[
# #         ('event_name', OneHotEncoder(handle_unknown='ignore'), ['event_name'])
# #     ],
# #     remainder='passthrough'
# # )

# # pipeline = Pipeline([
# #     ('preprocessor', preprocessor),
# #     ('regressor', RandomForestRegressor(n_estimators=200, max_depth=20, random_state=42))
# # ])

# # pipeline.fit(X, y)
# # joblib.dump(pipeline, 'sales_model.pkl')
# # print("✅ Model trained and saved as sales_model.pkl")

# # import pandas as pd
# # import numpy as np
# # import joblib
# # from sklearn.ensemble import RandomForestRegressor
# # from sklearn.preprocessing import OneHotEncoder
# # from sklearn.compose import ColumnTransformer
# # from sklearn.pipeline import Pipeline

# # # Load datasets
# # walmart_df = pd.read_csv('pages/walmart_info.csv')
# # events_df = pd.read_csv('pages/city_venue_concert.csv')

# # # Clean column names
# # for df in [walmart_df, events_df]:
# #     df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# # # Print for debugging
# # print("✅ Walmart columns:", walmart_df.columns)
# # print("✅ Event columns:", events_df.columns)

# # # Ensure correct dtype
# # events_df['event_impact_score'] = pd.to_numeric(events_df['event_impact_score'], errors='coerce')

# # # Synthetic training data
# # training_data = []
# # for _, store in walmart_df.iterrows():
# #     store_population = store['population_within_5km']
# #     for _, event in events_df.iterrows():
# #         event_name = event['event_name']
# #         event_impact_score = event['event_impact_score']

# #         # Skip rows with missing score
# #         if pd.isna(event_impact_score):
# #             continue

# #         # Generate multiple synthetic scenarios
# #         for _ in range(5):
# #             attendees = np.random.randint(100, 5000)
# #             total_population = store_population + attendees

# #             # Simulate sales as function of population, impact
# #             noise = np.random.normal(0, 5000)
# #             sales = total_population * event_impact_score * np.random.uniform(15, 25) + noise

# #             training_data.append({
# #                 'population': total_population,
# #                 'event_name': event_name,
# #                 'event_impact_score': event_impact_score,
# #                 'sales': sales
# #             })

# # df_train = pd.DataFrame(training_data)
# # print("✅ Sample training data:")
# # print(df_train.head())

# # # Features and target
# # X = df_train[['population', 'event_name', 'event_impact_score']]
# # y = df_train['sales']

# # # Build pipeline
# # preprocessor = ColumnTransformer(
# #     transformers=[
# #         ('event_name', OneHotEncoder(handle_unknown='ignore'), ['event_name'])
# #     ],
# #     remainder='passthrough'
# # )

# # pipeline = Pipeline([
# #     ('preprocessor', preprocessor),
# #     ('regressor', RandomForestRegressor(n_estimators=200, max_depth=20, random_state=42))
# # ])

# # # Train
# # pipeline.fit(X, y)

# # # Save expected input column names for Streamlit
# # pipeline.input_features_custom = list(X.columns)


# # # Save model
# # joblib.dump(pipeline, 'sales_model.pkl')
# # print("✅ Model trained and saved as sales_model.pkl")
# # print("✅ Expected input columns:", list(pipeline.feature_names_in_))
# import pandas as pd
# import numpy as np
# import joblib
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline

# # Load datasets
# walmart_df = pd.read_csv('pages/walmart_info.csv')
# events_df = pd.read_csv('pages/city_venue_concert.csv')

# # Clean column names
# for df in [walmart_df, events_df]:
#     df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# # Ensure correct dtype
# events_df['event_impact_score'] = pd.to_numeric(events_df['event_impact_score'], errors='coerce')

# # Generate synthetic training data
# training_data = []
# for _, store in walmart_df.iterrows():
#     store_population = store['population_within_5km']
#     for _, event in events_df.iterrows():
#         event_name = event['event_name']
#         event_impact_score = event['event_impact_score']

#         if pd.isna(event_impact_score):
#             continue

#         for _ in range(5):
#             attendees = np.random.randint(100, 5000)
#             total_population = store_population + attendees
#             noise = np.random.normal(0, 5000)
#             sales = total_population * event_impact_score * np.random.uniform(15, 25) + noise

#             training_data.append({
#                 'population': total_population,
#                 'event_name': event_name,
#                 'event_impact_score': event_impact_score,
#                 'sales': sales
#             })

# df_train = pd.DataFrame(training_data)

# # Features and target
# X = df_train[['population', 'event_name', 'event_impact_score']]
# y = df_train['sales']

# # Define preprocessing pipeline
# preprocessor = ColumnTransformer(
#     transformers=[
#         ('event_name', OneHotEncoder(handle_unknown='ignore'), ['event_name'])
#     ],
#     remainder='passthrough'
# )

# pipeline = Pipeline([
#     ('preprocessor', preprocessor),
#     ('regressor', RandomForestRegressor(n_estimators=200, max_depth=20, random_state=42))
# ])

# # Fit pipeline
# pipeline.fit(X, y)

# # Save the pipeline
# joblib.dump(pipeline, 'sales2_model.pkl')

# print("✅ Model trained and saved as sales_model.pkl")
# print("✅ Expected input format: population, event_name, event_impact_score")

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import joblib

# Load data
walmart_df = pd.read_csv('pages/walmart_info.csv')
events_df = pd.read_csv('pages/city_venue_concert.csv')

# Clean
for df in [walmart_df, events_df]:
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
events_df['event_impact_score'] = pd.to_numeric(events_df['event_impact_score'], errors='coerce')

# Synthetic data
training_data = []
for _, store in walmart_df.iterrows():
    pop = store['population_within_5km']
    for _, event in events_df.iterrows():
        if pd.isna(event['event_impact_score']):
            continue
        for _ in range(5):
            attendees = np.random.randint(100, 5000)
            total_pop = pop + attendees
            noise = np.random.normal(0, 5000)
            sales = total_pop * event['event_impact_score'] * np.random.uniform(15, 25) + noise
            training_data.append({
                'population': total_pop,
                'event_name': event['event_name'],
                'event_impact_score': event['event_impact_score'],
                'sales': sales
            })

df_train = pd.DataFrame(training_data)

# Features / target
X = df_train[['population', 'event_name', 'event_impact_score']]
y = df_train['sales']

# Pipeline
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

# Fit and save
pipeline.fit(X, y)
joblib.dump(pipeline, 'sales2_model.pkl')
print("✅ Model trained and saved correctly.")
