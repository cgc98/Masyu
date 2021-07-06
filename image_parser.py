import matplotlib.pyplot as plt
import numpy as np
import cv2
import image_slicer
from skimage.measure import compare_ssim

image_slicer.slice('grid.jpg', 400)