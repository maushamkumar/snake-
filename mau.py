
import pygame 
from pygame.locals import *
import time

# Using OOP we are making a snake
class Snake:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load("Daco_1444224.png").convert()
        self.x = 100
        self.y = 100
        self.direction = 'down'
     
    # This method helps snake to move left   
    def move_left(self):
        self.direction = "left"
    # This method helps snake to move right   
    def move_right(self):
        self.direction = 'right'
    
    # This method helps snake to move up     
    def move_up(self):
        self.direction = "up"
     
    # This method helps snake to move down   
    def move_down(self):
        self.direction = 'down'
       
    # We create a method to move snake using keyboard
    # Let's call it walk function
    # which direction you want to move 
    def walk(self):
        if self.direction =='left':
            self.x = self.x - 10
        if self.direction =='right':
            self.x = self.x + 10
        if self.direction =='up':
            self.y = self.y - 10
        if self.direction == 'down':
            self.y = self.y + 10
            
        self.draw()
        
    # This method draw a block and display it   
    def draw(self):
        self.parent_screen.fill((110,110,5))
        
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
        

# This method to play game you know right      
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((100, 100, 5))
        self.snake = Snake(self.surface)
        self.snake.draw()
        
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        
                    if event.key == K_LEFT:
                        self.snake.move_left()
                        
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        
                    if event.key == K_UP:
                        self.snake.move_up()
                        
                    if event.key == K_DOWN:
                        self.snake.move_down()
                        
                elif event.type == QUIT:
                    running = False
                    
            self.snake.walk()
        time.sleep(.2)
        
if __name__ == '__main__':
    # We don't wnat to much code in my method
    game = Game()
    game.run()