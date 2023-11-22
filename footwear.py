import pandas as pd
import lir

from utils import print_LR_per_category

df = pd.read_excel('data/1-s2.0-S0379073822002481-mmc1.xlsx', sheet_name=1)

# terminology; mated vs non-mated
h1s = df[df['Mating'] == 'Mated']['Conclusion']
h2s = df[df['Mating'] == 'Nonmated']['Conclusion']

LR_map = {kw: (h1s == kw).sum() / (h2s == kw).sum() for kw in df['Conclusion'].unique()}

print_LR_per_category(LR_map)
# NotSuitable: 1/3.38
# Assn: 1/1.34
# Excl: 1/10.72
# ID: 75.55
# LimitedAssn: 1/1.92
# NonAssn: 1/8.36

stats = lir.calculate_lr_statistics(h2s.map(LR_map), h1s.map(LR_map))
print(stats.cllr)
# 0.68