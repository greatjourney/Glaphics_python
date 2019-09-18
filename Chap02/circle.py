from tkinter import *                    # tkinterモジュールのimport
import sys
import math

W, H = (600, 600)       

def circle(cen= (300,299), r = 250 ):
    if len(sys.argv) > 1:
        num = sys.argv[1]
    else:
        num = input('# of points -> ')
    n = int(num)
    p = []
    for i in range(n):
        t = 2 * math.pi * i / n
        p.append((r*math.cos(t)+cen[0], r*math.sin(t) + cen[1]))
    return tuple(p)

def display(canvas, points):
    for i in range(len(points)):
        j = (i + 1) % len(points)
        canvas.create_line(points[i], points[j])




def main():                              # main関数
  root = Tk()                            # ルートフレームの作成
  canvas = Canvas(root, width = W, height = H, highlightthickness=0)
                                         # canvasの作成
  canvas.pack()                         # canvasの配置確定
  points = circle()  
  display(canvas, points)                      # 描画関数 (display) の呼出
  root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
