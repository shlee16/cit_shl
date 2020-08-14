import pygame as pg

pg.init()

display_width = 800
display_height = 600
car_width = 128
car_height = 128

gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('racey')

white = (255,255,255)

crashed = False
carImg = pg.image.load('images/car.png')


x = (display_width * 0.45)
y = (display_height * 0.5)
x_change = 0
y_change = 0
car_health = 10

def message(text_content, text_x, text_y, text_font, text_size, text_color):
    text = pg.font.Font(text_font, text_size)
    textSurf = text.render(text_content, True, text_color)
    textRect = textSurf.get_rect()
    textRect.center = (text_x, text_y)
    gameDisplay.blit(textSurf, textRect)


while not crashed:
    eventlist = pg.event.get()
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    print(click)
    # print(mouse)

    for event in eventlist:
        if event.type == pg.QUIT:
            crashed = True
        # print(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x_change = -5
            elif event.key == pg.K_RIGHT:
                x_change = 5
            elif event.key == pg.K_UP:
                y_change = -5
            elif event.key == pg.K_DOWN:
                y_change = 5
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT :
                x_change = 0
            if event.key == pg.K_UP or event.key == pg.K_DOWN :
                y_change = 0

##
    x += x_change # x = x + x_change
    y += y_change
    buttonColor = (0,255,0)

    if x > display_width - car_width or x < 0:
        # x -= x_change # x = x - x_change
        x = display_width/2
        car_health -= 1
    if y > display_height - car_height or y < 0:
        # y -= y_change
        y = display_height/2
        car_health -= 1

    if 600 < mouse[0] and mouse[0]<700 and 100<mouse[1] and 150>mouse[1]:
        buttonColor = (100, 255, 100)
        if click[2] :
            car_health = 10


    gameDisplay.fill(white)
    gameDisplay.blit(carImg, (x,y))
    message( str(car_health ), x + 64, y - 15, "freesansbold.ttf", 30, (0,0,0))
    pg.draw.rect(gameDisplay, buttonColor , (600,100,100,50))
    message( "Revive!", 650, 125, "freesansbold.ttf", 20, (0,0,0))


    pg.display.update()
