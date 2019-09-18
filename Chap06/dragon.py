import math
import numpy as np
from vectorMatrix import rotMatrix, scaleMatrix
from myCanvas import MyCanvas
from fractal import Fractal

class Dragon(Fractal):
    def __init__(self, canvas):
        base = [np.array((-1,1)),np.array((0,0)), np.array((1,1))]
        mats = [scaleMatrix(1/math.sqrt(2)).dot(rotMatrix(3*math.pi/4))]
        mats.append(scaleMatrix(1/math.sqrt(2)).dot(rotMatrix(-3*math.pi/4)))
        mats.append(scaleMatrix(1/math.sqrt(2)).dot(rotMatrix(math.pi/4)))
        # mats.append(scaleMatrix(1/math.sqrt(2)).dot(rotMatrix(-math.pi/4)))
        vecs = [base[0]]
        vecs.append(mats[0].dot(base[0]) + vecs[0])
        vecs.append(mats[1].dot(base[0]) + vecs[1])
        # vecs.append(mats[2].dot(base[2]) + vecs[2])
        # vecs.append(mats[3].dot(base[2]) + vecs[3])
        super().__init__(canvas,base,mats, vecs)
    
    def drawObject(self, pnts):
        self.canvas.drawPolyline(pnts)

def main():
    canvas = MyCanvas(r=12)
    Dragon(canvas).drawFractal()
    canvas.mainloop()

if __name__ == '__main__':
    main()