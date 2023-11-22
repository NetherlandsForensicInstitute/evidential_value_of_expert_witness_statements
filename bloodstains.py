import lir
import pandas as pd

from utils import print_LR_per_category

df = pd.read_excel('data/1-s2.0-S0379073821001766-mmc4.xlsx', sheet_name='Classes', dtype={'KnownCause': str})
# pandas sometimes has issues reading the column names
df.columns = ['SampleID', 'SamplePnum', 'Prompt', 'KnownCause', 'MostCons', 'Responses', 'N(D)', 'N(I)', 'N(E)']

h1s = df[df['KnownCause'].str.lower() == 'true']
h2s = df[df['KnownCause'].str.lower() == 'false']

num_columns = ['N(D)', 'N(I)', 'N(E)']

tot_h2s = sum(h2s[kw].sum() for kw in num_columns)
tot_h1s = sum(h1s[kw].sum() for kw in num_columns)

LR_map = {kw: (h1s[kw].sum() / tot_h1s) / (h2s[kw].sum() / tot_h2s) for kw in num_columns}

print_LR_per_category(LR_map)
# N(D): 6.19
# N(I): 1.02
# N(E): 1/3.96


h1_LRs = []
h2_LRs = []
for kw in num_columns:
    h1_LRs += [LR_map[kw]] * h1s[kw].sum()
    h2_LRs += [LR_map[kw]] * h2s[kw].sum()

stats = lir.calculate_lr_statistics(h2_LRs, h1_LRs)
print(stats.cllr)
# 0.77
