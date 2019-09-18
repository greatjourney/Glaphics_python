from tkinter import *
import circle
import colorsys

W, H = (600, 600)  

def f2hex(x):
    return '{:02X}'.format(int(x*0xff))

def string(r,g,b):
    return '#' + f2hex(r) + f2hex(g) + f2hex(b)

def color(n,i):
    h = i/n
    s = v = 1.0
    r, g, b = colorsys.hsv_to_rgb(h, s,v)
    return string(r,g,b)


def display(canvas, points):
    for i in range(len(points)):
        j = (i + 1) % len(points)
        canvas.create_line(points[i], points[j], fill = color(len(points), i))

def main():
    root = Tk()                            # ルートフレームの作成
    canvas = Canvas(root, width = W, height = H, bg = 'black')
                                         # canvasの作成
    canvas.pack()                         # canvasの配置確定
    points = circle.circle()  
    display(canvas, points)                    # 描画関数 (display) の呼出
    root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
