import numpy as np 
from myGLCanvas import MyGLCanvas
from fractal import Fractal, getArgs
from cube import Cube

class MengerSponge(Fractal):
    def __init__(self, times):
        cube = Cube()
        nv = len(cube.vertices)
        ne = len(cube.edges)
        SCL = 1 / 3
        vecs = []
        for i in range(nv):
            vecs.append(np.array(cube.vertices[i]) * (1-SCL))
        for i in range(ne):
            mid = (np.array(cube.vertices[cube.edges[i][0]]) + 
                    np.array(cube.vertices[cube.edges[i][1]])) / 2
            
            vecs.append(mid * (1- SCL))
        super().__init__(cube, SCL, vecs, times)

def main():                              # main関数
    times, args = getArgs()
    dispObj = MengerSponge(times)       
    canvas = MyGLCanvas()                  # MyGLCanvasの作成
    canvas.init(dispObj)                   # OpenGLの初期化
    canvas.argsInit(args)             # シェル引数/キーボード入力による文字列の取得
    canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出

        

