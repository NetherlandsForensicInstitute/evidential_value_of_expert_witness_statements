import os.path

import lir
import pandas as pd

from utils import print_LR_per_category, return_file_path_and_download_data_if_not_present, get_lr_map, \
    get_list_of_conclusions

# download the data if not present
url = "https://ars.els-cdn.com/content/image/1-s2.0-S0379073821001766-mmc4.xlsx"
file_name = return_file_path_and_download_data_if_not_present(url)

df = pd.read_excel(file_name, sheet_name='Classes', dtype={'KnownCause': str})
# pandas sometimes has issues reading the column names
df.columns = ['SampleID', 'SamplePnum', 'Prompt', 'KnownCause', 'MostCons', 'Responses', 'N(D)', 'N(I)', 'N(E)']

h1s = df[df['KnownCause'].str.lower() == 'true']
h2s = df[df['KnownCause'].str.lower() == 'false']

# in this study the participants were given images of bloodstain patterns, and a possible classification.
# They had to respond whether they agreed with that classification (definitive), disagreed (exclusion) or
# could not reach a conclusion (included).
# the xlsx gives the total number of judgements made that were:
# N(D) definitive, N(E) exclusion and N(I) included
num_columns = ['N(D)', 'N(I)', 'N(E)']

#get these into the format of the other studies
h1_conclusions, h2_conclusions = get_list_of_conclusions({kw: h1s[kw].sum() for kw in num_columns},
                                                         {kw: h2s[kw].sum() for kw in num_columns})

LR_map = get_lr_map(h1_conclusions, h2_conclusions, num_columns)

print_LR_per_category(LR_map)
# N(D): 6.19
# N(I): 1.02
# N(E): 1/3.96

stats = lir.calculate_lr_statistics([LR_map[c] for c in h2_conclusions], [LR_map[c] for c in h1_conclusions])
print(stats.cllr)  # 0.77





# NB We can repeat the analysis for only those assessments that were deemed 'most consequential'. The numbers change
# little overal:
df = df[df['MostCons']=='MC']

# (from Hicklin et al):
# In order to limit the effects of prompts that could be seen as minor or semantic,
# the BPA analysts on the study team also evaluated each prompt to determine
# whether an error on that prompt would be highly consequential in an actual case.
# These are labeled “most consequential", and 22.5% of the prompts were labeled as such (see SI Appendix 1.6).

h1s = df[df['KnownCause'].str.lower() == 'true']
h2s = df[df['KnownCause'].str.lower() == 'false']

h1_conclusions, h2_conclusions = get_list_of_conclusions({kw: h1s[kw].sum() for kw in num_columns},
                                                         {kw: h2s[kw].sum() for kw in num_columns})

LR_map = get_lr_map(h1_conclusions, h2_conclusions, num_columns)

print_LR_per_category(LR_map)
# N(D): 7.16
# N(I): 1/1.12
# N(E): 1/5.8

stats = lir.calculate_lr_statistics([LR_map[c] for c in h2_conclusions], [LR_map[c] for c in h1_conclusions])
print(stats.cllr)
# 0.71
