import sys
import numpy as np 
from myCanvas import MyCanvas

class Fractal(object):
    def __init__(self, canvas,base,mats, vecs):
        if len(sys.argv) > 1:
            num = sys.argv[1]
        else:
            num = input('# of iterations -> ')
        self.times = int(num)
        self.canvas = canvas
        self.base, self.mats, self.vecs = (base, mats, vecs)

    def drawFractal(self, l = -1, mat = np.array(((1,0),(0,1))), vec = np.array((0,0))):
        if l < 0:
            l = self.times
        if l > 0:
            for i in range(len(self.mats)):
                self.drawFractal(l-1, mat.dot(self.mats[i]), mat.dot(self.vecs[i]) + vec)
        
        else:
            points = []
            for i in range(len(self.base)):
                points.append(mat.dot(self.base[i]) + vec)
            self.drawObject(points)