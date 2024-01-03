# the following is manually copied from table S5 in the appendix (in pdf form)

# 'Mates' column
import lir
import numpy as np

from utils import print_LR_per_category, get_list_of_conclusions, get_lr_map

h1 = {'Exclusion': 161+450, 'Inconclusive': 2019+1856, 'Individualisation': 40+3663 }
# check manual entering with total
h1_tot = 8189
assert h1_tot == sum([int(val) for val in h1.values()])

# 'Nonmates' column
h2 = {'Exclusion': 325+3622, 'Inconclusive': 577+455, 'Individualisation': 0+6 }
# check manual entering with total
h2_tot = 4985
assert h2_tot == sum([int(val) for val in h2.values()])


# reform the totals to list of conclusions so we can handle them like other studies
h1_conclusions, h2_conclusions = get_list_of_conclusions(h1, h2)


LR_map = get_lr_map(h1_conclusions, h2_conclusions, set(h1))
print_LR_per_category(LR_map)
# Exclusion: 1/10.61
# Inconclusive: 2.29
# Individualisation: 375.70

stats = lir.calculate_lr_statistics([LR_map[c] for c in h2_conclusions], [LR_map[c] for c in h1_conclusions])
print(stats.cllr)
# 0.49