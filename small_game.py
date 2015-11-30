# This file has been implemented to the fork by Max Ferney
# No legal thingy for this file

# this program was the simple_game_template.py program,
#   but I just modified it. I only used it as a template

import pygame
from xbox360_controller import XBox360Controller

pygame.init()

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY  = (125, 125, 125)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
BLUE =  (  0,   0, 255)

# window settings
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Little Game")
FPS = 30
clock = pygame.time.Clock()

# make a controller
controller = XBox360Controller(0)
    
# drawing functions
def draw_ground():
    pygame.draw.rect(screen, GRAY, [0, size[1]-200, size[0], size[1]], 0)

def draw_player(pos):
    pygame.draw.rect(screen, BLACK, [pos[0], pos[1], 10, 20], 0)

def draw_attack(pos):
    #porcupine
    pygame.draw.line(screen, RED, [pos[0], pos[1]+5], [pos[0]-15, pos[1]+5])
    pygame.draw.line(screen, RED, [pos[0], pos[1]], [pos[0]-7.5, pos[1]-7.5])
    pygame.draw.line(screen, RED, [pos[0]+5, pos[1]], [pos[0]+5, pos[1]-15])
    pygame.draw.line(screen, RED, [pos[0]+10, pos[1]], [pos[0]+17.5, pos[1]-7.5])
    pygame.draw.line(screen, RED, [pos[0]+10, pos[1]+5], [pos[0]+25, pos[1]+5])
    
# Player
x = (size[0]/2)-5
y = (size[1]-220)
startpos1 = [x, y]
p1_pos = [x, y]

# game loop
playing = False
done = False
attacking = False
moved = False

while not done:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    # joystick stuff
    back = controller.back()
    start = controller.start()
    lt_stick = controller.left_stick_axes()
    A = controller.a()      #go up
    B = controller.b()      #go down
    X = controller.x()      #attack
    hat = controller.hat()
    

    # game logic
    if not playing:
        if start == 1:
            playing = True
    else:
        if back == 1:
            playing = False
            p1_pos = startpos1

    if playing:
        p1_pos[0] += int(lt_stick[0] * 5)
        if X == 1:
            attacking = True
        if X == 0:
            attacking = False

        if not moved:
            if A == 1 or hat[1] == -1:
                p1_pos[1] -= 10
                moved = True
            if B == 1 or hat[1] == 1:
                p1_pos[1] += 10
                moved = True
            if hat[0] == -1:
                p1_pos[0] -= 10
                moved = True
            if hat[0] == 1:
                p1_pos[0] += 10
                moved = True
        if A == 0 and B == 0 and hat[0] == 0 and hat[1] == 0:
            moved = False
        

    # drawing
    screen.fill(WHITE)

    draw_ground()

    if attacking:
        draw_attack(p1_pos)
        
    draw_player(p1_pos)
    
    # update screen
    pygame.display.flip()
    clock.tick(FPS)

# close window on quit
pygame.quit ()
