from myCanvas import MyCanvas

def pressed1(event):
    global canvas           
    canvas.drawMarker(canvas.point(event.x, event.y), fill='#ff0000')

def pressed2(event):
    global canvas           
    canvas.drawMarker(canvas.point(event.x, event.y), fill='#00ff00')

def pressed3(event):
    global canvas           
    canvas.drawMarker(canvas.point(event.x, event.y), fill='#0000ff')

def main():
    global canvas
    canvas = MyCanvas(width=400, height=400)
    canvas.mr = 5
    canvas.bind('<Button-1>', pressed1) 
    canvas.bind('<Button-2>', pressed2) 
    canvas.bind('<Button-3>', pressed3) 

if __name__ == '__main__':
    main()