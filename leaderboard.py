import pygame
import sys
import pygame_gui
import DB
pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
leaderboard_container = pygame.Rect((300,100),(200,250))
manager = pygame_gui.UIManager((800, 600))

active = False
clock = pygame.time.Clock()
is_running = True
tagInput = True

if tagInput:
   pygame.draw.rect(background,pygame.Color("#FFFFFF"),leaderboard_container)
   check_leaderboard = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 100), (150, 30)),
                                            text='Leaderboard',
                                            manager=manager)

   base_font = pygame.font.Font(None, 32)
   user_text = ''

   # create rectangle
   input_rect = pygame.Rect((350, 300), (100, 40))
   input_rect.clamp(leaderboard_container)
   # color_active stores color(lightskyblue3) which
   # gets active when input box is clicked by user
   color_active = pygame.Color('lightskyblue3')

   # color_passive store color(chartreuse4) which is
   # color of input box.
   color_passive = pygame.Color('chartreuse4')
   color = color_passive

while is_running:



 time_delta = clock.tick(60)/1000.0
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         is_running = False
         pygame.quit()
         sys.exit()

     if event.type == pygame_gui.UI_BUTTON_PRESSED:
          if event.ui_element == check_leaderboard:
            if tagInput:
              print("was clicked")
              count = 0
              POS_Y = 100
              topten = DB.getScores()
              print(topten)
              print(topten[0][1])

              tagInput = False
              new_rect = pygame.Rect((350, 50), (50, 50))
              check_leaderboard.set_position((300,70))
              check_leaderboard.set_text("Input Score")
              background.fill('#000000') # Fill the entire screen with black
              while count < 10:
                  if len(topten)-1 >= count:
                      text_surface = base_font.render("#"+str(count+1)+"  "+str(topten[count][1]), True, ('#000000'))
                  else:text_surface = base_font.render("No score", True, ('#000000'))

                  score_rect = pygame.Rect((300,POS_Y),(200,25))
                  pygame.draw.rect(background,pygame.Color("#FFFFFF"),score_rect)
                  background.blit(text_surface, (score_rect.x+5, score_rect.y+5))
                  print(count)
                  count+=1
                  POS_Y+=26
            else:
                tagInput = True
                background.fill('#000000') # Fill the entire screen with black
                check_leaderboard.set_position((300,100))
                pygame.draw.rect(background,pygame.Color("#FFFFFF"),leaderboard_container)




     if event.type == pygame.MOUSEBUTTONDOWN:
         if input_rect.collidepoint(event.pos):
             active = True
         else:
             active = False

     if event.type == pygame.KEYDOWN:

         # Check for backspace
         if event.key == pygame.K_BACKSPACE:

             # get text input from 0 to -1 i.e. end.
             user_text = user_text[:-1]
         elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
             DB.insertTag(user_text)
             tag_id = DB.getTagID(user_text)
             DB.insertScore(5,tag_id)
             print(DB.getTagID(user_text))

         # Unicode standard is used for string
         # formation
         else:
             user_text += event.unicode

     manager.process_events(event)
 if(tagInput):
   pygame.draw.rect(background, color, input_rect)

 text_surface = base_font.render(user_text, True, (255, 255, 255))

 # render at position stated in arguments
 background.blit(text_surface, (input_rect.x+5, input_rect.y+5))

 # set width of textfield so that text cannot get
 # outside of user's text input
 input_rect.w = max(100, text_surface.get_width()+10)


 # it will set background color of screen

 if active:
     color = color_active
 else:
     color = color_passive

 # draw rectangle and argument passed which should
 # be on screen


 # display.flip() will update only a portion of the
 # screen to updated, not full area
 # pygame.display.flip()

 # clock.tick(60) means that for every second at most
 # 60 frames should be passed.
 clock.tick(60)
 manager.update(time_delta)

 window_surface.blit(background, (0, 0))
 manager.draw_ui(window_surface)
 pygame.display.update()
