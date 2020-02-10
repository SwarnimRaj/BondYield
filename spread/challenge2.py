import sys

import pandas as pd
from scipy.interpolate import interp1d

from utils import clean_data

# df = pd.read_csv('../devtest/sample_input.csv')
# df = pd.read_csv('./challenge2.csv')
df = pd.read_csv(sys.argv[1])
corp_bonds, govt_bonds = clean_data(df)
f1 = interp1d(govt_bonds['term'], govt_bonds['yield'], kind='linear')

print("bond,spread_to_curve")
for idx, row in corp_bonds.iterrows():
    print("%s,%1.2f%%" % (row['bond'], row['yield'] - f1(row['term'])))
