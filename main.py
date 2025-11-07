import pygame
from constants import *
from logger import log_state





def main():

    pygame.init()


    #print("Starting Asteroids!")
    #print("Screen width: 1280")
    #print(F"Screen height: 720")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    
    running = True
    while running:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
         
        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Update the display to show the changes
        pygame.display.flip() # or pygame.display.update()

    #pygame.quit()




    

if __name__ == "__main__":
    main()
