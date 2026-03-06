import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Score": [85, 90, 88],
})

combined = pd.concat([df1, df2], axis=0)
combined = pd.concat([df1, df2], axis=1)

merged = pd.merge(df1, df2, on="ID")
merged = pd.merge(df1, df2, how="left", on="ID")
merged = pd.merge(df1, df2, how="inner", on="ID")


joined = df1.join(df2.set_index("ID"), on="ID", how="inner")
