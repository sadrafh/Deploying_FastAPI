import pandas as pd
import numpy as np

df = pd.read_csv("./data/census.csv",delimiter=',', encoding="utf-8-sig")

categorical_features_indices = np.where(df.dtypes == object)[0]
cat_features = df.columns[categorical_features_indices].tolist()


df.columns = [c.strip() for c in df.columns]

#for c in cat_features:
#    df[c] = df[c].str.strip()

df.to_csv("./data/census.csv", index=False)