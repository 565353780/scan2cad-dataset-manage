#!/usr/bin/env python
# -*- coding: utf-8 -*-

import open3d as o3d

from scan2cad_dataset_manage.Method.bbox import getOpen3DBBoxFromBBox


def renderScan2CADBBox(scene):
    shapenet_dataset_folder_path = "/home/chli/chLi/ShapeNet/Core/ShapeNetCore.v2/"
    gt_mesh_file_path = \
        "/home/chli/chLi/ScanNet/scans/scene0474_02/scene0474_02_vh_clean.ply"

    bbox_list = []
    mesh_list = []

    for model in scene.model_list:
        bbox_list.append(getOpen3DBBoxFromBBox(model.trans_bbox))
        model_file_path = shapenet_dataset_folder_path + \
            model.cad_cat_id + "/" + model.cad_id + "/models/model_normalized.obj"
        mesh = o3d.io.read_triangle_mesh(model_file_path)
        mesh.transform(model.trans_matrix)
        mesh_list.append(mesh)

    gt_mesh = o3d.io.read_triangle_mesh(gt_mesh_file_path)

    o3d.visualization.draw_geometries(bbox_list + mesh_list + [gt_mesh])
    return True
