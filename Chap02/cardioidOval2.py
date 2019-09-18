from tkinter import *
import math

W, H = (600, 600)       


def circle(cen= (300,299), r = 250 ,n = 256):
    p = []
    for i in range(n):
        t = 2 * math.pi * i / n
        p.append((r*math.cos(t)+cen[0], r*math.sin(t) + cen[1]))
    return tuple(p)

def circle_display(canvas, points):
    for i in range(len(points)):
        j = (i + 1) % len(points)
        canvas.create_line(points[i], points[j])

def display(canvas, points):
    for i in range(len(points)):
        r =((points[i][0] - points[0][0]) ** 2 + (points[i][1] - points[0][1])**2)**0.5
        p = circle((points[i][0], points[i][1]),r)
        circle_display(canvas, p)      


def main():
    root = Tk()                            # ルートフレームの作成
    canvas = Canvas(root, width = W, height = H, highlightthickness=0)
                                         # canvasの作成
    canvas.pack()                         # canvasの配置確定
    points = circle((350, 299),100)  
    circle_display(canvas, points) 
    display(canvas, points)                     # 描画関数 (display) の呼出
    root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
