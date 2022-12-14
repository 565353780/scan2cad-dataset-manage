#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append("../mesh-manage")

from scan2cad_dataset_manage.Module.dataset_loader import DatasetLoader


def demo():
    dataset_folder_path = "/home/chli/chLi/Scan2CAD/scan2cad_dataset/"
    scannet_dataset_folder_path = "/home/chli/chLi/ScanNet/scans/"
    shapenet_dataset_folder_path = "/home/chli/chLi/ShapeNet/Core/ShapeNetCore.v2/"

    dataset_loader = DatasetLoader(dataset_folder_path,
                                   scannet_dataset_folder_path,
                                   shapenet_dataset_folder_path)

    scene_name_list = dataset_loader.getSceneNameList()

    #  for scene_name in scene_name_list:
        #  print("render scene: ", scene_name)
        #  dataset_loader.renderScan2CADScene(scene_name)

    #  scannet_scene_name = "scene0013_02"
    scannet_scene_name = "scene0474_02"
    assert dataset_loader.isSceneValid(scannet_scene_name)

    dataset_loader.renderScan2CADScene(scannet_scene_name)
    return True
