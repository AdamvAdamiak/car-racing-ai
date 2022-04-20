import pygame
import math
import matplotlib.pyplot as plt


class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.angle = 90
        self.img = pygame.image.load("assets/car.png")
        self.front_x = self.x + 16 + 16 * math.sin(math.radians(self.angle))
        self.back_x = self.x + 16 - 16 * math.sin(math.radians(self.angle))
        self.front_y = self.y + 16 + 16 * math.cos(math.radians(self.angle))
        self.back_y = self.y + 16 - 16 * math.cos(math.radians(self.angle))
        self.laps = 0
        self.points = 0
        self.latest_move = ''
        self.isAlive = True

    def move(self, i=1):
        for x in range(i):
            self.x = self.x + math.sin(math.radians(self.angle))*self.vel
            self.y = self.y + math.cos(math.radians(self.angle))*self.vel
            self.latest_move = 'move'

    def accelerate(self, i=1):
        for x in range(i):
            if self.vel < 15:
                self.vel += 0.5

    def decelerate(self, i=1):
        for x in range(i):
            if self.vel > 1:
                self.vel -= 0.5

    def turn_right(self, i=1):
        for x in range(i):
            if self.vel > 0:
                self.angle -= 2 + self.vel*0.3
                if self.angle < 0:
                    self.angle += 360
        self.latest_move = 'turn_right'

    def turn_left(self, i=1):
        for x in range(i):

            if self.vel > 0:
                self.angle += 2 + self.vel*0.3
                if self.angle > 360:
                    self.angle -= 360
        self.latest_move = 'turn_left'

    def get_ends(self):
        self.front_x = self.x + 16 + 16*math.sin(math.radians(self.angle))
        self.back_x = self.x + 16 - 16*math.sin(math.radians(self.angle))
        self.front_y = self.y + 16 + 16*math.cos(math.radians(self.angle))
        self.back_y = self.y + 16 - 16*math.cos(math.radians(self.angle))
        return self.front_x, self.back_x, self.front_y, self.back_y

    def draw(self, screen):
        rotated_img = pygame.transform.rotate(self.img, self.angle)
        new_rect = rotated_img.get_rect(
            center=self.img.get_rect(topleft=(self.x, self.y)).center)
        screen.blit(rotated_img, new_rect.topleft)
