import sys                               # sysモジュールのimport
from OpenGL.GL import *                  # GLモジュールのimport
from OpenGL.GLU import *                 # GLUモジュールのimport
from OpenGL.GLUT import *                # GLUTモジュールのimport

eyeX, eyeY, eyeZ = (4, 3, 7)                      # OpenGLウィンドウの幅と高さ

def window(width, height):               # ウィンドウ作成
  '''
  width  - OpenGLウィンドウの幅
  height - OpenGLウィンドウの高さ
  GLUTを初期化して，OpenGLウィンドウを作成する
  '''
  glutInit(sys.argv)                     # GLUTの初期化
  glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE) # 表示モードの指定
  glutInitWindowSize(width, height)      # ウィンドウサイズの指定
  glutInitWindowPosition(0, 0)           # ウィンドウ位置の指定
  glutCreateWindow('OpenGL')             # ウィンドウの作成


def init():                              # OpenGLの初期化
  '''
  OpenGLを初期化する
  '''
  glClearColor(0, 0, 0, 1)               # 背景色の設定 (白) 
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)


def argsInit():
    global eyeX, eyeY, eyeZ
    if len(sys.argv) > 3:
        args = sys.argv[1:]

    else:
        args = input('eyeX eyeY eyeZ or [] -> ').split(' ')
    
    if len(args) >= 3:
        eyeX, eyeY, eyeZ = (float(args[0]),float(args[1]),float(args[2]))



def reshape(width, height):              # ウィンドウのサイズ変更に伴うコールバック関数
  '''
  width  - 変更後のOpenGLウィンドウの幅
  height - 変更後のOpenGLウィンドウの高さ
  ウィンドウサイズ変更に伴う処理を行う
  '''
  global eyeX, eyeY, eyeZ
  fieldOfView ,near ,far = (25, 1, 20)
  aspect = width / height
  glViewport(0, 0, width, height)        # ビューポートの設定
  glMatrixMode(GL_PROJECTION)            # 投影変換行列の設定開始
  glLoadIdentity()                       # 恒等行列での初期化
  gluPerspective(fieldOfView, aspect, near ,far)
  glMatrixMode(GL_MODELVIEW)             # モデル変換行列の設定開始
  glLoadIdentity()                       # 恒等行列での初期化
  gluLookAt(eyeX, eyeY, eyeZ,0,0,0,0,1,0)

def display():                           # 描画要求に伴うコールバック関数
  '''
  描画要求に伴う処理を行う (放射状の線を描画する)
  '''
  vertices = ((-1, -1, -1),(1, -1, -1),(1, 1, -1),(-1, 1, -1),
            (-1, -1, 1),(1, -1, 1),(1, 1, 1),(-1, 1, 1))
  
  faces = ((1,2,6,5),(2,3,7,6),(4,5,6,7),
            (0,4,7,3),(0,1,5,4),(0,3,2,1))

  colors = ((0,1,1),(1,0,1),(1,1,0),
            (0,0.5,0.5),(0.5,0,0.5),(0.5,0.5,0))
 
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)           # 背景の消去
  glBegin(GL_QUADS)                      # 線分描画の開始
  for i in range(len(faces)):           # 線分描画の反復 (終点の個数分)
    glColor3dv(colors[i])
    for j in range(len(faces[i])):  
        glVertex3dv(vertices[faces[i][j]])                  # 線分の始点
  glEnd()                                # 線分描画の終了
  glFlush()                              # 描画命令の送信

def loop():                              # コールバック関数の設定とループ起動
  '''
  reshape と displayコールバック関数を設定し，ループを起動する
  '''
  glutReshapeFunc(reshape)               # reshapeコールバック関数の登録
  glutDisplayFunc(display)               # displayコールバック関数の登録
  glutMainLoop()                         # GLUTのメインループ起動

def main():                              # main関数
  W, H = (500, 500)
  window(W, H)                           # ウィンドウの作成
  init()                                 # OpenGLの初期化
  argsInit()
  loop()                                 # コールバック関数の設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
