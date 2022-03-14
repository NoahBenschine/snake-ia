import pygame
import sys
import pygame_gui





pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))
leaderboard_container = pygame.Rect((100,100),(400,350))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))
#pygame_gui.core.interfaces.container_interface.IContainerLikeInterface
hello_button = pygame_gui.elements.ui_vertical_scroll_bar.UIVerticalScrollBar(relative_rect=pygame.Rect((400,0), (50, 50)),
                                         visible_percentage=.5,
                                         manager=manager,
                                         parent_element=leaderboard_container,
                                         object_id="scrollbar")

clock = pygame.time.Clock()
is_running = True

while is_running:
 time_delta = clock.tick(60)/1000.0
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         is_running = False

     manager.process_events(event)

 manager.update(time_delta)

 window_surface.blit(background, (0, 0))
 manager.draw_ui(window_surface)


 pygame.display.update()
