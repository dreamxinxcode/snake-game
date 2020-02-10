import pygame
import sys 
import random 
import time


# class Snake():
#     def __init__(self):



# class Food():
#      def __init__(self):
       

canvas = pygame.display.set_mode((700, 400))

# FPS controller
fpsController = pygame.time.Clock()

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

