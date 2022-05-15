## Simple method for short data

df2 = df.T.drop_duplicates().T

# Use groupby() to drop duplicate columns
df2 = df.T.groupby(level=0).first().T

# Remove duplicate columns pandas DataFrame
df2 = df.loc[:,~df.columns.duplicated()]

# Remove repeted columns in a DataFrame
df2 = df.loc[:,~df.T.duplicated(keep='first')]

# keep last duplicate columns
df2 = df.loc[:,~df.T.duplicated(keep='last')]

# Use DataFrame.columns.duplicated() to drop duplicate columns
duplicate_cols = df.columns[df.columns.duplicated()]
df.drop(columns=duplicate_cols, inplace=True)
