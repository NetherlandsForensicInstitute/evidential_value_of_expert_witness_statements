import os

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