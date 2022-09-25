#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../mesh-manage")

from scan2cad_dataset_manage.Module.dataset_loader import DatasetLoader

import open3d as o3d

def demo():
    dataset_folder_path = "/home/chli/chLi/Scan2CAD/scan2cad_dataset/"
    scannet_dataset_folder_path = "/home/chli/chLi/ScanNet/scans/"
    shapenet_dataset_folder_path = "/home/chli/chLi/ShapeNet/Core/ShapeNetCore.v2/"
    scannet_scene_name = "scene0474_02"
    scannet_object_file_path = "/home/chli/chLi/ScanNet/objects/scene0474_02/34_monitor.ply"

    dataset_loader = DatasetLoader(dataset_folder_path,
                                   scannet_dataset_folder_path,
                                   shapenet_dataset_folder_path)

    shapenet_model_file_path = dataset_loader.getShapeNetModelFilePathByBBoxDist(
        scannet_scene_name, scannet_object_file_path)
    print(scannet_object_file_path)
    print("-->")
    print(shapenet_model_file_path)
    return True
