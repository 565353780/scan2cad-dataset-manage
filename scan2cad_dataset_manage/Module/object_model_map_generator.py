#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import numpy as np
from tqdm import tqdm

from scan2cad_dataset_manage.Method.path import createFileFolder
from scan2cad_dataset_manage.Module.dataset_loader import DatasetLoader


class ObjectModelMapGenerator(object):

    def __init__(self,
                 dataset_folder_path=None,
                 scannet_dataset_folder_path=None,
                 shapenet_dataset_folder_path=None,
                 scannet_object_dataset_folder_path=None,
                 scannet_bbox_dataset_folder_path=None):
        self.dataset_loader = DatasetLoader(dataset_folder_path,
                                            scannet_dataset_folder_path,
                                            shapenet_dataset_folder_path)

        self.scannet_object_dataset_folder_path = None
        self.scannet_bbox_dataset_folder_path = None
        self.shapenet_dataset_folder_path = None

        if None not in [
                dataset_folder_path, scannet_dataset_folder_path,
                shapenet_dataset_folder_path,
                scannet_object_dataset_folder_path,
                scannet_bbox_dataset_folder_path
        ]:
            self.loadDatasetFolderPath(dataset_folder_path,
                                       scannet_dataset_folder_path,
                                       shapenet_dataset_folder_path,
                                       scannet_object_dataset_folder_path,
                                       scannet_bbox_dataset_folder_path)
        return

    def reset(self):
        self.dataset_loader.reset()

        self.scannet_bbox_dataset_folder_path = None
        self.shapenet_dataset_folder_path = None
        return True

    def loadDatasetFolderPath(self, dataset_folder_path,
                              scannet_dataset_folder_path,
                              shapenet_dataset_folder_path,
                              scannet_object_dataset_folder_path,
                              scannet_bbox_dataset_folder_path):
        assert os.path.exists(dataset_folder_path)
        assert os.path.exists(scannet_dataset_folder_path)
        assert os.path.exists(shapenet_dataset_folder_path)
        assert os.path.exists(scannet_object_dataset_folder_path)
        assert os.path.exists(scannet_bbox_dataset_folder_path)

        self.reset()

        assert self.dataset_loader.loadDataset(dataset_folder_path,
                                               scannet_dataset_folder_path,
                                               shapenet_dataset_folder_path)

        self.scannet_object_dataset_folder_path = scannet_object_dataset_folder_path
        self.scannet_bbox_dataset_folder_path = scannet_bbox_dataset_folder_path
        self.shapenet_dataset_folder_path = shapenet_dataset_folder_path
        return True

    def generateSceneObjectModelMap(self, scene, save_map_json_file_path):
        scannet_scene_bbox_json_file_path = self.scannet_bbox_dataset_folder_path + \
            scene.scene_name + "/object_bbox.json"
        if not os.path.exists(scannet_scene_bbox_json_file_path):
            return True
        assert os.path.exists(scannet_scene_bbox_json_file_path)

        with open(scannet_scene_bbox_json_file_path, "r") as f:
            scannet_scene_bbox_json = json.load(f)

        scannet_object_center_dict = {}
        for scannet_object_file_name, scannet_object_bbox in scannet_scene_bbox_json.items(
        ):
            scannet_object_center = [
                (scannet_object_bbox[0][i] + scannet_object_bbox[1][i]) / 2.0
                for i in range(3)
            ]
            scannet_object_center_dict[
                scannet_object_file_name] = scannet_object_center

        scene_object_model_map_dict = {}

        for shapenet_model in scene.model_list:
            model_file_path = self.shapenet_dataset_folder_path + \
                shapenet_model.cad_cat_id + "/" + shapenet_model.cad_id + "/models/model_normalized.obj"
            assert os.path.exists(model_file_path)

            shapenet_model_min_point_list = [
                np.min(shapenet_model.trans_bbox_array[:, i]) for i in range(3)
            ]
            shapenet_model_max_point_list = [
                np.max(shapenet_model.trans_bbox_array[:, i]) for i in range(3)
            ]

            shapenet_model_trans_center = [
                (shapenet_model_min_point_list[i] +
                 shapenet_model_max_point_list[i]) / 2.0 for i in range(3)
            ]

            min_dist_scannet_object_file_name = None
            min_dist_to_shapenet_model_trans_center = float('inf')
            for scannet_object_file_name, scannet_object_center in scannet_object_center_dict.items(
            ):
                x_diff = scannet_object_center[
                    0] - shapenet_model_trans_center[0]
                y_diff = scannet_object_center[
                    1] - shapenet_model_trans_center[1]
                z_diff = scannet_object_center[
                    2] - shapenet_model_trans_center[2]
                current_dist_to_shapenet_model_trans_center = x_diff * x_diff + y_diff * y_diff + z_diff * z_diff
                if current_dist_to_shapenet_model_trans_center < min_dist_to_shapenet_model_trans_center:
                    min_dist_scannet_object_file_name = scannet_object_file_name
                    min_dist_to_shapenet_model_trans_center = current_dist_to_shapenet_model_trans_center

            scene_object_model_map_dict[
                min_dist_scannet_object_file_name] = shapenet_model.toDict()

        createFileFolder(save_map_json_file_path)
        with open(save_map_json_file_path, "w") as f:
            f.write(json.dumps(scene_object_model_map_dict, indent=4))
        return True

    def generateAllSceneObjectModelMap(self,
                                       save_map_json_folder_path,
                                       print_progress=False):
        os.makedirs(save_map_json_folder_path, exist_ok=True)

        for_data = self.dataset_loader.dataset.scene_dict.items()
        if print_progress:
            print(
                "[INFO][ObjectModelMapGenerator::generateAllSceneObjectModelMap]"
            )
            print("\t start generate object model map json for all scenes...")
            for_data = tqdm(for_data)
        for scene_name, scene in for_data:
            save_map_json_file_path = save_map_json_folder_path + scene_name + "/object_model_map.json"
            assert self.generateSceneObjectModelMap(scene,
                                                    save_map_json_file_path)
        return True
