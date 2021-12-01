import random

SPLIT_TRAIN_FILE = 'train_files.txt'
SPLIT_VAL_FILE = 'val_files.txt'

lines = list(set(open(SPLIT_TRAIN_FILE).readlines()))
random.shuffle(lines)
open(SPLIT_TRAIN_FILE, 'w').writelines(lines)

lines = list(set(open(SPLIT_VAL_FILE).readlines()))
random.shuffle(lines)
open(SPLIT_VAL_FILE, 'w').writelines(lines)
