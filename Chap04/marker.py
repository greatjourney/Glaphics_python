from tkinter import *                    # tkinterモジュールのimport

R = 5

def pressed1(event):                     
  global canvas                          
  x, y = (event.x, event.y)
  canvas.create_rectangle((x-R, y-R), (x+R, y+R), outline='', fill='#ff0000')

def pressed2(event):                      
  global canvas                         
  x, y = (event.x, event.y)
  canvas.create_rectangle((x-R, y-R), (x+R, y+R), outline='', fill='#00ff00')

def pressed3(event):                      
  global canvas                         
  x, y = (event.x, event.y)
  canvas.create_rectangle((x-R, y-R), (x+R, y+R), outline='', fill='#0000ff')
                                         
def main():                              # main関数
  global canvas                          # 大域変数 canvas
  W, H = (400, 400) 
  root = Tk()                            # ルートフレームの作成
  canvas = Canvas(root, width = W, height = H, bg='#ffffff') # canvasの作成
  canvas.pack()                          # canvasの配置確定
  canvas.bind('<Button-1>', pressed1)     # Button1 pressed コールバック関数
  canvas.bind('<Button-2>', pressed2)     # Button1 pressed コールバック関数
  canvas.bind('<Button-3>', pressed3)     # Button1 pressed コールバック関数
  root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
