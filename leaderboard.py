import pygame
import sys
import pygame_gui
import DB





fps = pygame.time.Clock()

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

def start_leaderboard(score,leaderboard_surface,new_game):
    leaderboard_surface.fill('#000000')
    manager = pygame_gui.UIManager((800, 600))
    leaderboard_container = pygame.Rect((300,100),(250,250))
    active = False
    is_running = True
    tagInput = True
    if tagInput:
       pygame.draw.rect(leaderboard_surface,pygame.Color("#FFFFFF"),leaderboard_container)
       check_leaderboard = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 100), (150, 30)),
                                                text='Leaderboard',
                                                manager=manager)
       start_new_game = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 100), (100, 30)),
                                                text='New Game',
                                                manager=manager,)

       my_font = pygame.font.SysFont('times new roman', 25)

       # creating a text surface on which text
       # will be drawn
       game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

       # create a rectangular object for the text
       # surface object
       game_over_rect = game_over_surface.get_rect()

       # setting position of the text
       game_over_rect.midtop = (400,200)

       # blit will draw the text on screen
       leaderboard_surface.blit(game_over_surface, game_over_rect)
       pygame.display.flip()

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



     time_delta = fps.tick(60)/1000.0
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
                  start_new_game.visible = 1
                  check_leaderboard.set_position((300,70))
                  start_new_game.set_position((450,70))
                  check_leaderboard.set_text("Input Score")
                  leaderboard_surface.fill('#000000') # Fill the entire screen with black
                  while count < 10:
                      if len(topten)-1 >= count:
                          text_surface = base_font.render("#"+str(count+1)+"  "+str(topten[count][1]), True, ('#000000'))
                      else:text_surface = base_font.render("No score", True, ('#000000'))

                      score_rect = pygame.Rect((300,POS_Y),(250,25))
                      pygame.draw.rect(leaderboard_surface,pygame.Color("#FFFFFF"),score_rect)
                      leaderboard_surface.blit(text_surface, (score_rect.x+5, score_rect.y+5))
                      print(count)
                      count+=1
                      POS_Y+=26
                else:
                    tagInput = True
                    leaderboard_surface.fill('#000000') # Fill the entire screen with black
                    check_leaderboard.set_position((300,100))
                    pygame.draw.rect(leaderboard_surface,pygame.Color("#FFFFFF"),leaderboard_container)
              if event.ui_element == start_new_game:
                  leaderboard_surface.fill('#000000')
                  new_game()





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
                 DB.insertScore(score,tag_id)
                 print(DB.getTagID(user_text))

             # Unicode standard is used for string
             # formation
             else:
                 user_text += event.unicode

         manager.process_events(event)
     if(tagInput):
       pygame.draw.rect(leaderboard_surface, color, input_rect)

     text_surface = base_font.render(user_text, True, (255, 255, 255))

     # render at position stated in arguments
     leaderboard_surface.blit(text_surface, (input_rect.x+5, input_rect.y+5))

     # set width of textfield so that text cannot get
     # outside of user's text input
     input_rect.w = max(100, text_surface.get_width()+10)


     # it will set leaderboard_surface color of screen

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
     fps.tick(60)
     manager.update(time_delta)

     leaderboard_surface.blit(leaderboard_surface, (0, 0))
     manager.draw_ui(leaderboard_surface)
     pygame.display.update()
