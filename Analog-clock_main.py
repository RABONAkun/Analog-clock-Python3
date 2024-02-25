#インポート
import math
import datetime
import time
import tkinter as tk # tkinterをtkに省略
import threading
 
## 定数
WIDTH    = 400      # 幅
HEIGHT   = 400      # 高さ
RADIUS   = 190      # 半径
NEEDLE_H = 120      # 長針
NEEDLE_M = 160      # 短針
NEEDLE_S = 150      # 秒針
MARK     = 160      # 時字
BASE_AGL = 90       # 基準角度
W_TAG    = "needle" # ウィジェットタグ
CENTER   = int(WIDTH/2),int(HEIGHT/2)
 
### 時刻取得関数
def get_time():
 
    ### 無限ループ
    while True:
 
        ### 現在時刻取得
        now = datetime.datetime.now()
 
        ### 角度計算
        angle_h = float(BASE_AGL - 30 * now.hour - 0.5 * now.minute)    # 時
        angle_m = int(BASE_AGL - 6 * now.minute)                        # 分
        angle_s = int(BASE_AGL - 6 * now.second)                        # 秒
 
        ### 針の終端位置
        pos_hx = round(math.cos(math.radians(angle_h))*NEEDLE_H)    # 時のX座標
        pos_hy = round(math.sin(math.radians(angle_h))*NEEDLE_H)    # 時のY座標
        pos_mx = round(math.cos(math.radians(angle_m))*NEEDLE_M)    # 分のX座標
        pos_my = round(math.sin(math.radians(angle_m))*NEEDLE_M)    # 分のY座標
        pos_sx = round(math.cos(math.radians(angle_s))*NEEDLE_S)    # 秒のX座標
        pos_sy = round(math.sin(math.radians(angle_s))*NEEDLE_S)    # 秒のY座標
 
        ### 秒針表示
        canvas.create_line(CENTER, CENTER[0]+pos_hx, CENTER[1]-pos_hy, width=8, tags=W_TAG)
        canvas.create_line(CENTER, CENTER[0]+pos_mx, CENTER[1]-pos_my, width=5, tags=W_TAG)
        canvas.create_line(CENTER, CENTER[0]+pos_sx, CENTER[1]-pos_sy, width=2, tags=W_TAG)
 
        #### 待ち時間
        time.sleep(0.2)
 
        ### キャンバス初期化
        canvas.delete("needle")
 
### キャンバス作成
canvas = tk.Canvas(master=None, width=WIDTH, height=HEIGHT)
 
### 円表示
canvas.create_oval(10, 10, 390, 390, outline="lightgray", fill="lightgray")
 
### 目盛り表示
for mark in range(0, 360, 6):
    mark_o_x = round(math.cos(math.radians(mark))*RADIUS)           # 外側のX座標
    mark_o_y = round(math.sin(math.radians(mark))*RADIUS)           # 外側のY座標
 
    ### 正時
    if 0 == mark % 30:
        mark_i_x = round(math.cos(math.radians(mark))*(RADIUS-8))   # 内側のX座標
        mark_i_y = round(math.sin(math.radians(mark))*(RADIUS-8))   # 内側のY座標
        canvas.create_line((CENTER[0]+mark_i_x,CENTER[1]+mark_i_y), (CENTER[0]+mark_o_x,CENTER[1]+mark_o_y), width=3, fill="gray")
 
    ### 正時以外
    else:
        mark_i_x = round(math.cos(math.radians(mark))*(RADIUS-4))   # 内側のX座標
        mark_i_y = round(math.sin(math.radians(mark))*(RADIUS-4))   # 内側のY座標
        canvas.create_line((CENTER[0]+mark_i_x,CENTER[1]+mark_i_y), (CENTER[0]+mark_o_x,CENTER[1]+mark_o_y), width=1, fill="gray")
 
### 時字表示
dic = {"1":300,"2":330,"3":0,"4":30,"5":60,"6":90,"7":120,"8":150,"9":180,"10":210,"11":240,"12":270}
 
### 目盛り表示
for mark,angle in dic.items():
 
    ### 座標設定
    mark_x = round(math.cos(math.radians(angle))*MARK)
    mark_y = round(math.sin(math.radians(angle))*MARK)
 
    ### 時字表示
    canvas.create_text((CENTER[0]+mark_x,CENTER[1]+mark_y), text=mark, font=(None,24))
 
### キャンバス表示
canvas.pack()
 
### スレッド作成
thread = threading.Thread(target=get_time, daemon=True)
 
### スレッド開始
thread.start()
 
### イベントループ
canvas.mainloop()
