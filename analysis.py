import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)

df = pd.read_json('nolanDB.json')
print(df)