import cv2

# 画像の読み込み
img = cv2.imread("oit.png")

# BGR → YUV
img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# Y, U, Vチャンネルに分離
Y, U, V = cv2.split(img)

# 各チャンネルを表示
cv2.imshow("Y Channel", Y)
cv2.imshow("U Channel", U)
cv2.imshow("V Channel", V)

cv2.waitKey(0)
cv2.destroyAllWindows()