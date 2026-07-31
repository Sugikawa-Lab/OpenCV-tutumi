import numpy as np
import cv2
img0 = cv2.imread('test1.png',1)
cv2.imshow('image',img0)
cv2.waitKey(0) #待機時間
cv2.destroyAllWindows #写真を閉じるためのウィンドウ