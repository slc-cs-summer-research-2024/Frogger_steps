#logs can have frog jump on them and moves frog 

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

    log_length = 600/5
    log_height = 45
    logs = [{'x': 200, 'y': 50,'dir': 1},{'x': 200-log_length*2, 'y': 50,'dir': 1},{'x': 200- log_length*4, 'y': 50,'dir': 1}
              ,{'x': 400, 'y': 100,  'dir': -1},{'x': 400+ log_length*2, 'y': 100, 'dir': -1},{'x': 400+ log_length*4, 'y': 100 , 'dir': -1}
              ,{'x': 100, 'y': 150, 'dir': 1},{'x': 100 + log_length*2, 'y': 150, 'dir': 1},{'x': 100+ log_length*4, 'y':150, 'dir': 1}
            ,{'x': 300, 'y':200,'dir': -1},{'x': 300+ log_length*2, 'y': 200,'dir': -1},{'x': 300+ log_length*4, 'y': 200,'dir': -1}]

    truck_length = 600/ 5
    truck_height = 30
    trucks = [{'x': 200, 'y': 585,'dir': 1},{'x': 200-truck_length*2, 'y': 585,'dir': 1},{'x': 200- truck_length*4, 'y': 585,'dir': 1}
              ,{'x': 400, 'y': 395,  'dir': -1},{'x': 400+ truck_length*2, 'y': 395 , 'dir': -1},{'x': 400+ truck_length*4, 'y': 395 , 'dir': -1}
              ,{'x': 100, 'y': 465, 'dir': 1},{'x': 100 + truck_length*2, 'y': 465, 'dir': 1},{'x': 100+ truck_length*4, 'y': 465, 'dir': 1}
            ,{'x': 300, 'y': 655,'dir': -1},{'x': 300+ truck_length*2, 'y': 655,'dir': -1},{'x': 300+ truck_length*4, 'y': 655,'dir': -1}]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        frog_x, frog_y = move(keys, frog_x, frog_y, frog_speed, screenW, screenH, frog_size,logs,log_length,log_height)
        frog_rect = pygame.Rect(frog_x, frog_y, frog_size, frog_size)
        
        log(logs,screenW,log_length)
        truck(trucks, truck_length, screenW,frog_rect,truck_height)
        redraw(win, frog_x, frog_y, frog_size,trucks, truck_length, truck_height,logs,log_length,log_height)
        if frog_y == 0:
            win_game()
    pygame.quit()

def log(logs,screenW,log_length):
    for log in logs:
        log['x'] +=log['dir']
        if log['dir'] == 1 and log['x'] > screenW:
            log['x'] = - log_length
        elif log['dir'] == -1 and log['x'] < 0 -log_length:
            log['x'] = screenW 
        




def truck(trucks, truck_length, screenW,frog_rect,truck_height):
    for truck in trucks:
        truck['x'] += truck ['dir']
        if truck['dir'] == 1 and truck['x'] > screenW:
            truck['x'] = - truck_length
        elif truck['dir'] == -1 and truck['x'] < 0 -truck_length:
            truck['x'] = screenW 
        truck_rect = pygame.Rect(truck['x'],truck['y'],truck_length,truck_height)
        if truck_rect.colliderect(frog_rect):
            death()
        
def death():
    print("Game Over!")
    pygame.time.delay(2000)  
    pygame.quit()
    quit() 

def win_game():
    print("Winner!")
    pygame.time.delay(2000)  
    pygame.quit()
    quit() 
    

def move(keys, frog_x, frog_y, frog_speed, screenW, screenH, frog_size,logs,log_length,log_height):
    if keys[pygame.K_RIGHT]and frog_x < screenW - frog_size:
        frog_x += frog_speed
    elif keys[pygame.K_LEFT] and frog_x > 0:
        frog_x -= frog_speed
    elif keys[pygame.K_UP] and frog_y > 0:
        frog_y -= frog_speed
    elif keys [pygame.K_DOWN] and frog_y < screenH - frog_size:
        frog_y += frog_speed
    for log in logs:
        log_rect = pygame.Rect(log['x'], log['y'], log_length, log_height)
        if log_rect.colliderect(pygame.Rect(frog_x, frog_y, frog_size, frog_size)):
            frog_x += log['dir']
    return frog_x, frog_y


def redraw(win, frog_x, frog_y, frog_size,trucks, truck_length, truck_height,logs,log_length,log_height):
    win.fill("black")
    
    for truck in trucks:
        pygame.draw.rect(win,('red'), (truck['x'],truck['y'],truck_length,truck_height))
    for log in logs:
        pygame.draw.rect(win,(200,190,140),(log['x'],log['y'],log_length,log_height))
    pygame.draw.rect(win, ('green'), (frog_x, frog_y, frog_size, frog_size))
    pygame.display.update ()


if __name__ == "__main__":
    game()

