# Starts with just a box in the center of the screen that moves  left to right when keys are pressed

import pygame


class Player:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

    def move(self, keys):
        if keys[pygame.K_RIGHT] :
            self.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed

class Game:
    def __init__(self):
        pygame.init()
        self.screenW = 800
        self.screenH = 800
        self.win = pygame.display.set_mode((self.screenW, self.screenH))
        pygame.display.set_caption("Frogger")
        self.frog_size = 25
        self.frog_speed = 2
        self.frog = Player(self.screenW / 2, self.screenH/ 2 , self.frog_size, self.frog_speed)
    

    def redraw(self):
        self.win.fill("black")
        pygame.draw.rect(self.win, 'green', (self.frog.x, self.frog.y, self.frog.size, self.frog.size))
        pygame.display.update()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            self.frog.move(keys)
            self.redraw()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()