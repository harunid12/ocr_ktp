import cv2
import numpy as np

def bytes_to_cv2_image(image_bytes: bytes):
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    return img
