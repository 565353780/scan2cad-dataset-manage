#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

from scan2cad_dataset_manage.Method.path import createFileFolder

from scan2cad_dataset_manage.Module.dataset_loader import DatasetLoader


class ObjectModelMapGenerator(object):

    def __init__(self,
                 dataset_folder_path=None,
                 scannet_dataset_folder_path=None,
                 shapenet_dataset_folder_path=None,
                 scannet_bbox_dataset_folder_path=None):
        self.dataset_loader = DatasetLoader(dataset_folder_path,
                                            scannet_dataset_folder_path,
                                            shapenet_dataset_folder_path)

        self.scannet_bbox_dataset_folder_path = None
        self.shapenet_dataset_folder_path = None

        if None not in [
                scannet_bbox_dataset_folder_path, shapenet_dataset_folder_path
        ]:
            self.loadDatasetFolderPath(scannet_bbox_dataset_folder_path,
                                       shapenet_dataset_folder_path)
        return

    def reset(self):
        self.dataset_loader.reset()

        self.scannet_bbox_dataset_folder_path = None
        self.shapenet_dataset_folder_path = None
        return True

    def loadDatasetFolderPath(self, dataset_folder_path,
                              scannet_dataset_folder_path,
                              shapenet_dataset_folder_path,
                              scannet_bbox_dataset_folder_path):
        assert os.path.exists(dataset_folder_path)
        assert os.path.exists(scannet_dataset_folder_path)
        assert os.path.exists(shapenet_dataset_folder_path)
        assert os.path.exists(scannet_bbox_dataset_folder_path)

        self.reset()

        self.dataset_loader.loadDataset(dataset_folder_path,
                                        scannet_dataset_folder_path,
                                        shapenet_dataset_folder_path)

        self.scannet_bbox_dataset_folder_path = scannet_bbox_dataset_folder_path
        self.shapenet_dataset_folder_path = shapenet_dataset_folder_path
        return True

    def generateSceneObjectModelMap(self, scene, save_map_json_file_path):
        createFileFolder(save_map_json_file_path)

        scannet_scene_bbox_json_file_path = self.scannet_bbox_dataset_folder_path + \
            scene.scene_name + "/object_bbox.json"
        assert os.path.exists(scannet_scene_bbox_json_file_path)

        with open(scannet_scene_bbox_json_file_path, "r") as f:
            scannet_scene_bbox_json = json.load(f)
        print(scannet_scene_bbox_json)

        object_model_map_dict = {}
        return True
