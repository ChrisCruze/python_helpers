import pandas as pd

def pandas_date_fix(df,field):
  df[field] = pd.to_datetime(df[field], errors='coerce').fillna('2021-12-31 00:00:00')
  return df


def pandas_count_values(df,field):
  df[field].value_counts()
  
def pandas_count_values_two(df,field):
  df[field].value_counts()