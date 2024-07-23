#Small changes which dont allow the frog/box to move off screen 

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
        frog_x, frog_y = move(keys, frog_x, frog_y, frog_speed, screenW, screenH, frog_size)
        

        redraw(win, frog_x, frog_y, frog_size)
    pygame.quit()


def move(keys, frog_x, frog_y, frog_speed, screenW, screenH, frog_size):
    if keys[pygame.K_RIGHT]and frog_x < screenW - frog_size:#***
        frog_x += frog_speed
    elif keys[pygame.K_LEFT] and frog_x > 0:#***
        frog_x -= frog_speed
    elif keys[pygame.K_UP] and frog_y > 0:#***
        frog_y -= frog_speed
    elif keys [pygame.K_DOWN] and frog_y < screenH - frog_size:#***
        frog_y += frog_speed
    return frog_x, frog_y


def redraw(win, frog_x, frog_y, frog_size):
    win.fill("black")
    pygame.draw.rect(win, ('green'), (frog_x, frog_y, frog_size, frog_size))
    pygame.display.update ()


if __name__ == "__main__":
    game()