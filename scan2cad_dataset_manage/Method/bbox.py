#!/usr/bin/env python
# -*- coding: utf-8 -*-


def getBBoxDist(bbox_1, bbox_2):
    min_x_diff = bbox_1.min_point.x - bbox_2.min_point.x
    min_y_diff = bbox_1.min_point.y - bbox_2.min_point.y
    min_z_diff = bbox_1.min_point.z - bbox_2.min_point.z
    max_x_diff = bbox_1.max_point.x - bbox_2.max_point.x
    max_y_diff = bbox_1.max_point.y - bbox_2.max_point.y
    max_z_diff = bbox_1.max_point.z - bbox_2.max_point.z

    bbox_dist = \
        min_x_diff * min_x_diff + \
        min_y_diff * min_y_diff + \
        min_z_diff * min_z_diff + \
        max_x_diff * max_x_diff + \
        max_y_diff * max_y_diff + \
        max_z_diff * max_z_diff
    return bbox_dist


def getNearestModelIdxByBBoxDist(bbox, scene):
    min_bbox_dist = float('inf')
    min_bbox_dist_model_idx = -1
    for i, model in enumerate(scene.model_list):
        current_bbox_dist = getBBoxDist(bbox, model.bbox)
        if current_bbox_dist < min_bbox_dist:
            min_bbox_dist = current_bbox_dist
            min_bbox_dist_model_idx = i
    return min_bbox_dist_model_idx
