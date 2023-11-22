# the following is manually copied from table S5 in the appendix (in pdf form)

# 'Mates' column
import lir
import numpy as np

from utils import print_LR_per_category

h1 = {'Exclusion': 161+450, 'Inconclusive': 2019+1856, 'Individualisation': 40+3663 }
# check manual entering with total
h1_tot = 8189
assert h1_tot == sum([int(val) for val in h1.values()])

# 'Nonmates' column
h2 = {'Exclusion': 325+3622, 'Inconclusive': 577+455, 'Individualisation': 0+6 }
# check manual entering with total
h2_tot = 4985
assert h2_tot == sum([int(val) for val in h2.values()])


LR_map = {}
h1s=[]
h2s=[]
for keyword in h2.keys():
    LR_map[keyword] = h1[keyword]/h1_tot / (h2[keyword]/h2_tot)
    h1s += [LR_map[keyword]] * h1[keyword]
    h2s += [LR_map[keyword]] * h2[keyword]
print_LR_per_category(LR_map)
# Exclusion: 1/10.61
# Inconclusive: 2.29
# Individualisation: 375.70
stats = lir.calculate_lr_statistics(h2s, h1s)
print(stats.cllr)
# 0.49