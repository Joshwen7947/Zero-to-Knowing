from pygame import *

FPS = 30
WIDTH = 700
HEIGHT = 500
plane_x = 100
plane_y = 300
speed = 10

screen = display.set_mode((WIDTH,HEIGHT))
display.set_caption("Fly Me")
clock = time.Clock()
background = transform.scale(image.load("desert.png"),(WIDTH,HEIGHT))
airplane = transform.scale(image.load("airplane.png"))

run = True
while run:
    screen.blit(background,(0,0))
    screen.blit(airplane,(plane_x,plane_y))
    for e in event.get():
        if e.type == QUIT:
            quit()
            run = False
    
    keys = key.get_pressed()
    if keys[K_LEFT] and plane_x > 5:
        plane_x -= speed
    if keys[K_RIGHT] and plane_x < WIDTH-200:
        plane_x += speed
        
    if keys[K_UP] and plane_y > 5:
        plane_y -= speed
    if keys[K_DOWN] and plane_y < HEIGHT -100:
        plane_y += speed
    
    display.update()
    clock.tick(FPS)