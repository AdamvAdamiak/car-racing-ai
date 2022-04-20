from car import Car
from road import Road
import pygame
import random


class Main:
    def __init__(self, cars):
        self.road = Road()
        # self.car = Car(330, 60)
        self.cars = cars

        self.rewards = {
            False: 10,
            True: -50
        }

        self.WIDTH = 600
        self.HEIGHT = 600

        self.init_pygame()

    def draw_road(self):
        self.road.draw_road(self.screen)

    # def draw_car(self):
        # self.car.draw(self.screen)

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill((255, 255, 255))
        self.draw_road()

    def run_pygame(self):
        running = True
        while running:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

            self.draw_road()
            self.update()

        pygame.quit()
        quit()

    def update(self):
        for car in self.cars:

            tmp = random.random()
            previous_points = car.points

            if tmp < 0.33:
                car.move()
            elif tmp > 0.66:
                car.turn_left()
            else:
                car.turn_right()

            boolean = self.road.collide(car)

            if boolean:
                car.points += self.rewards[True]
            else:
                car.points += self.rewards[False]

            if car.points < previous_points:
                if car.latest_move == 'turn_right':
                    car.turn_left(16)
                elif car.latest_move == 'turn_left':
                    car.turn_right(16)
            car.vel = 5
            car.draw(self.screen)

            print(car.x, car.y, car.points)


if __name__ == '__main__':
    cars = []
    for i in range(5):
        cars.append(Car(330, 60))
    main = Main(cars)
    main.run_pygame()
