import lir

from utils import print_LR_per_category

h1 = {'ID': 1056,
      'Inconclusive-A': 177,
      'Inconclusive-B': 140,
      'Inconclusive-C': 22,
      'Elimination': 25,
      'Other': 25
      }
h1_tot = sum([int(val) for val in h1.values()])

h2 = {'ID': 26,
      'Inconclusive-A': 177,
      'Inconclusive-B': 637,
      'Inconclusive-C': 620,
      'Elimination': 1375,
      'Other': 40
      }
h2_tot = sum([int(val) for val in h2.values()])
# check manual entering with total
assert h2_tot + h1_tot == 4320

LR_map = {}
h1s = []
h2s = []
for keyword in h2.keys():
    LR_map[keyword] = h1[keyword] / h1_tot / (h2[keyword] / h2_tot)
    h1s += [LR_map[keyword]] * h1[keyword]
    h2s += [LR_map[keyword]] * h2[keyword]

print_LR_per_category(LR_map)
# ID: 80.81
# Inconclusive-A: 1.99
# Inconclusive-B: 1/2.29
# Inconclusive-C: 1/14.16
# Elimination: 1/27.64
# Other: 1.24
stats = lir.calculate_lr_statistics(h2s, h1s)
print(stats.cllr)
# 0.37
