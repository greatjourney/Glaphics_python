from myCanvas import MyCanvas
from vectorMatrix import norm
import myCircle

def pressed1(event):                     
    global startX, startY                
    startX, startY  = (event.x, event.y)

def dragged(event): 
    global canvas , startX, startY       
    canvas.clear()
    x, y = (event.x, event.y)
    r = norm((canvas.point(x, y) - canvas.point(startX, startY)))
    canvas.drawCircle(canvas.point(startX , startY), r)
    canvas.drawCircle(canvas.point(startX , startY), r / 2)
    canvas.drawCircle(canvas.point(startX , startY), r * 3/ 2)

def main():
    global canvas
    canvas = MyCanvas()
    canvas.bind('<Button-1>', pressed1) 
    canvas.bind('<B1-Motion>', dragged) 
    canvas.mainloop()

if __name__ == '__main__':
    main()