import pandas as pd
import numpy as np


df = pd.read_csv('../data/churn_data.csv')


# Handle missing values
df.fillna(method='ffill', inplace=True)


# Convert categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].apply(lambda x: x.astype('category'))


# Save cleaned data
df.to_csv('../data/cleaned_churn.csv', index=False)