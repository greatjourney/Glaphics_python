from tkinter import *
import circle

W, H = (600, 600)  

def f2hex(x):
    return '{:02X}'.format(int(x*0xff))

def string(r,g,b):
    return '#' + f2hex(r) + f2hex(g) + f2hex(b)

def color(n,i):
    oneSixth, twoSixth, threeSixth, fourSixth, fiveSixth, six = (1.0/6.0, 2.0/6.0, 3.0/6.0, 4.0/6.0, 5.0/6.0, 6.0)
    ratio = i/n
    if ratio <= oneSixth:
        return string(1.0, ratio*six, 0.0)
    elif ratio <= twoSixth:
        return string((twoSixth - ratio)*six, 1.0,  0.0)
    elif ratio <= threeSixth:
        return string(0.0,  1.0,(ratio - twoSixth)*six)
    elif ratio <= fourSixth:
        return string(0.0, (fourSixth - ratio)*six, 1.0)
    elif ratio <= fiveSixth:
        return string((ratio - fourSixth)*six, 0.0,  1.0)
    else:
        return string(1.0, 0.0, (1.0-ratio)*six)

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
