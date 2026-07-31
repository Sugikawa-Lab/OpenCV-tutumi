import cv2
import numpy as np

# 1. 画像の読み込み
image = cv2.imread('youkai.jpg')

# 2. BGRからHSV空間へ変換
# ※OpenCVでは標準がBGR形式で、Hの範囲は 0〜179 に変換されます
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3. 抽出したい色の範囲を指定（例：赤色）
# 赤色はHue（色相）の0付近と170付近の両方にまたがるため、2つの領域を指定して結合します
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 100, 100])
upper_red2 = np.array([179, 255, 255])

# 4. マスク画像の作成（範囲内の画素を255、範囲外を0に）
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2) # 2つのマスクを結合

# 5. 元画像にマスクを適用して指定色だけを抽出
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Result', result)
cv2.waitKey(0)