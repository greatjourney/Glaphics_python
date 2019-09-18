import math
import numpy as np   
from myCanvas import MyCanvas
from parametricCurve import ParametricCurve

class CycloidCurve(ParametricCurve):
    def __init__(self,canvas):
        super().__init__(canvas)

    def evaluate(self,t):
        return np.array((t - math.sin(t), 1 - math.cos(t)))


def main():
    canvas = MyCanvas(r = 8)
    offset = np.array((-math.pi, 0))
    canvas.drawPolyline([np.array((-4,0)),np.array((4,0))],color='blue')
    canvas.drawPolyline([np.array((-math.pi,-4)),np.array((-math.pi,4))],color='blue')
    for i in range(7):
        canvas.drawCircle((-math.pi + (i/3)*math.pi,1),1)
    CycloidCurve(canvas).drawCurve(-3, 8, offset) 
    canvas.mainloop()

if __name__ == '__main__':
    main()
    
