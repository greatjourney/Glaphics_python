import math
import numpy as np   
from myCanvas import MyCanvas
from parametricCurve import ParametricCurve

class Spiral(ParametricCurve):
    def __init__(self,canvas):
        super().__init__(canvas)

    def evaluate(self,t):
        return np.array((math.exp(t)*math.cos(t), math.exp(t)*math.sin(t)))


def main():
    canvas = MyCanvas(r = 100)
    canvas.drawPolyline([np.array((-4,0)),np.array((4,0))],color='blue')
    canvas.drawPolyline([np.array((0,-4)),np.array((0,4))],color='blue')
    Spiral(canvas).drawCurve(0, 4*math.pi) 
    canvas.mainloop()

if __name__ == '__main__':
    main()
    
