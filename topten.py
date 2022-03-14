import pygame
import sys
import pygame_gui


pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                         text='Say Hello',
                                         manager=manager)

clock = pygame.time.Clock()
POS_X = 0
POS_Y = 0
count = 0

is_running = True

while is_running:
 time_delta = clock.tick(60)/1000.0
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         is_running = False

     if event.type == pygame_gui.UI_BUTTON_PRESSED:
          if event.ui_element == hello_button:


              while count < 10:
                       pygame.draw.rect(background,pygame.Color("#FFFFFF"),pygame.Rect((POS_X,POS_Y),(200,75)))
                       # print(count)
                       count+=1
                       POS_Y+=80


     manager.process_events(event)

 manager.update(time_delta)

 window_surface.blit(background, (0, 0))
 manager.draw_ui(window_surface)


 pygame.display.update()
