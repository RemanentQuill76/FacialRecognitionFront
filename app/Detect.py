import pyrealsense2 as rs
import cv2
import numpy as np
import time

debug_mode = True


def display_bbox_values(bbox):
    if debug_mode:
        print(
            f"Raw bounding box values: x1={bbox[0]}, y1={bbox[0]}, x2={bbox[1]}, y2={bbox[1]}"
        )


pipeline = rs.pipeline()
config = rs.config()

config.enable_stream(rs.stream.depth, 1024, 768, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

hole_filling = rs.hole_filling_filter()
colorizer = rs.colorizer()
