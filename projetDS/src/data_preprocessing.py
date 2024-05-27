import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from feature_engineering import feature_engineering

def data_preprocessing(name_file):
    df = pd.read_csv('../data/raw/' + name_file + '.csv')
    df['Age'] = df['Rings'] + 1.5
    features = df.drop(columns=['Sex', 'Rings', 'Age'])
    scaler = MinMaxScaler(feature_range=(0, 1))
    features_scaled = scaler.fit_transform(features)
    df_scaled = pd.DataFrame(features_scaled, columns=features.columns)
    df_scaled['Age'] = df['Age']
    df_scaled.to_csv('../data/processed/processed_' + name_file + '.csv', index=False)
    df = pd.read_csv('../data/processed/processed_' + name_file + '.csv')
    df[['Sex_F', 'Sex_I', 'Sex_M']] = pd.get_dummies(pd.read_csv('../data/raw/' + name_file + '.csv')['Sex'])
    df[['Sex_F', 'Sex_I', 'Sex_M']] = df[['Sex_F', 'Sex_I', 'Sex_M']].astype(int)
    df.to_csv('../data/processed/processed_' + name_file + '_with_sex.csv', index=False)


def run():
    if (feature_engineering()):
        name_file_1 = 'abalone_data'
        name_file_2 = 'abalone_data_with_feature_engineering'
    else:
        print("Feature engineering failed.")
    data_preprocessing(name_file_1)
    data_preprocessing(name_file_2)
    print("Data preprocessing completed.")

if __name__ == '__main__':
    run()