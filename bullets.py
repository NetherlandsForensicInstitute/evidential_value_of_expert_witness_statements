import lir

from utils import print_LR_per_category

h1 = {'ID': 1076,
      'Inconclusive-A': 127,
      'Inconclusive-B': 125,
      'Inconclusive-C': 36,
      'Elimination': 41,
      'Other': 24
      }
h1_tot = sum([int(val) for val in h1.values()])

h2 = {'ID': 20,
      'Inconclusive-A': 268,
      'Inconclusive-B': 848,
      'Inconclusive-C': 745,
      'Elimination': 961,
      'Other': 49
      }
h2_tot = sum([int(val) for val in h2.values()])

# check manual entering with total reported in paper
assert h2_tot + h1_tot == 4320

LR_map = {}
h1s = []
h2s = []
for keyword in h2.keys():
    LR_map[keyword] = h1[keyword] / h1_tot / (h2[keyword] / h2_tot)
    h1s += [LR_map[keyword]] * h1[keyword]
    h2s += [LR_map[keyword]] * h2[keyword]

print_LR_per_category(LR_map)
# ID: 108.84
# Inconclusive-A: 1/1.04
# Inconclusive-B: 1/3.35
# Inconclusive-C: 1/10.23
# Elimination: 1/11.59
# Other: 1/1.01
stats = lir.calculate_lr_statistics(h2s, h1s)
print(stats.cllr)
# 0.42
