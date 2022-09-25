#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json


class Dataset(object):

    def __init__(self,
                 dataset_folder_path=None,
                 scannet_dataset_folder_path=None,
                 shapenet_dataset_folder_path=None):
        self.dataset_folder_path = None
        self.scannet_dataset_folder_path = None
        self.shapenet_dataset_folder_path = None

        self.cad_appearances_json = None
        self.full_annotations_json = None
        self.unique_cad_csv = None

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
        self.full_annotations_json = None
        self.unique_cad_csv = None
        return True

    def loadJson(self):
        cad_appearances_json_file_path = self.dataset_folder_path + "cad_appearances.json"
        assert os.path.exists(cad_appearances_json_file_path)

        with open(cad_appearances_json_file_path, "r") as f:
            self.cad_appearances_json = json.load(f)

        full_annotations_json_file_path = self.dataset_folder_path + "full_annotations.json"
        assert os.path.exists(full_annotations_json_file_path)

        with open(full_annotations_json_file_path, "r") as f:
            self.full_annotations_json = json.load(f)

        return True

    def loadDataset(self, dataset_folder_path, scannet_dataset_folder_path,
                    shapenet_dataset_folder_path):
        assert os.path.exists(dataset_folder_path)
        assert os.path.exists(scannet_dataset_folder_path)
        assert os.path.exists(shapenet_dataset_folder_path)

        self.dataset_folder_path = dataset_folder_path
        self.scannet_dataset_folder_path = scannet_dataset_folder_path
        self.shapenet_dataset_folder_path = shapenet_dataset_folder_path

        self.loadJson()
        return True
