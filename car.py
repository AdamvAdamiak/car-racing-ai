import pygame
import math

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.angle = 0
        # self.img = pygame.image.load("assets/car.png")
        self.front_x = self.x + 16 + 16 * math.sin(math.radians(self.angle))
        self.back_x = self.x + 16 - 16 * math.sin(math.radians(self.angle))
        self.front_y = self.y + 16 + 16 * math.cos(math.radians(self.angle))
        self.back_y = self.y + 16 - 16 * math.cos(math.radians(self.angle))
        self.laps = 0

    def move(self):
        self.x = self.x + math.sin(math.radians(self.angle))*self.vel
        self.y = self.y + math.cos(math.radians(self.angle))*self.vel

    def accelerate(self):
        if self.vel < 15:
            self.vel += 0.5

    def decelerate(self):
        if self.vel > 1:
            self.vel -= 0.5

    def turn_right(self):
        if self.vel > 0:
            self.angle -= 2 + self.vel*0.3
            if self.angle < 0:
                self.angle += 360

    def turn_left(self):
        if self.vel > 0:
            self.angle += 2 + self.vel*0.3
            if self.angle > 360:
                self.angle -= 360