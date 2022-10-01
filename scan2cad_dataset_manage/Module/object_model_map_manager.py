#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os


class ObjectModelMapManager(object):

    def __init__(self,
                 scannet_object_dataset_folder_path=None,
                 shapenet_dataset_folder_path=None,
                 object_model_map_dataset_folder_path=None):

        self.scannet_object_dataset_folder_path = None
        self.shapenet_dataset_folder_path = None
        self.object_model_map_dataset_folder_path = None

        self.scene_name = None
        self.scene_name_list = None
        self.scene_object_model_map_dict = None

        if None not in [
                scannet_object_dataset_folder_path,
                shapenet_dataset_folder_path,
                object_model_map_dataset_folder_path
        ]:
            self.loadDataset(scannet_object_dataset_folder_path,
                             shapenet_dataset_folder_path,
                             object_model_map_dataset_folder_path)
        return

    def reset(self):
        self.scannet_object_dataset_folder_path = None
        self.shapenet_dataset_folder_path = None
        self.object_model_map_dataset_folder_path = None

        self.scene_name_list = None
        self.scene_object_model_map_dict = None
        return

    def loadDataset(self, scannet_object_dataset_folder_path,
                    shapenet_dataset_folder_path,
                    object_model_map_dataset_folder_path):
        assert os.path.exists(scannet_object_dataset_folder_path)
        assert os.path.exists(shapenet_dataset_folder_path)
        assert os.path.exists(object_model_map_dataset_folder_path)

        self.reset()

        self.scannet_object_dataset_folder_path = scannet_object_dataset_folder_path
        self.shapenet_dataset_folder_path = shapenet_dataset_folder_path
        self.object_model_map_dataset_folder_path = object_model_map_dataset_folder_path

        self.scene_name_list = os.listdir(
            self.object_model_map_dataset_folder_path)
        return

    def loadScene(self, scene_name):
        if scene_name == self.scene_name:
            return
        assert scene_name in self.scene_name_list

        object_model_map_json_file_path = self.object_model_map_dataset_folder_path + \
            scene_name + "/object_model_map.json"
        assert os.path.exists(object_model_map_json_file_path)

        with open(object_model_map_json_file_path, "r") as f:
            self.scene_object_model_map_dict = json.load(f)
        return

    def getShapeNetModelDict(self, scene_name, object_file_name):
        self.loadScene(scene_name)

        assert self.scene_object_model_map_dict is not None
        assert object_file_name in self.scene_object_model_map_dict.keys()

        shapenet_model_dict = self.scene_object_model_map_dict[
            object_file_name]

        scannet_object_file_path = self.scannet_object_dataset_folder_path + \
            scene_name + "/" + object_file_name
        assert os.path.exists(scannet_object_file_path)

        shapenet_model_file_path = self.shapenet_dataset_folder_path + \
            shapenet_model_dict['cad_cat_id'] + "/" + shapenet_model_dict['cad_id'] + \
            "/models/model_normalized.obj"
        assert os.path.exists(shapenet_model_file_path)

        shapenet_model_dict[
            "scannet_object_file_path"] = scannet_object_file_path
        shapenet_model_dict[
            "shapenet_model_file_path"] = shapenet_model_file_path

        return shapenet_model_dict
