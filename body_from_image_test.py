# -*-coding:utf8-*-
"""
It requires OpenCV installed for Python  
author:zhangyu
email:zhangyuyu417@gmail.com
"""
from flask import Flask

from flask import render_template

app = Flask(__name__)

import sys
import cv2
import os
from sys import platform
import argparse
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import json
from flask import request
import os
import base64

try:
    # Import Openpose (Windows/Ubuntu/OSX)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    try:
        # Change these variables to point to the correct folder (Release/x64 etc.)
        sys.path.append(dir_path + '/../bin/python/openpose/Release')
        os.environ['PATH'] = os.environ['PATH'] + ';' + dir_path + '/../x64/Release;' + dir_path + '/../bin;'
        import pyopenpose as op
    except ImportError as e:
        print(
            'Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
        raise e
    # Custom Params (refer to include/openpose/flags.hpp for more parameters)
    params = dict()
    params["model_folder"] = "../models/"

    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    # Process Image
    datum = op.Datum()
    # cv2.waitKey(0)
except Exception as e:
    print(e)


def get_pic(d='d:\\girl.jpg') -> np.ndarray:
    im = Image.open(d)  # 打开图片
    im_array = np.array(im)
    return im_array


def deal_with_pic(input_data=None):
    datum.cvInputData = get_pic()
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))
    # Display Image
    # print("Body keypoints: \n" + str(datum.poseKeypoints))
    cv2.imshow("OpenPose 1.7.0 - Tutorial Python API", datum.cvOutputData)
    cv2.waitKey(0)
    return str(datum.cvOutputData)


if __name__ == '__main__':
    d = get_pic()
    print(str(d))
    print("===")
    res = deal_with_pic(d)
    print(res)
    # t = np.array(res)
    # print(type(t))

