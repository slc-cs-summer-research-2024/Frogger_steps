#water that kills frog if not on logs
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
        self.screenW = 600
        self.screenH = 800
        self.win = pygame.display.set_mode((self.screenW, self.screenH))
        pygame.display.set_caption("Frogger")

        self.frog_size = 25
        self.frog_speed = 2
        self.frog = Player(self.screenW // 2, self.screenH - self.frog_size, self.frog_size, self.frog_speed)

        self.log_per_row = 4
        self.log_rownum = 7
        self.logs_startY = 50
        self.LOG_SPEED = 1
        self.log_length = self.screenW /  (self.log_per_row + (self.log_per_row -1))
        self.water_size = 270
        self.vert_btw_logs = self.frog_size / 5
        self.log_height = self.water_size / self.log_rownum
        self.logs = self.create_logs()

        self.water = pygame.Rect(0, self.logs_startY, self.screenW, self.water_size + ((self.frog_size / 5) * (self.log_rownum - 1)))

        self.trucks_per_row = 3
        self.truck_rownum = 4
        self.truck_startY = 400
        self.TRUCK_SPEED = 1
        self.truck_length = self.screenW / (self.trucks_per_row + (self.trucks_per_row -1))
        self.truck_height = 30
        self.vert_btw_trucks = self.frog_size * 1.5
        self.trucks = self.create_trucks()

    def create_logs(self):
        logs = []
        dir = 1
        y_pos = self.logs_startY
        x_pos = 0 
        for i in range(self.log_per_row * self.log_rownum):
            logs.append({'x': x_pos, 'y': y_pos, 'dir': dir * self.LOG_SPEED})
            x_pos += (self.log_length * 2)
            if (i + 1) % self.log_per_row == 0: 
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
            trucks.append({'x': x_pos, 'y': y_pos, 'dir': dir * self.TRUCK_SPEED})
            x_pos += ( self.truck_length *2)
            if (i + 1) % self.trucks_per_row == 0: 
                x_pos = 0 
                dir = dir * -1
                y_pos += (self.truck_height + self.vert_btw_trucks)
        return trucks

    def log(self):
        for log in self.logs:
            log['x'] += log['dir']
            if log['dir'] > 0 and log['x'] > self.screenW:
                log['x'] = -self.log_length
            elif log['dir']< 0 and log['x'] < 0 - self.log_length:
                log['x'] = self.screenW

    def truck(self, frog_rect):
        for truck in self.trucks:
            truck['x'] += truck['dir']
            if truck['dir'] > 0 and truck['x'] > self.screenW:
                truck['x'] = -self.truck_length
            elif truck['dir'] < 0 and truck['x'] < 0 - self.truck_length:
                truck['x'] = self.screenW
            truck_rect = pygame.Rect(truck['x'], truck['y'], self.truck_length, self.truck_height)
            if truck_rect.colliderect(frog_rect):
                self.frog.death()

    def redraw(self):
        self.win.fill("black")
        pygame.draw.rect(self.win, 'blue', self.water)
        for truck in self.trucks:
            pygame.draw.rect(self.win, 'red', (truck['x'], truck['y'], self.truck_length, self.truck_height))
        for log in self.logs:
            pygame.draw.rect(self.win, (200, 190, 140), (log['x'], log['y'], self.log_length, self.log_height))
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

            if self.frog.y == 0:
                self.frog.win_game()

            on_log = False
            for log in self.logs:
                log_rect = pygame.Rect(log['x'], log['y'], self.log_length, self.log_height)
                if log_rect.colliderect(frog_rect):
                    on_log = True
                    self.frog.x += log['dir']
            if self.logs_startY <= self.frog.y <= self.water_size and not on_log:
                self.frog.death()
    
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()