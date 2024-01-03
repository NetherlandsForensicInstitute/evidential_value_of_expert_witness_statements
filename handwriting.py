import lir
import numpy as np
import pandas as pd

from utils import print_LR_per_category, return_file_path_and_download_data_if_not_present, get_lr_map

# download the data if not present
url = "https://www.pnas.org/doi/suppl/10.1073/pnas.2119944119/suppl_file/pnas.2119944119.sd02.xlsx"
file_name = return_file_path_and_download_data_if_not_present(url)

df = pd.read_excel(file_name)

# terminology; mated vs non-mated
h1_conclusions = df[df['Mating'] == 'M']['Conclusion']
h2_conclusions = df[df['Mating'] == 'N']['Conclusion']

LR_map = get_lr_map(h1_conclusions, h2_conclusions, df['Conclusion'].unique())

print_LR_per_category(LR_map)
# ProbWritten: 6.93
# NotWritten: 1/27.65
# ProbNot: 1/22.19
# Written: 16.73
# NoConc: 1/1.80

h1_conclusions = np.array(h1_conclusions.map(LR_map))
h2_conclusions = np.array(h2_conclusions.map(LR_map))
stats = lir.calculate_lr_statistics(h2_conclusions, h1_conclusions)
print(stats.cllr)
# 0.4
