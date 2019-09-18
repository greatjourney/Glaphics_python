from tkinter import *      

def pressed(event):
    global oldX, oldY
    oldX, oldY = (event.x, event.y)

def dragged(event):
    global canvas, oldX, oldY
    x, y = (event.x, event.y)
    canvas.create_line((oldX, oldY ), (x,y))
    oldX, oldY = (x,y)

def main():                              # main関数
  global canvas                          # 大域変数 canvas
  W, H = (400, 400) 
  root = Tk()                            # ルートフレームの作成
  canvas = Canvas(root, width = W, height = H, bg='#ffffff') # canvasの作成
  canvas.pack()                          # canvasの配置確定
  canvas.bind('<Button-1>', pressed)     # Button1 pressed コールバック関数
  canvas.bind('<B1-Motion>', dragged)     # Button1 pressed コールバック関数
  root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
