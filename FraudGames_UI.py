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
    screen.blit(background, (w // 12, h // 9))
    pygame.display.flip()
    font = pygame.font.Font('Roboto-Black.ttf', 40)
    text = font.render('Do you want to be a a fraduster (a) or a fighter (b)', True, red)
    textRect = text.get_rect()
    textRect.center = (w // 2, h // 2)
    screen.blit(text, textRect)
    font = pygame.font.Font('Roboto-Black.ttf', 30)
    text = font.render('click a or b', True, green)
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    fraud1()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    game_loop2()
                #event function to handle mouse clicks
        pygame.quit()
    
    menu_loop()

def fraud1():
    pygame.init()
    background = pygame.image.load('title.png')
    background_colour = gray
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    w, h = pygame.display.get_surface().get_size()
    pygame.display.set_caption('Fraud Games')
    screen.fill(background_colour)
    screen.blit(background, (w // 12, h // 9))
    pygame.display.flip()
    font = pygame.font.Font('Roboto-Black.ttf', 30)
    text = font.render('You are one of the top financial managers at Play the Game Inc. /nYou just recently experienced a rise in the price of your rent at your apartment complex.  /nYou could pitch a fraud scheme to a vendor that you know to overcharge for their products, /n and you will give them the profit from this fraud.', True, red)
    textRect = text.get_rect()
    textRect.center = (w // 2, h // 2)
    screen.blit(text, textRect)
    font = pygame.font.Font('Roboto-Black.ttf', 30)
    text = font.render('click a or b', True, green)
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    game_loop1()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    game_loop2()
                #event function to handle mouse clicks
        pygame.quit()
    
    menu_loop()

menu()
