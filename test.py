import pandas as pd

from main import preprocess_wine_df
df = pd.read_excel('wine.xlsx')

print(preprocess_wine_df(df))