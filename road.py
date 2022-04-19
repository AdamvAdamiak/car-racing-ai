from turtle import circle
import matplotlib.pyplot as plt
import math
import numpy as np


def circle_function(x, r):
    return np.sqrt(-x**2+r**2)


class Road:
    def __init__(self, r_inline, r_outline) -> None:

        if r_inline > r_outline:
            print('Error, r_inline must be higher than r_outline')
            exit()

        self.r_inline = r_inline
        self.r_outline = r_outline

        self.x_inline = np.linspace(-r_inline, r_inline, 1000)
        self.x_outline = np.linspace(-r_outline, r_outline, 1000)

    def create_inline(self):
        self.y_inline = circle_function(self.x_inline, self.r_inline)

    def create_outline(self):
        self.y_outline = circle_function(self.x_outline, self.r_outline)

    def draw_road(self):

        self.create_inline()
        self.create_outline()

        plt.plot(self.x_inline, self.y_inline, 'b')
        plt.plot(self.x_inline, -self.y_inline, 'b')

        plt.plot(self.x_outline, self.y_outline, 'b')
        plt.plot(self.x_outline, -self.y_outline, 'b')

        plt.show()


if __name__ == '__main__':

    road = Road(10, 15)
    road.draw_road()
