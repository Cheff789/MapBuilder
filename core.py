from VisualLib import point
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *



def main():
    pygame.init()
    display = (800,600)
    l1 = point(1,0,color(.5,1,1))
    l2 = point(0,1,color(.5,1,1))
    l3 = point(-1,0,color(.5,1,1))
    l4 = point(0,-1,color(.5,1,1))
    q = quad(l1,l2,l3,l4)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)
    getTicksLastFrame = 0
    while True:
        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        q.draw()

        pygame.display.flip()
        pygame.time.wait(10)
        print(deltaTime)


main()