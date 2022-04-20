import matplotlib.pyplot as plt
import numpy as np
import pygame
from sqlalchemy import true
from PIL import Image


def circle_function(x, r):
    return np.sqrt(-x**2+r**2)


class Road:
    def __init__(self) -> None:

        self.img = Image.open("assets/road.jpg")

    def draw_road(self, screen):
        img = pygame.image.load("assets/road.jpg")

        self.screen = screen
        self.screen.blit(img, (0, 0))

    def collide(self, car):
        # Getting the pixel in the front and back of the car, then looking if it's red or green pixel and if true
        # return True
        front_x, back_x, front_y, back_y = car.get_ends()
        r, g, b, *a = self.img.getpixel((front_x, front_y))
        r2, g2, b2, *a = self.img.getpixel((back_x, back_y))
        #print(self.track.getpixel((front_x, front_y)))
        if (r > 155 and b < 100) or (r2 > 155 and b2 < 100) or (g > 155 and b < 100) or (g2 > 155 and b < 100):
            #print("Collided: , "+ str(r) + "  " + str(g) + "  " + str(b))
            if r < 50 and b < 50 and g < 50:
                return False
            return True
        #print("Not collided")
