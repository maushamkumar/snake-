# Convert block into a snake
# Draw apple at random locations

import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,25)*SIZE
        self.y = random.randint(1,20)*SIZE

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("block.jpg").convert()
        self.direction = 'down'

        self.length = length
        self.x = [40]*length# This will create a length number of array
        self.y = [40]*length
    
    # This method helps snake to move left
    def move_left(self):
        self.direction = 'left'
    
    # This method helps snake to move right
    def move_right(self):
        self.direction = 'right'
        
    # This method helps snake to move up
    def move_up(self):
        self.direction = 'up'

    # This method helps snake to move down
    def move_down(self):
        self.direction = 'down'
        
# We create a method to move snake using keyboard
#     # Let's call it walk function
#     # which direction you want to move
# we have to change our movement because this we a snake and you first block will then second block take position of first block 
# That mean we have to run revese block
    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    # This method draw a block and display it 
    def draw(self):
        self.parent_screen.fill((110, 110, 5))

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        
# This method to play game you know right 
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface, 5)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()


    def play(self):
        self.snake.walk()
        self.apple.draw()

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

            self.play()

            time.sleep(.2)

if __name__ == '__main__':
    # We don't wnat to much code in my method
    game = Game()
    game.run()