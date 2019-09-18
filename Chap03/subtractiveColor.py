from tkinter import *


W, H = (600, 600)       

def display(canvas):
    radius2 = 180**2
    centers = ((300.0,225.0), (213.4, 375.0),(386.6, 375))
    for y in range(H):
        for x in range(W):
            color = '#'
            for i in range(3):
                dist2 = (x-centers[i][0])**2 + (y - centers[i][1])**2
                color += 'ff' if dist2 > radius2 else '00'
            canvas.create_rectangle((x,y),(x,y), outline = '', fill = color)

def main():
    root = Tk()                            # ルートフレームの作成
    canvas = Canvas(root, width = W, height = H)
                                         # canvasの作成
    canvas.pack()                         # canvasの配置確定
    display(canvas)                     # 描画関数 (display) の呼出
    root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
