from myCanvas import MyCanvas
from vectorMatrix import norm
import myCircle

def display(canvas, points):
    for i in range(len(points)):
        canvas.drawCircle((points[i][0], points[i][1]), points[i][1] - points[0][1])


def main():
    canvas = MyCanvas()
    points = myCircle.circle((0, 0), 100 * canvas.r / canvas.w)
    myCircle.display(canvas, points)
    display(canvas, points)
    canvas.mainloop()

if __name__ == '__main__':
    main()