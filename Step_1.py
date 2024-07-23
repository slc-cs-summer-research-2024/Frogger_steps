# Box can now move up,down,left and right
#Box moves faster 
# *** where changes have been 

import pygame 

def game():
    pygame.init()

    screenW = 600
    screenH = 800
    win = pygame.display.set_mode((screenW,screenH))
    pygame.display.set_caption("Frogger")

    frog_size = 25
    frog_x = screenW//2
    frog_y = screenH - frog_size 
    frog_speed = 1 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        frog_x, frog_y = move(keys, frog_x, frog_y, frog_speed)
        

        redraw(win, frog_x, frog_y, frog_size)
    pygame.quit()


def move(keys, frog_x, frog_y, frog_speed):
    if keys[pygame.K_RIGHT]:
            frog_x += frog_speed
    elif keys[pygame.K_LEFT]:
            frog_x -= frog_speed
    elif keys[pygame.K_UP]: #***
            frog_y -= frog_speed #***
    elif keys [pygame.K_DOWN]:#***
            frog_y += frog_speed#***
    return frog_x, frog_y


def redraw(win, frog_x, frog_y, frog_size):
    win.fill("black")
    pygame.draw.rect(win, ('green'), (frog_x, frog_y, frog_size, frog_size))
    pygame.display.update ()


if __name__ == "__main__":
    game()