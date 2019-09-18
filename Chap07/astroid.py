import math
import numpy as np   
from myCanvas import MyCanvas
from parametricCurve import ParametricCurve

class CycloidCurve(ParametricCurve):
    def __init__(self,canvas):
        super().__init__(canvas)

    def evaluate(self,t):
        return np.array((3*math.cos(t)**3, 3*math.sin(t)**3))


def main():
    canvas = MyCanvas(r = 8)
    canvas.drawPolyline([np.array((-4,0)),np.array((4,0))],color='blue')
    canvas.drawPolyline([np.array((0,-4)),np.array((0,4))],color='blue')
    CycloidCurve(canvas).drawCurve(-4, 4) 
    canvas.mainloop()

if __name__ == '__main__':
    main()
    
