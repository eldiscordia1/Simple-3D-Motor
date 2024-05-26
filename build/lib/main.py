import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [
    [1, -1, -1],  # 0
    [1, 1, -1],   # 1
    [-1, 1, -1],  # 2
    [-1, -1, -1], # 3
    [1, -1, 1],   # 4
    [1, 1, 1],    # 5
    [-1, -1, 1],  # 6
    [-1, 1, 1]    # 7
]

edges = [
    [0, 1, 2, 3],
    [4, 5, 7, 6],
    [0, 4, 6, 3],
    [1, 5, 7, 2],
    [0, 1, 5, 4],
    [2, 3, 7, 6]
]

colors = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
]

def draw_cube():
    for i, edge in enumerate(edges):
        glBegin(GL_QUADS)
        glColor3fv(colors[i])
        for vertex in edge:
            glVertex3fv(vertices[vertex])
        glEnd()

def render_text(text, position):
    font = pygame.font.SysFont(None, 32)
    text_surface = font.render(text, True, (255, 255, 255))
    text_width, text_height = text_surface.get_size()
    text_x, text_y = position
    glPushMatrix()
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)
    glRasterPos2i(text_x, text_y)
    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_BLEND)
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_TEXTURE_2D)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tostring(text_surface, "RGBA", False))
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glClearColor(0.53, 0.81, 0.98, 1)  # Celeste

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Dibuja el cubo
        draw_cube()
        
        # Rotación de la cámara
        glRotatef(0.5, 1, 1, 1)
        
        # Renderiza el texto
        render_text("Made By Mars!", (10, display[1] - 40))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()


