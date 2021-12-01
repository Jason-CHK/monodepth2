import os
from .mono_dataset import MonoDataset, pil_loader
import PIL.Image as pil
import numpy as np


CARLA_RGB_PATH = '_out_rgb_{}/{}.jpg'
CARLA_DEPTH_PATH = '_out_depth_{}/{}.jpg'


class CarlaDataset(MonoDataset):
    def __init__(self, data_path, filenames, height, width, frame_idxs, num_scales, is_train=False, img_ext='.jpg'):
        super(CarlaDataset, self).__init__(data_path, filenames, height, width, frame_idxs, num_scales, is_train=is_train, img_ext=img_ext)

        # NOTE: Make sure your intrinsics matrix is *normalized* by the original image size.
        # To normalize you need to scale the first row by 1 / image_width and the second row
        # by 1 / image_height. Monodepth2 assumes a principal point to be exactly centered.
        # If your principal point is far from the center you might need to disable the horizontal
        # flip augmentation.
        self.K = np.array([[0.58, 0, 0.5, 0],
                           [0, 1.92, 0.5, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]], dtype=np.float32)
        self.full_res_shape = (1242, 375)

    def get_color(self, folder, frame_index, side, do_flip):
        image_path = self.data_path + "/" + CARLA_RGB_PATH.format(folder, frame_index)
        color = pil_loader(image_path)
        if do_flip:
            color = color.transpose(pil.FLIP_LEFT_RIGHT) # flip the left to right, and right to left by 90 degrees
        return color

    def check_depth(self):
        return True

    def get_depth(self, folder, frame_index, side, do_flip):
        image_path = os.path.join(
            self.data_path, CARLA_DEPTH_PATH.format(folder, frame_index))
        im = pil_loader(image_path)
        rgb_im = im.convert('RGB')

        depth_map = np.empty([375, 1242])
        for x in range(im.width):
            for y in range(im.height):
                r, g, b = rgb_im.getpixel((x, y))
                depth_map[y][x] = (r + g*256 + b*256*256) / ( 256*256*256 - 1 ) * 10
        return depth_map
