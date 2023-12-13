# Build a screen and a moving block 

# first we gonna import pygame
import pygame
# we also need pygame.locals import everything
from pygame.locals import *

def draw_block():
    # fill the background using fill((110, 110, 5)) you can use any color
    # This code will create a bolck whenever I want i can call the block 
    surface.fill((110, 110, 5))  # To clear 
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()
    
if __name__ == '__main__':
    pygame.init()  # To intilize the whole model
    
    surface = pygame.display.set_mode((500, 500))  # set_mode initilize your game window and how big size you want and many more thing  
    surface.fill((100, 110, 5))  # This will fill the color and whatever color you want you can add here to use rgb color on google 
    
    block = pygame.image.load("Daco_1444224.png").convert()  # This is code to upload an image
    
    block_x, block_y = 100, 100
    
    surface.blit(block,(block_x, block_y))  # TO draw that image use blit function
    
    pygame.display.flip()  # To update your game either you use flip() or update()
    
    # Create a event loop 
    # However it look like while True but here is a catch if want to escape the set some key whatever you want 
    running = True
    
    while running:
        # pygame.event.get code allow us to do all kind of event 
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key ==K_ESCAPE:  # When you use Escape button then also you escape the game
                    running = False
                if event.key == K_LEFT: # To move left side 
                    block_x = block_x - 10
                    draw_block()
                    
                if event.key == K_RIGHT:  # To move right side 
                    block_x = block_x + 10
                    draw_block()
                    
                if event.key == K_UP:  # To move your block up and you can change how much move 
                    block_y = block_y - 10
                    draw_block()
                    
                if event.key == K_DOWN:  # To move down 
                    block_y = block_y + 10 
                    draw_block()
                    
                elif event.type == QUIT:  # we use click to cancle buttom that time it will quit 
                    running = False