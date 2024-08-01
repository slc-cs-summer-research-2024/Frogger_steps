#logs can have frog jump on them and moves frog 


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

    def win_game(self):
        print("Winner!")
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
        self.log_per_row = 4
        self.log_rownum = 4
        self.log_n_space = self.screenW/self.log_per_row
        self.logs_startY = 50
        self.Log_speed = 1
        
    
        self.vert_btw_logs = self.frog_size / 5
        self.log_height = 40
        self.logs = self.create_logs()

        

        self.trucks_per_row = 4
        self.truck_rownum = 4
        self.truck_startY = 400
        self.truck_n_space = self.screenW/self.trucks_per_row
        self.truck_height = 30
        self.truck_speed = 1
        self.vert_btw_trucks = self.frog_size * 1.5
        self.trucks = self.create_trucks()

    def create_logs(self):
        logs = []
        dir = 1
        y_pos = self.logs_startY
        x_pos = 0
        for i in range(self.log_per_row * self.log_rownum):
            log_length = (self.log_n_space /randrange(2, 4)) 
            x_pos += self.log_n_space
            logs.append({'x': x_pos, 'y': y_pos, 'dir': dir * self.Log_speed, 'length': log_length})
            if (i + 1) % self.log_per_row == 0: 
                self.Log_speed += (dir*(randrange(1,6))/10)
                x_pos = 0
                dir = dir * -1
                y_pos += (self.log_height + self.vert_btw_logs)
        return logs

    def create_trucks(self):
        trucks = []
        dir = 1
        y_pos = self.truck_startY
        x_pos = 0 
        for i in range(self.trucks_per_row * self.truck_rownum):
            truck_length = (self.truck_n_space /randrange(2, 4)) 
            x_pos += self.truck_n_space
            trucks.append({'x': x_pos, 'y': y_pos, 'dir': dir * self.truck_speed, 'length': truck_length})
            if (i + 1) % self.trucks_per_row == 0: 
                self.truck_speed += (dir * (randrange(1, 6)) / 10)
                x_pos = 0
                dir = dir * -1
                y_pos += (self.truck_height + self.vert_btw_trucks)
        return trucks

    def log(self):
        for log in self.logs:
            log['x'] += log['dir']
            if log['dir'] > 0 and log['x'] > self.screenW:
                log['x'] = -log['length']
            elif log['dir']< 0 and log['x'] < 0 - log['length']:
                log['x'] = self.screenW

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
        for log in self.logs:
            pygame.draw.rect(self.win, (200, 190, 140), (log['x'], log['y'], log['length'], self.log_height))
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

            self.log()
            self.truck(frog_rect)
            self.redraw()

            if self.frog.y <= 0:
                self.frog.win_game()

            for log in self.logs:
                log_rect = pygame.Rect(log['x'], log['y'],log['length'], self.log_height)
                if log_rect.colliderect(frog_rect):
                    self.frog.x += log['dir']
    
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()