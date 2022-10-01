#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scan2cad_dataset_manage.Module.object_model_map_manager import ObjectModelMapManager


def demo():
    scannet_object_dataset_folder_path = "/home/chli/chLi/ScanNet/objects/"
    shapenet_dataset_folder_path = "/home/chli/chLi/ShapeNet/Core/ShapeNetCore.v2/"
    object_model_map_dataset_folder_path = "/home/chli/chLi/Scan2CAD/object_model_maps/"

    object_model_map_manager = ObjectModelMapManager(
        scannet_object_dataset_folder_path, shapenet_dataset_folder_path,
        object_model_map_dataset_folder_path)

    scannet_scene_name = "scene0013_02"
    scannet_object_file_name = "0_chair.ply"

    shapenet_model_dict = object_model_map_manager.getShapeNetModelDict(
        scannet_scene_name, scannet_object_file_name)

    print(shapenet_model_dict)
    return True
