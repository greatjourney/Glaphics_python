from tkinter import *
import circle

W, H = (600, 600)       

def display(canvas, points):
    for i in range(len(points)):
        j = (3 *i) % len(points)
        canvas.create_line(points[i], points[j])

def main():
    root = Tk()                            # ルートフレームの作成
    canvas = Canvas(root, width = W, height = H, highlightthickness=0)
                                         # canvasの作成
    canvas.pack()                         # canvasの配置確定
    points = circle.circle()  
    circle.display(canvas, points) 
    display(canvas, points)                     # 描画関数 (display) の呼出
    root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
