import pygame
import time

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0,0, 128)
red = (200, 0, 0)
light_red = (255, 0, 0)
black = (0, 0, 0)
gray = (128, 128 ,128)

def menu():
    pygame.init()
    background = pygame.image.load('title.png')
    background_colour = gray
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    w, h = pygame.display.get_surface().get_size()
    pygame.display.set_caption('Fraud Games')
    screen.fill(background_colour)
    screen.blit(background, (w // 17, h // 17))
    pygame.display.flip()
    font = pygame.font.Font('Roboto-Black.ttf', 90)
    text = font.render('IS CODY GAY', True, red)
    textRect = text.get_rect()
    textRect.center = (w // 2, h // 2)
    screen.blit(text, textRect)
    font = pygame.font.Font('Roboto-Black.ttf', 30)
    text = font.render('type y or n', True, green)
    textRect = text.get_rect()
    textRect.center = (w // 2, h // 1.65)
    screen.blit(text, textRect)
    font = pygame.font.Font('Roboto-Black.ttf', 30)
    text = font.render('Click ESC to exit', True, green)
    textRect = text.get_rect()
    textRect.center = (w // 2, h // 1.5)
    screen.blit(text, textRect)
    pygame.display.update()
    def menu_loop():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                #adding jump to next loop
                if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    game_loop1()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                    game_loop2()
                #event function to handle mouse clicks
        pygame.quit()
    
    menu_loop()

def game_loop1():
    background = pygame.image.load('title.png')
    background_colour = gray
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    w, h = pygame.display.get_surface().get_size()
    #changed colors and generated fixed resolution backround scene
    pygame.display.set_caption('Fraud Games')
    screen.fill(background_colour)
    screen.blit(background, (w // 17, h // 17))
    pygame.display.flip()
    #text displays and rendering
    font = pygame.font.Font('Roboto-Black.ttf', 90)
    text = font.render('You Right', True, red)
    textRect = text.get_rect()
    textRect.center = (w // 2, h // 2)
    screen.blit(text, textRect)
    font = pygame.font.Font('Roboto-Black.ttf', 30)
    text = font.render('Click ESC to exit', True, green)
    textRect = text.get_rect()
    textRect.center = (w // 2, h // 1.65)
    screen.blit(text, textRect)
    pygame.display.update()
    #sound playback loads sounds and converts any effects into variables to be used on a later line
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
    menu()

def game_loop2():
    background = pygame.image.load('title.png')
    background_colour = gray
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    w, h = pygame.display.get_surface().get_size()
    #changed colors and generated fixed resolution backround scene
    pygame.display.set_caption('Fraud Games')
    screen.fill(background_colour)
    screen.blit(background, (w // 17, h // 17))
    pygame.display.flip()
    #text displays and rendering
    font = pygame.font.Font('Roboto-Black.ttf', 90)
    text = font.render('You Wrong', True, red)
    textRect = text.get_rect()
    textRect.center = (w // 2, h // 2)
    screen.blit(text, textRect)
    font = pygame.font.Font('Roboto-Black.ttf', 30)
    text = font.render('Click ESC to exit', True, green)
    textRect = text.get_rect()
    textRect.center = (w // 2, h // 1.65)
    screen.blit(text, textRect)
    pygame.display.update()
    #sound playback loads sounds and converts any effects into variables to be used on a later line
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
    menu()
    
menu()
