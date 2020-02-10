import sys

import pandas as pd

from utils import clean_data

# df = pd.read_csv('../devtest/sample_input.csv')
# df = pd.read_csv('./challenge1.csv')
df = pd.read_csv(sys.argv[1])
corp_bonds, govt_bonds = clean_data(df)

print("bond,benchmark,spread_to_benchmark")
for idx, row in corp_bonds.iterrows():
    benchmark = df.iloc[(govt_bonds['term'] - row['term']).abs().idxmin()]
    print("%s,%s,%1.2f%%" % (row['bond'], benchmark['bond'], row['yield'] - benchmark['yield']))
