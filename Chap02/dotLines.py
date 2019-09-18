from tkinter import *                    # tkinterモジュールのimport

W, H = (600, 600)                        # canvasの幅と高さ

def display(canvas):                     # 描画関数
  '''
  canvas - 描画するcanvas
  11本の放射上の線分を1ピクセルごとに描画する
  '''
  points = ((W/60,  H), (W/20,  H), (W/8,  H), (W/4,  H),
            ( W/2,  H), (   W,  H), ( W, H/2), ( W, H/4),
            (  W, H/8), ( W, H/20), ( W, H/60)) # 線分の終点，11個
  origin = (0, 0)                        # 線分の始点 (左上隅)
  for i in range(len(points)):           # 線分描画の反復 (終点の個数分)
    if points[i][0] >= points[i][1]:     # x >= y (横長の直線)
      n = int(points[i][0])              # 表示ピクセルの個数(-1): n = x
      d = points[i][1] / points[i][0]    # 1ピクセルごとの差分
      for x in range(n):               # ピクセル(1x1長方形)描画の反復 (n+1)回
        p = (x, int(x*d+0.5))            # 長方形の左上隅
        q = (x+1, int(x*d+0.5)+1)        # 長方形の右下隅
        canvas.create_rectangle(p, q, outline='', fill='black')
                                         # 1ピクセル(1x1長方形)の描画
    else:                                # x < y (縦長の直線)
      n = int(points[i][1])              # 表示ピクセルの個数(-1): n = x
      d = points[i][0] / points[i][1]    # 1ピクセルごとの差分
      for y in range(n):               # ピクセル(1x1長方形)描画の反復 (n+1)回
        p = (int(y*d+0.5), y)            # 長方形の左上隅
        q = (int(y*d+0.5)+1, y+1)        # 長方形の右下隅
        canvas.create_rectangle(p, q, outline='', fill='black')
                                         # 1ピクセル(1x1長方形)の描画
def main():                              # main関数
  root = Tk()                            # ルートフレームの作成
  canvas = Canvas(root, width = W, height = H, highlightthickness=0)
                                         # canvasの作成
  canvas.pack()                          # canvasの配置確定
  display(canvas)                        # 描画関数 (display) の呼出
  root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
