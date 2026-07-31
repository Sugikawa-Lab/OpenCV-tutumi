import cv2

# 画像の読み込み
img = cv2.imread("oit.png")

# BGR → LAB
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# L, A, Bチャンネルに分離
L, A, B = cv2.split(img)

# 各チャンネルを表示
cv2.imshow("L Channel", L)
cv2.imshow("A Channel", A)
cv2.imshow("B Channel", B)

cv2.waitKey(0)
cv2.destroyAllWindows()