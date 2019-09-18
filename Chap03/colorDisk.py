from tkinter import *
import math
import colorsys
from colorRingRGB import string

W, H = (600, 600)  

def display(canvas):
    center = (300,299)
    radius = 250
    for y in range(H):
        for x in range(W):
            dx = x -center[0]
            dy = y - center[1]
            h = math.atan2(dy,dx) / (2 * math.pi)
            h = h if h >= 0.0 else h + 1.0
            s = (dx**2+dy**2) **0.5 / radius
            v = 0.0 if s > 1.0 else 1.0
            s = 0.0 if s > 1.0 else s
            r, g, b = colorsys.hsv_to_rgb(h, s,v)
            color = string(r, g, b)
            canvas.create_rectangle((x,y),(x,y), outline = '', fill = color)

def main():
    root = Tk()                            # ルートフレームの作成
    canvas = Canvas(root, width = W, height = H, bg = 'black')
                          # canvasの作成
    canvas.pack()                         # canvasの配置確定
    display(canvas)                     # 描画関数 (display) の呼出
    root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
