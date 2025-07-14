

combined = pd.concat([df1, df2], axis=0)
combined = pd.concat([df1, df2], axis=1)

merged = pd.merge(df1, df2, on="common_column")
merged = pd.merge(df1, df2, how="left", on="common_column")
merged = pd.merge(df1, df2, how="inner", on="common_column")


joined = df1.join(df2, how="inner")