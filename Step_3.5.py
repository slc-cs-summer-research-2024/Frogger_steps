# 4 rows with multiple trucks

import pygame
from random import randrange

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

    def death(self):
        print("Game Over!")
        pygame.time.delay(2000)
        pygame.quit()
        quit()

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
    

        self.trucks_per_row = 4
        self.truck_rownum = 4
        self.truck_startY = 400
        self.truck_n_space = self.screenW/self.trucks_per_row
        self.truck_height = 30
        self.vert_btw_trucks = self.frog_size * 1.5
        self.trucks = self.create_trucks()


    def create_trucks(self):
        trucks = []
        dir = 1
        y_pos = self.truck_startY
        x_pos = 0 
        for i in range(self.trucks_per_row * self.truck_rownum):
            truck_length = (self.truck_n_space /randrange(2, 4)) 
            x_pos += self.truck_n_space
            trucks.append({'x': x_pos, 'y': y_pos, 'dir': dir , 'length': truck_length})
            if (i + 1) % self.trucks_per_row == 0: 
                x_pos = 0
                dir = dir * -1
                y_pos += (self.truck_height + self.vert_btw_trucks)
        return trucks

    def truck(self, frog_rect):
        for truck in self.trucks:
            truck['x'] += truck['dir']
            if truck['dir'] > 0 and truck['x'] > self.screenW:
                truck['x'] = -truck['length']
            elif truck['dir'] < 0 and truck['x'] < 0 - truck['length']:
                truck['x'] = self.screenW
            truck_rect = pygame.Rect(truck['x'], truck['y'], truck['length'], self.truck_height)
            if truck_rect.colliderect(frog_rect):
                self.frog.death()

    def redraw(self):
        self.win.fill("black")
        for truck in self.trucks:
            pygame.draw.rect(self.win, 'red', (truck['x'], truck['y'], truck['length'], self.truck_height))
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
            frog_rect = pygame.Rect(self.frog.x, self.frog.y, self.frog.size, self.frog.size)
            self.truck(frog_rect)
            self.redraw()


        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()