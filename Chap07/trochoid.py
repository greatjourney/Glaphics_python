import math
import numpy as np   
from myCanvas import MyCanvas
from parametricCurve import ParametricCurve


class TrochoidCurve1(ParametricCurve):
    def __init__(self,canvas):
        super().__init__(canvas)

    def evaluate(self,t):
        return np.array((t - 0.8*math.sin(t), 1 - 0.8*math.cos(t)))

class TrochoidCurve2(ParametricCurve):
    def __init__(self,canvas):
        super().__init__(canvas)

    def evaluate(self,t):
        return np.array((t - 1.2*math.sin(t), 1 - 1.2*math.cos(t)))

def main():
    canvas = MyCanvas(r = 8)
    offset1 = np.array((-math.pi, 1.5))
    offset2 = np.array((-math.pi, -2.5))
    canvas.drawPolyline([np.array((-4,1.5)),np.array((4,1.5))],color='blue')
    canvas.drawPolyline([np.array((-4,-2.5)),np.array((4,-2.5))],color='blue')
    canvas.drawPolyline([np.array((-math.pi,-4)),np.array((-math.pi,4))],color='blue')
    for i in range(7):
        canvas.drawCircle((-math.pi + (i/3)*math.pi,1.5+0.9),0.9)
        canvas.drawCircle((-math.pi + (i/3)*math.pi,-2.5+1.1),1.1)
    TrochoidCurve1(canvas).drawCurve(-3, 8, offset1)  
    TrochoidCurve2(canvas).drawCurve(-3, 8, offset2) 
    canvas.mainloop()

if __name__ == '__main__':
    main()
    
