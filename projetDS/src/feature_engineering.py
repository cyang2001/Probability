import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def feature_engineering():
    df = pd.read_csv('../data/raw/abalone_data.csv')
    df_num = df[df.columns[df.dtypes != 'object']]
    Q1 = df_num.quantile(0.25) ## 计算四分位数和IQR
    Q3 = df_num.quantile(0.75)
    IQR = Q3 - Q1
    df_num = df_num[~((df_num < (Q1 - 1.5 * IQR)) | (df_num > (Q3 + 1.5 * IQR))).any(axis=1)]
    df_num = df_num.sort_index()
    df_num['Sex'] = df['Sex']
    df_num.to_csv('../data/raw/abalone_data_with_feature_engineering.csv', index=False)
    print("Feature engineering completed.")
    return True

