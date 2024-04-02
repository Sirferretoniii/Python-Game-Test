# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

circlepos = pygame.Vector2(screen.get_width() * 0.25,screen.get_height() / 2)
circlevel = 1
jumpvel = 10
gravity = 1

firstclicked = False
Clicked = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
        if not firstclicked:
            firstclicked = True
            Clicked = True
            circlevel = -jumpvel
    if firstclicked:
        if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
            if Clicked == False:
                Clicked = True
                circlevel = -jumpvel
        else:
            Clicked = False
            circlevel += gravity
        circlepos.y += circlevel
    pygame.draw.circle(screen, pygame.Color("yellow"), circlepos, 40)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()