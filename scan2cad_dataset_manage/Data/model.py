#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scan2cad_dataset_manage.Data.trans import Trans
from scan2cad_dataset_manage.Data.point import Point
from scan2cad_dataset_manage.Data.bbox import BBox


class Model(object):

    def __init__(self, model_dict=None):
        self.trans_model_to_world = None
        self.bbox = None
        self.center = None
        self.sym = None
        self.cad_id = None
        self.cad_cat_id = None
        self.cad_keypoint_list = None
        self.scan_keypoint_list = None

        if model_dict is not None:
            self.loadModelDict(model_dict)
        return

    def loadTrans(self, model_dict):
        self.trans_model_to_world = Trans(
            model_dict['trs']['translation'],
            model_dict['trs']['rotation'],
            model_dict['trs']['scale'],
        )
        return True

    def loadBBox(self, model_dict):
        self.center = Point.fromList(model_dict['center'])

        bbox_length = model_dict['bbox']
        self.bbox = BBox(
            Point(self.center.x - bbox_length[0],
                  self.center.y - bbox_length[1],
                  self.center.z - bbox_length[2]),
            Point(self.center.x + bbox_length[0],
                  self.center.y + bbox_length[1],
                  self.center.z + bbox_length[2]),
        )
        return True

    def loadSym(self, model_dict):
        self.sym = model_dict['sym'].split("__SYM_")[1]
        return True

    def loadCAD(self, model_dict):
        self.cad_id = model_dict['id_cad']
        self.cad_cat_id = model_dict['catid_cad']
        return True

    def loadKeyPoints(self, model_dict):
        self.cad_keypoint_list = model_dict['keypoints_cad']['position']
        self.scan_keypoint_list = model_dict['keypoints_scan']['position']
        return True

    def loadModelDict(self, model_dict):
        assert self.loadTrans(model_dict)
        assert self.loadBBox(model_dict)
        assert self.loadSym(model_dict)
        assert self.loadCAD(model_dict)
        assert self.loadKeyPoints(model_dict)
        return True
