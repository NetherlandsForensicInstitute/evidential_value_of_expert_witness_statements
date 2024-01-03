import pandas as pd
import lir

from utils import print_LR_per_category, return_file_path_and_download_data_if_not_present, get_lr_map

# download the data if not present
url = "https://ars.els-cdn.com/content/image/1-s2.0-S0379073822002481-mmc1.xlsx"
file_name = return_file_path_and_download_data_if_not_present(url)

df = pd.read_excel(file_name, sheet_name=1)

# terminology; mated vs non-mated
h1_conclusions = df[df['Mating'] == 'Mated']['Conclusion']
h2_conclusions = df[df['Mating'] == 'Nonmated']['Conclusion']

LR_map = get_lr_map(h1_conclusions, h2_conclusions, df['Conclusion'].unique())

print_LR_per_category(LR_map)
# NotSuitable: 1/2.26
# Assn: 1.12
# Excl: 1/7.15
# ID: 113.25
# LimitedAssn: 1/1.28
# NonAssn: 1/5.58
# HighAssn: 12.76
# Inc: 1/1.55

stats = lir.calculate_lr_statistics(h2_conclusions.map(LR_map), h1_conclusions.map(LR_map))
print(stats.cllr)
# 0.66
