#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scan2cad_dataset_manage.Data.dataset import Dataset


class DatasetLoader(object):

    def __init__(self,
                 dataset_folder_path=None,
                 scannet_dataset_folder_path=None,
                 shapenet_dataset_folder_path=None):
        self.dataset = Dataset(dataset_folder_path,
                               scannet_dataset_folder_path,
                               shapenet_dataset_folder_path)
        return

    def loadDataset(self, dataset_folder_path, scannet_dataset_folder_path,
                    shapenet_dataset_folder_path):
        return self.dataset.loadDataset(dataset_folder_path,
                                        scannet_dataset_folder_path,
                                        shapenet_dataset_folder_path)
