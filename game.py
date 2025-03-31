# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 
def init_game (): 
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True

def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here

   # -- Set Position Of Graphic -- #
   background_position = [0,0]

   # -- Load and Set Up Graphic -- #
   background_image = pygame.image.load("C:\move-spaceship-images\saturn_family1.jpg").convert()
   player_image = pygame.image.load("C:\move-spaceship-images\player.png").convert()
   player_image.set_colorkey(config.BLACK)

   running = True
   while running:
      running = handle_events()
      screen.fill(config.WHITE) # Use color from config

      # -- Copy Image -- # 
      screen.blit(background_image, background_position)

      # -- get Current Mouse "Pos", this returens the "pos" as a list of two numbers -- #
      player_position = pygame.mouse.get_pos() 
      x = player_position[0] 
      y = player_position[1]

      # -- Copy Image to Screen -- # 
      screen.blit(player_image, [x-50, y-50])

      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()