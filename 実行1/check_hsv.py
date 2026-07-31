import os
import cv2
import numpy as np

# --------------------------------------------------
# 1. H（色相）の値から大体の色名を判定する関数
# --------------------------------------------------
def get_color_name(h, s, v):
    # 明度と彩度から黒・白・灰色を判定
    if v < 50:
        return "黒 (Black)"
    if s < 30:
        return "白 (White)" if v > 200 else "灰色 (Gray)"
    
    # H（色相）の値から色名を判定 (0〜179)
    if (0 <= h <= 10) or (170 <= h <= 179):
        return "赤 (Red)"
    elif 11 <= h <= 20:
        return "橙 (Orange)"
    elif 21 <= h <= 35:
        return "黄 (Yellow)"
    elif 36 <= h <= 85:
        return "緑 (Green)"
    elif 86 <= h <= 100:
        return "水色 (Cyan)"
    elif 101 <= h <= 135:
        return "青 (Blue)"
    elif 136 <= h <= 160:
        return "紫 (Purple)"
    return "不明"

# --------------------------------------------------
# 2. マウスクリック時のイベント処理
# --------------------------------------------------
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 左クリックされた時
        # クリックした位置 (y, x) のHSV値を取得
        hsv_val = hsv_img[y, x]
        h, s, v = hsv_val[0], hsv_val[1], hsv_val[2]
        
        # 色名の判定
        color_name = get_color_name(h, s, v)
        
        # ターミナルに出力
        print(f"位置: ({x}, {y}) | HSV: ({h}, {s}, {v}) | 色の目安: {color_name}")

        # 画像上に値を表示（確認しやすくするため）
        display_img = img.copy()
        text = f"H:{h} S:{s} V:{v} [{color_name}]"
        
        # 該当箇所に小さな円を描画し、文字を書き込む
        cv2.circle(display_img, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(display_img, text, (x + 10, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        cv2.imshow('Image Explorer', display_img)

# --------------------------------------------------
# 3. 画像の読み込み処理（日本語フォルダ対策）
# --------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'youkai.jpg')

img_array = np.fromfile(image_path, dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

if img is None:
    print(f"エラー: 画像が見つかりません ({image_path})")
    exit()

# BGR画像をHSV空間に変換
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# --------------------------------------------------
# 4. ウィンドウの表示とイベントハンドラ設定
# --------------------------------------------------
print("=== 操作方法 ===")
print("・画像上の調べたい場所を『左クリック』してください")
print("・キーボードの何か（EscやEnterなど）を押すと終了します")
print("================\n")

cv2.imshow('Image Explorer', img)

# マウスコールバック関数をセット
cv2.setMouseCallback('Image Explorer', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()