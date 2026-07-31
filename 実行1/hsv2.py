import cv2
import numpy as np

# 1. 画像の読み込み
image = cv2.imread('youkai.jpg')

# 2. BGRからHSV空間へ変換
# ※OpenCVでは標準がBGR形式で、Hの範囲は 0〜179 に変換されます
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3.1 抽出したい色の範囲を指定（例：赤色）
# 赤色はHue（色相）の0付近と170付近の両方にまたがるため、2つの領域を指定して結合します
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 100, 100])
upper_red2 = np.array([179, 255, 255])

# 3.2 抽出したい色の範囲を指定（例：黄色）
lower_yellow = np.array([20, 92, 100])
upper_yellow = np.array([30, 255, 255])

# 3.3 抽出したい色の範囲を指定（例：黒色）
lower_black = np.array([0, 0, 0])
upper_black = np.array([179, 255, 70])

# 3.4 抽出したい色の範囲を指定（例：白色）
lower_white = np.array([0, 0, 170])
upper_white = np.array([179, 50, 255])

# 3.5 抽出したい色の範囲を指定（例：ピンク色）
lower_pink = np.array([160, 100, 90])
upper_pink = np.array([179, 255, 255])

# 3.6 抽出したい色の範囲を指定（例：水色）
lower_cyan = np.array([82, 100, 150])
upper_cyan = np.array([89, 169, 250])

# 4. マスク画像の作成
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask12 = cv2.bitwise_or(mask1, mask2) # 2つのマスクを結合

mask3 = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask123 = cv2.bitwise_or(mask12, mask3) # 赤と黄色のマスクを結合

mask4 = cv2.inRange(hsv, lower_black, upper_black)
mask1234 = cv2.bitwise_or(mask123, mask4) # 赤、黄色、黒のマスクを結合

mask5 = cv2.inRange(hsv, lower_white, upper_white)
mask12345 = cv2.bitwise_or(mask1234, mask5) # 赤、黄色、黒、白色のマスクを結合

mask6 = cv2.inRange(hsv, lower_pink, upper_pink)
mask123456 = cv2.bitwise_or(mask12345, mask6) # 赤、黄色、黒、白色、ピンク色のマスクを結合

mask7 = cv2.inRange(hsv, lower_cyan, upper_cyan)
mask1234567 = cv2.bitwise_or(mask123456, mask7) # 赤

result = cv2.bitwise_and(image, image, mask=mask1234567)

cv2.imshow('Result', result)
cv2.waitKey(0)