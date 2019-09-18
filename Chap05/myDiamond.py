from myCanvas import MyCanvas
from vectorMatrix import norm
import myCircle

def display(canvas, points):
    for i in range(len(points) -1):
        for j in range(i + 1, len(points)):
            canvas.drawPolyline((points[i], points[j]))

def main():
    canvas = MyCanvas()
    points = myCircle.circle((0, 0), 250 * canvas.r / canvas.w)
    myCircle.display(canvas, points)
    display(canvas, points)
    canvas.mainloop()

if __name__ == '__main__':
    main()