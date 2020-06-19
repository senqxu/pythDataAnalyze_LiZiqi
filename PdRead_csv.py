import numpy as np
import pandas as pd

excel_file = r'C:\A-SMS-work\2020-BI-Work\Tutorial-Next-Steps-Scripting\Tutorials-source\Transactions.csv'
df1 = pd.DataFrame(pd.read_csv(excel_file))
print(df1)
df1[['Product','List Price']]
df1[(df1['Product']=='A')&(df1['List Price']>1000)]