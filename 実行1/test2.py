import cv2

img = cv2.imread("test1.png")

# 幅640，高さ480に変更
resize_img = cv2.resize(img, (640, 480))

cv2.imshow('image',resize_img)
cv2.waitKey(0) #待機時間
cv2.destroyAllWindows #写真を閉じるためのウィンド