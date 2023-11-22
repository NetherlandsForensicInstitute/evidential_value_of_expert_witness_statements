import lir
import numpy as np
import pandas as pd

from utils import print_LR_per_category

df = pd.read_excel('data/pnas.2119944119.sd02.xlsx')

# terminology; mated vs non-mated
h1s = df[df['Mating'] == 'M']['Conclusion']
h2s = df[df['Mating'] == 'N']['Conclusion']

LR_map = {kw: (h1s == kw).sum() / (h2s == kw).sum() for kw in df['Conclusion'].unique()}

print_LR_per_category(LR_map)
# ProbWritten: 5.47
# NotWritten: 1/35.00
# ProbNot: 1/28.09
# Written: 13.21
# NoConc: 1/2.28

h1s = np.array(h1s.map(LR_map))
h2s = np.array(h2s.map(LR_map))
stats = lir.calculate_lr_statistics(h2s, h1s)
print(stats.cllr)
# 0.4
