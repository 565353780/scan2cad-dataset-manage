#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scan2cad_dataset_manage.Module.dataset_loader import DatasetLoader


def demo():
    dataset_folder_path = "/home/chli/chLi/Scan2CAD/scan2cad_dataset/"
    scannet_dataset_folder_path = "/home/chli/chLi/ScanNet/scans/"
    shapenet_dataset_folder_path = "/home/chli/chLi/ShapeNet/Core/ShapeNetCore.v2/"
    dataset_loader = DatasetLoader(dataset_folder_path,
                                   scannet_dataset_folder_path,
                                   shapenet_dataset_folder_path)
    return True
