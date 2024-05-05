import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv('../data/raw/abalone_data.csv')
df['Age'] = df['Rings'] + 1.5
features = df.drop(columns=['Sex', 'Rings', 'Age'])

## scaler = StandardScaler() # Standardize features by removing the mean and scaling to unit variance but will bring negative values
scaler = MinMaxScaler(feature_range=(0, 1))
features_scaled = scaler.fit_transform(features)

df_scaled = pd.DataFrame(features_scaled, columns=features.columns)
df_scaled['Age'] = df['Age']

df_scaled.to_csv('../data/processed/processed_abalone_data.csv', index=False)

df = pd.read_csv('../data/processed/processed_abalone_data.csv')
df[['Sex_F', 'Sex_I', 'Sex_M']] = pd.get_dummies(pd.read_csv('../data/raw/abalone_data.csv')['Sex'])
df[['Sex_F', 'Sex_I', 'Sex_M']] = df[['Sex_F', 'Sex_I', 'Sex_M']].astype(int)
df.to_csv('../data/processed/processed_abalone_data_with_sex.csv', index=False)