#Small changes which dont allow the frog/box to move off screen 

import pygame


class Player:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

    def move(self, keys, screenW, screenH):
        if keys[pygame.K_RIGHT] and self.x < screenW - self.size:
            self.x += self.speed
        elif keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        elif keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        elif keys[pygame.K_DOWN] and self.y < screenH - self.size:
            self.y += self.speed


class Game:
    def __init__(self):
        pygame.init()
        self.screenW = 800
        self.screenH = 800
        self.win = pygame.display.set_mode((self.screenW, self.screenH))
        pygame.display.set_caption("Frogger")

        self.frog_size = 25
        self.frog_speed = 2
        self.frog = Player(self.screenW // 2, self.screenH - self.frog_size, self.frog_size, self.frog_speed)
    

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
            self.frog.move(keys, self.screenW, self.screenH)
            self.redraw()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()