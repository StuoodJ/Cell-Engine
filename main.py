import pygame
import math
import sys
pygame.init()
screen = pygame.display.set_mode((480, 480))
clock = pygame.time.Clock()
running = True
dt = 0
cd = 480
f = 2
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    mouse_pos = pygame.mouse.get_pos
    mousex = mouse_pos()[0]
    gridx = math.floor(mousex/cd)
    mousey = mouse_pos()[1]
    gridy = math.floor(mousey/cd)
    mousecell = pygame.Rect((gridx*cd), (gridy*cd), cd, cd)
    pygame.draw.rect(screen, "red", mousecell)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        f -= 2
    if keys[pygame.K_s]:
        f += 2
    if f >= 20:
        f = 20
    if f <= 2:
        f = 2
    cd = 480/f
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()