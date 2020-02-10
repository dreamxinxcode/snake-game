import pygame
import sys 
import random 
import time


# class Snake():
#     def __init__(self):



# class Food():
#      def __init__(self):

dimensions = (700, 400)
black = [0, 0, 0]
white = [255, 255, 255]

pygame.init()
canvas = pygame.display.set_mode(dimensions)
canvas.fill(white)
pygame.display.set_caption('Snake Game')
pygame.display.flip()



if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
