#!/usr/bin/env python
# -*- coding: utf-8 -*-

import open3d as o3d

from scan2cad_dataset_manage.Method.bbox import getOpen3DBBoxFromBBox


def renderScan2CADBBox(scene):
    bbox_list = []
    for model in scene.model_list:
        bbox_list.append(getOpen3DBBoxFromBBox(model.bbox))

    o3d.visualization.draw_geometries(bbox_list)
    return True
