import lir

from utils import print_LR_per_category, get_list_of_conclusions, get_lr_map

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

# reform the totals to list of conclusions so we can handle them like other studies
h1_conclusions, h2_conclusions = get_list_of_conclusions(h1, h2)

LR_map = get_lr_map(h1_conclusions, h2_conclusions, set(h1))
print_LR_per_category(LR_map)
# ID: 108.84
# Inconclusive-A: 1/1.04
# Inconclusive-B: 1/3.35
# Inconclusive-C: 1/10.23
# Elimination: 1/11.59
# Other: 1/1.01

stats = lir.calculate_lr_statistics([LR_map[c] for c in h2_conclusions], [LR_map[c] for c in h1_conclusions])
print(stats.cllr)
# 0.42
