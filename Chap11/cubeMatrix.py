import sys
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import cubePosition as cp

def reshape(width, height):
    fieldOfView, near, far = (25, 1, 20)
    aspect = width / height
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fieldOfView, aspect, near, far)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity() 
    eyeXZ = (cp.eyeX**2 + cp.eyeZ**2)**0.5
    eyeXYZ = (eyeXZ**2 + cp.eyeY**2)**0.5
    translate = (
    1,0,0,0,
    0,1,0,0,
    0,0,1,0,
    0,0,-eyeXYZ,1
    )
    glMultMatrixd(translate)
    sinP, cosP = (cp.eyeY/eyeXYZ, eyeXZ/eyeXYZ)
    rotateX = (
    1,0,0,0,
    0,cosP,sinP, 0,
    0,-sinP,cosP,0,
    0,0,0,1
    )
    glMultMatrixd(rotateX)
    sinT, cosT = (cp.eyeX/eyeXZ, cp.eyeZ/eyeXZ)
    rotateY = (
    cosT,  0, sinT, 0,
    0,       1,  0,      0,
    -sinT, 0,  cosT, 0,
    0,0,0,1
    )
    glMultMatrixd(rotateY)

def loop():
    glutReshapeFunc(reshape)
    glutDisplayFunc(cp.display)
    glutMainLoop()

def main():
    W, H = (500, 500)
    cp.window(W, H)
    cp.init()
    cp.argsInit()
    loop()

if __name__ == "__main__":
    main()
