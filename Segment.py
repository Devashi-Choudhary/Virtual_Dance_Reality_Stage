# The Class : DeepLabModel and Function : drawSegment, run_visualization is inspired from https://github.com/susheelsk/image-background-removal
import os
from io import BytesIO
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import tensorflow as tf
import sys
import datetime

# Class to load deeplab model and run inference.
class DeepLabModel(object):
    INPUT_TENSOR_NAME = 'ImageTensor:0'
    OUTPUT_TENSOR_NAME = 'SemanticPredictions:0'
    INPUT_SIZE = 513
    FROZEN_GRAPH_NAME = 'frozen_inference_graph'
    
    # Creates and loads pretrained deeplab model.
    def __init__(self, tarball_path):
        self.graph = tf.Graph()
        graph_def = None
        graph_def = tf.compat.v1.GraphDef.FromString(open("/Users/devashi/Desktop/Virtual_Dance_Reality_Show/xception_model" + "/frozen_inference_graph.pb", "rb").read()) 
        if graph_def is None:
              raise RuntimeError('Cannot find inference graph in tar archive.')
        with self.graph.as_default():
              tf.import_graph_def(graph_def, name='')
        self.sess = tf.compat.v1.Session(graph=self.graph)
    
    # Runs inference on a single image. Args: image: A PIL.Image object, raw input image.
    # Returns: 1. resized_image: RGB image resized from original input image. 2. seg_map: Segmentation map of `resized_image`
    def run(self, image):
        start = datetime.datetime.now()
        width, height = image.size
        resize_ratio = 1.0 * self.INPUT_SIZE / max(width, height)
        target_size = (int(resize_ratio * width), int(resize_ratio * height))
        resized_image = image.convert('RGB').resize(target_size, Image.ANTIALIAS)
        batch_seg_map = self.sess.run(
            self.OUTPUT_TENSOR_NAME, feed_dict={self.INPUT_TENSOR_NAME: [np.asarray(resized_image)]})
        seg_map = batch_seg_map[0]
        end = datetime.datetime.now()
        diff = end - start
        #print("Time taken to evaluate segmentation is : " + str(diff))
        return resized_image, seg_map


def drawSegment(baseImg, matImg):
    width, height = baseImg.size
    dummyImg = np.zeros([height, width, 4], dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            color = matImg[y,x]
            (r,g,b) = baseImg.getpixel((x,y))
            if color == 0:
                dummyImg[y,x,3] = 0
            else :
                dummyImg[y,x] = [r,g,b,255]
    img = Image.fromarray(dummyImg)
    return img  


# Inferences DeepLab model and visualizes result.
def run_visualization(filepath):
    try:
        orignal_im = filepath
    except IOError:
        print('Cannot retrieve image. Please check file: ' + filepath)
        return
    #print('running deeplab on image %s...' % filepath)
    resized_im, seg_map = MODEL.run(orignal_im)
    bgrimg = drawSegment(resized_im, seg_map)
    return bgrimg

MODEL = DeepLabModel("xception_model")