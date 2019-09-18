import numpy as np   
from myCanvas import MyCanvas

class ParametricCurve(object):
    def __init__(self, canvas):
        self.canvas = canvas

    def drawCurve(self, ts =0, te=0, offset = np.array((0,0)), nop=128):
        dt = (te -ts) / nop
        prevPnt = self.evaluate(ts) + offset
        prevIn = self.canvas.inside(prevPnt)
        for i in range(nop):
            currPnt = self.evaluate(ts + dt*(i+1)) + offset
            currIn = self.canvas.inside(currPnt)
            if prevIn or currIn:
                self.canvas.drawPolyline([prevPnt,currPnt])
            prevPnt, prevIn = (currPnt, currIn)