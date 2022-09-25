#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scan2cad_dataset_manage.Module.dataset_loader import DatasetLoader


def demo():
    dataset_folder_path = "/home/chli/chLi/Scan2CAD/scan2cad_dataset/"
    scannet_dataset_folder_path = "/home/chli/chLi/ScanNet/scans/"
    shapenet_dataset_folder_path = "/home/chli/chLi/ShapeNet/Core/ShapeNetCore.v2/"

    scannet_scene_name = "scene0474_02"

    dataset_loader = DatasetLoader(dataset_folder_path,
                                   scannet_dataset_folder_path,
                                   shapenet_dataset_folder_path)

    shapenet_model_file_path = dataset_loader.getShapeNetModelFilePath(scannet_scene_name)
    print(scannet_scene_name, "-->", shapenet_model_file_path)
    return True
