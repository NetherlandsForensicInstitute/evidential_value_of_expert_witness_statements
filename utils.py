import os

import numpy as np
import requests as requests
from pathlib import Path


def print_LR_per_category(lr_map):
    for key, LR in lr_map.items():
        if LR > 1:
            print(f'{key}: {LR:.2f}')
        else:
            print(f'{key}: 1/{1 / LR:.2f}')


def return_file_path_and_download_data_if_not_present(url):
    file_name = os.path.join('data', url.split('/')[-1])
    if not os.path.isfile(file_name):
        # if folder doesn’t exist create it
        Path("data").mkdir(parents=True, exist_ok=True)
        response = requests.get(url)
        open(file_name, "wb").write(response.content)
    return file_name


def get_list_of_conclusions(h1_totals, h2_totals):
    h1s = []
    h2s = []
    for keyword in set(h2_totals.keys()).union(set(h1_totals.keys())):
        h1s += [keyword] * h1_totals[keyword]
        h2s += [keyword] * h2_totals[keyword]
    return np.array(h1s), np.array(h2s)


def get_lr_map(h1s, h2s, keywords):
    return {kw: ((h1s == kw).sum() / len(h1s)) / ((h2s == kw).sum() / len(h2s)) for kw in keywords}
