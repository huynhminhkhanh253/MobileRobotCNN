import math
import cv2


def calculate(v,h,x_shift,img):
    alpha = 8.0 * math.pi / 180  # degree measured manually
    v0 = 119.865631204  # from camera matrix
    ay = 332.262498472  # from camera matrix
    # compute and return the distance from the target point to the camera
    d = h / math.tan(alpha + math.atan((v - v0) / ay))
    if d > 0:
        cv2.putText(img, '==',(img.shape[1] - 500, img.shape[0] - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    return d

"""
while True:
    img = wM.getImg(True, size=[380, 240])
    cv2.putText(img, '==',(img.shape[1] - 600, img.shape[0] - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.imshow('img',img)
    cv2.waitKey(1)
"""
