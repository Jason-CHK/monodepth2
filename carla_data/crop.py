from os import listdir
import os
from os.path import isfile, join, splitext
import random
from PIL import Image


CARLA_RGB_PATH = '_out_rgb_{}'
CARLA_DEPTH_PATH = '_out_depth_{}'
RUNS = [57,58,61,62,63]


for dir_path_template in [CARLA_RGB_PATH, CARLA_DEPTH_PATH]:
    for run in RUNS:
        dir_path = dir_path_template.format(run)
        files = [splitext(f)[0] for f in listdir(dir_path) if isfile(join(dir_path, f))]
        files = sorted(files)
        for f in files:
            path = dir_path + "/" + f + ".jpg"
            im = Image.open(path)

            left = 28
            top = 175
            right = 1252
            bottom = 545
            
            im1 = im.crop((left, top, right, bottom))
            im1.save(path)
