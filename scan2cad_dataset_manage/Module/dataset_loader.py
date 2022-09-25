#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

from scan2cad_dataset_manage.Data.dataset import Dataset


class DatasetLoader(object):

    def __init__(self,
                 dataset_folder_path=None,
                 scannet_dataset_folder_path=None,
                 shapenet_dataset_folder_path=None):
        self.dataset_folder_path = None
        self.scannet_dataset_folder_path = None
        self.shapenet_dataset_folder_path = None

        self.cad_appearances_json = None
        self.unique_cad_csv = None

        self.dataset = None

        if None not in [
                dataset_folder_path, scannet_dataset_folder_path,
                shapenet_dataset_folder_path
        ]:
            self.loadDataset(dataset_folder_path, scannet_dataset_folder_path,
                             shapenet_dataset_folder_path)
        return

    def reset(self):
        self.dataset_folder_path = None
        self.scannet_dataset_folder_path = None
        self.shapenet_dataset_folder_path = None

        self.cad_appearances_json = None
        self.unique_cad_csv = None
        return True

    def loadDataset(self, dataset_folder_path, scannet_dataset_folder_path,
                    shapenet_dataset_folder_path):
        assert os.path.exists(dataset_folder_path)
        assert os.path.exists(scannet_dataset_folder_path)
        assert os.path.exists(shapenet_dataset_folder_path)

        self.dataset_folder_path = dataset_folder_path
        self.scannet_dataset_folder_path = scannet_dataset_folder_path
        self.shapenet_dataset_folder_path = shapenet_dataset_folder_path

        cad_appearances_json_file_path = self.dataset_folder_path + "cad_appearances.json"
        assert os.path.exists(cad_appearances_json_file_path)

        with open(cad_appearances_json_file_path, "r") as f:
            cad_appearances_json = json.load(f)

        full_annotations_json_file_path = self.dataset_folder_path + "full_annotations.json"
        assert os.path.exists(full_annotations_json_file_path)

        with open(full_annotations_json_file_path, "r") as f:
            scene_dict_list = json.load(f)

        self.dataset = Dataset(scene_dict_list)
        return True

    def getShapeNetModelFilePath(self, scannet_scene_name):
        assert scannet_scene_name in self.dataset.scene_dict.keys()
        print(self.dataset.scene_dict[scannet_scene_name])
        shapenet_model_file_path = ""
        return shapenet_model_file_path
