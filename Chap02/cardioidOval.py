from tkinter import *
import circle

W, H = (600, 600)       

def display(canvas, points):
    for i in range(len(points)):
        r =((points[i][0] - points[0][0]) ** 2 + (points[i][1] - points[0][1])**2)**0.5
        ul = (points[i][0] - r, points[i][1] - r)
        lr = (points[i][0] + r, points[i][1] + r)
        canvas.create_oval(ul,lr)



def main():
    root = Tk()                            # ルートフレームの作成
    canvas = Canvas(root, width = W, height = H, highlightthickness=0)
                                         # canvasの作成
    canvas.pack()                         # canvasの配置確定
    points = circle.circle((350, 299),100)  
    circle.display(canvas, points) 
    display(canvas, points)                     # 描画関数 (display) の呼出
    root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
