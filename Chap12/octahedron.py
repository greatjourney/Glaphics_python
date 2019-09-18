from myGLCanvas import MyGLCanvas, getArgs # myGLCanvasモジュールのimport
from polyhedron import Polyhedron        # polyhedronモジュールのimport
import math

class Octahedron(Polyhedron):                  # Cubeクラスの定義
  def __init__(self):                    # 初期化メソッド
    '''
    立方体を初期化する
    '''
    super().__init__(                    # Polyhedronクラスの初期化メソッド
            ((math.sqrt(3), 0, 0), (-math.sqrt(3), 0, 0), (0, math.sqrt(3), 0), (0, -math.sqrt(3), 0),
             (0, 0, math.sqrt(3)), (0, 0, -math.sqrt(3))), # 頂点座標値
            ((0, 2, 4),(0, 3, 4) ,(4, 2, 1), (4, 3, 1),
             (1, 2, 5), (1, 3, 5), (5, 2, 0), (5, 3, 0)),        # 各面の頂点番号列
            ((0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 5),
             (2, 6), (3, 7), (4, 5), (5, 6), (6, 7), (7, 4)),  # 各稜線の頂点番号列
            ((  0,   1,   1), (  1,   0,   1), (  1,   1,   0), (1, 0, 0),
             (  0, 0.5, 0.5), (0.5,   0, 0.5), (0.5, 0.5,   0), (0, 1, 0)) ) # 各面の描画色

def main():                              # main関数
  dispObj = Octahedron()                       # Cubeオブジェクトの作成
  canvas = MyGLCanvas()                  # MyGLCanvasの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.argsInit(getArgs())             # シェル引数/キーボード入力による文字列の取得
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
