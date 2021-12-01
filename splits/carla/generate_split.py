from os import listdir
from os.path import isfile, join, splitext
import random


SPLIT_TRAIN_FILE = 'train_files.txt'
SPLIT_VAL_FILE = 'val_files.txt'
CARLA_RGB_PATH = '../../carla_data/_out_rgb_{}'
CARLA_DEPTH_PATH = '../../carla_data/_out_depth_{}'
RUNS = [57]
TRAIN_FRAC = 0.9


with open(SPLIT_TRAIN_FILE, 'w') as train_f, open(SPLIT_VAL_FILE, 'w') as val_f:
    trains = []
    vals = []
    for run in RUNS:
        rgb_path = CARLA_RGB_PATH.format(run)
        files = [splitext(f)[0] for f in listdir(rgb_path) if isfile(join(rgb_path, f))]
        files = sorted(files, key=lambda x: int(x))
        files = files[1:-1]
        split_point = int(len(files) * TRAIN_FRAC)
        random.shuffle(files)
        for f in files[:split_point]:
            # trains.append('{} {} {}\n'.format(run, f, 'l'))
            # trains.append('{} {} {}\n'.format(run, f, 'r'))
            trains.append('{} {}\n'.format(run, f))
        for f in files[split_point:]:
            # vals.append('{} {} {}\n'.format(run, f, 'l'))
            # vals.append('{} {} {}\n'.format(run, f, 'r'))
            vals.append('{} {}\n'.format(run, f))
    random.shuffle(trains)
    random.shuffle(vals)
    train_f.write(''.join(trains))
    val_f.write(''.join(vals))
