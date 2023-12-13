import lir
import numpy as np
import pandas as pd

from utils import print_LR_per_category, return_file_path_and_download_data_if_not_present

# download the data if not present
url = "https://www.pnas.org/doi/suppl/10.1073/pnas.2119944119/suppl_file/pnas.2119944119.sd02.xlsx"
file_name = return_file_path_and_download_data_if_not_present(url)

df = pd.read_excel(file_name)

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
print(stats.cllr)  # 0.4
