import math
import pprint
import random

from ui_model.point import Point
from ui_model.street import Street
from ui_model.light_intensity import Intensity


class Person():

    def __init__(self, size, point: Point, street: Street, speed=None, color='black'):

        self.rand = random.Random()

        self.edge_offset = 0  # So that people do not walk next to the edge of the street
        self.x = point.x
        self.y = point.y
        self.street = street
        self.is_on_crossroad = street.isPointInCrossrRoad(point, self.edge_offset)

        self.size = size
        self.color = color
        self.speed = speed if speed is not None else self.rand.randint(-5, 6)

        self.move_x = self.speed if street.IsHorizontal else 0
        self.move_y = self.speed if street.IsVertiacal else 0
        self.circle = None
        self.anxiety_level = 0
        self.anxiety_tolerance = self.rand.uniform(0, 1)

    def move(self, canvas_width, canvas_heigh):
        entered_crossroad, crossing_road = self.street.isPointInCrossrRoad(Point(self.x, self.y),
                                                                           self.size + self.edge_offset)

        if entered_crossroad:
            if not self.is_on_crossroad:  # if person is already on crossroad, stick to previous decision they made
                self.entered_crossroad()
                self.is_on_crossroad = True
        else:
            if self.is_on_crossroad:
                self.is_on_crossroad = False  # left crossroad

        self.x = self.x + self.move_x
        self.y = self.y + self.move_y

        if self.y < self.size or self.x < self.size or self.x >= -self.size + canvas_width or self.y >= canvas_heigh - self.size:
            self.move_y = -self.move_y
            self.move_x = -self.move_x

    def entered_crossroad(self):
        probability = lambda: self.rand.randint(0, 1) == 1  # Person has 50% chance of crossing the road
        if True:
            if self.move_x != 0:  # moving horizontally => move vertically
                self.move_x = 0
                if probability():  # Person has 50% chance selecting top/bottom or left/right
                    self.move_y = -self.speed
                else:
                    self.move_y = self.speed
            elif self.move_y != 0:  # moving vertically => move horizontally
                self.move_y = 0
                if probability():  # Person has 50% chance selecting top/bottom or left/right
                    self.move_x = -self.speed
                else:
                    self.move_x = self.speed
            else:
                raise Exception("Person movement is STALE")
        # stay on the current road

    def calculate_anxiety(self, lights):
        # Very basic anxiety calculation is a linear inverse relationship with light-level at a given point.
        # If light level is 100%, then anxiety is 0%, if light-level is 47%, then anxiety is 53%, etc.
        # Maximum possible intensity from 1 light is 100 W * 117 lm/W = 11700 lm
        max_intensity = 11700
        lights_on_same_street = []
        anxiety_uniformity = 0
        light_minimum = 0

        lights_sorted_by_distance = sorted(lights, key=self.distance_between_2_points)

        i = Intensity(self.x, self.y, lights_sorted_by_distance[0], lights_sorted_by_distance[1])

        current_intensity = round(i.get_intensity())

        # 100 is max anxiety and 0 is no anxiety
        anxiety_lux = 100 - ((min(current_intensity, max_intensity) / max_intensity) * 100)

        for light in lights:
            if self.street.is_light_on_the_street(light):
                lights_on_same_street.append(light)

        # if light_minimum is 0 then a light is off on the street. Maybe not relevant
        # without vertical and horizontal lux calculations
        light_minimum = min([light.power for light in lights_on_same_street])

        # anxiety_uniformity is when lights are not the same brightness.
        # 100 is max anxiety and happens when a light is off; 0 is all lights are equally lit.
        if sum([light.power for light in lights_on_same_street]) != 0:
            anxiety_uniformity = 100 - (light_minimum / (
                        sum([light.power for light in lights_on_same_street]) / len(lights_on_same_street))) * 100

        return ((anxiety_lux * 0.9) + (anxiety_uniformity * 0.1)) * (1 - self.anxiety_tolerance)

    def distance_between_2_points(self, light):
        return math.sqrt(pow((light.x - self.x), 2) + pow((light.y - self.y), 2))
