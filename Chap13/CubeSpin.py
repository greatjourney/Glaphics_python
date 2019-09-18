from mySpinCanvas import MySpinCanvas
from cube import Cube

def main():
    dispObj = Cube()
    canvas = MySpinCanvas()
    canvas.init(dispObj)
    canvas.loop()

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()   