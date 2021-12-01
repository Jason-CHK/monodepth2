from .mono_dataset import MonoDataset
from .carla_dataset import CarlaDataset
from .kitti_dataset import KITTIRAWDataset
import numpy as np


class MixedDataset(MonoDataset):
    def __init__(self, data_path, filenames, height, width, frame_idxs, num_scales, is_train=False, img_ext='.jpg'):
        super(MixedDataset, self).__init__(data_path, filenames, height, width, frame_idxs, num_scales, is_train=is_train, img_ext=img_ext)

        self.K = np.array([[0.58, 0, 0.5, 0],
                           [0, 1.92, 0.5, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]], dtype=np.float32)
        self.full_res_shape = (1242, 375)

        self.carla = CarlaDataset(data_path + '/carla_data', filenames, height, width, frame_idxs, num_scales, is_train=is_train, img_ext=img_ext)
        self.kitti = KITTIRAWDataset(data_path + '/kitti_data', filenames, height, width, frame_idxs, num_scales, is_train=is_train, img_ext=img_ext)

    def get_color(self, folder, frame_index, side, do_flip):
        if side:
            return self.kitti.get_color(folder, frame_index, side, do_flip)
        return self.carla.get_color(folder, frame_index, side, do_flip)

    def check_depth(self):
        return True

    def get_depth(self, folder, frame_index, side, do_flip):
        if side:
            return self.kitti.get_depth(folder, frame_index, side, do_flip)
        return self.carla.get_depth(folder, frame_index, side, do_flip)
