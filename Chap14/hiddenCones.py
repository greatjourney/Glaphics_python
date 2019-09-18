import math
from OpenGL.GL import*
from myRotateCanvas import MyRotateCanvas
from wireCones import WireCones

class HiddenCones(WireCones):
    def __init__(self):
        super().__init__()

    def displayFaces(self):
        glColor3dv((0, 0, 0))
        glBegin(GL_POLYGON)
        for i in range(1, len(self.circle)):
            glVertex3dv(self.circle[len(self.circle)-i])
        glEnd()
        glBegin(GL_TRIANGLE_FAN)
        glVertex3dv(self.apex)
        for i in range(len(self.circle)):
            glVertex3dv(self.circle[i])
        glEnd()

    def display(self):
        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1, 1)
        NOC = 16
        for i in range(NOC):
            t = 2 * math.pi * i / NOC
            glPushMatrix()
            glTranslated(1.6 * math.sin(t), 0, 1.6*math.cos(t))
            glScaled(0.3, 1.4, 0.3)
            self.displayEdges()
            self.displayFaces()
            glPopMatrix()

def main():
    dispObj = HiddenCones()
    canvas = MyRotateCanvas()
    canvas.init(dispObj)
    canvas.loop()

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()   