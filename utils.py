def print_LR_per_category(lr_map):
    for key, LR in lr_map.items():
        if LR > 1:
            print(f'{key}: {LR:.2f}')
        else:
            print(f'{key}: 1/{1 / LR:.2f}')