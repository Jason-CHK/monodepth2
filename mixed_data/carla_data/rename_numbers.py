from os import listdir
import os
from os.path import isfile, join, splitext
import random


CARLA_RGB_PATH = '_out_rgb_{}'
CARLA_DEPTH_PATH = '_out_depth_{}'
RUNS = [57,58,61,62,63]


for run in RUNS:
    rgb_path = CARLA_RGB_PATH.format(run)
    files = [splitext(f)[0] for f in listdir(rgb_path) if isfile(join(rgb_path, f))]
    files = sorted(files)
    count = 0
    for f in files:
        old_name = CARLA_RGB_PATH.format(run) + "/" + f + ".jpg"
        new_name = CARLA_RGB_PATH.format(run) + "/" + str(count) + ".jpg"
        os.rename(old_name, new_name)
        old_name = CARLA_DEPTH_PATH.format(run) + "/" + f + ".jpg"
        new_name = CARLA_DEPTH_PATH.format(run) + "/" + str(count) + ".jpg"
        os.rename(old_name, new_name)
        count += 1
