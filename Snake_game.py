# Moving block with a timer 
# This time we make the same in OOP so we can use anywhere easily
import pygame
from pygame.locals import *

# Using OOP we are makeing a snake
class Snake:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load("Daco_1444224.png").convert()
        self.x = 100
        self.y = 100
    
    # This method helps snake to move left   
    def move_left(self):
        self.x = self.x - 10
        self.draw()
    # This method helps snake to move right    
    def move_right(self):
        self.y = self.y + 10
        self.draw()
    # This method helps snake to move up    
    def move_up(self):
        self.y = self.y + 10
        self.draw()
    # This method helps snake to move down    
    def move_down(self):
        self.y = self.y + 10 
        self.down()
        
        
    # This method draw a block and display it  
    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
        
        
# This method to play game you know right           
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface)
        self.snake.draw()
        
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type ==KEYDOWN:
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

if __name__ == '__main__':
    game = Game()
    game.run()