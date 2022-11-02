import random

from ui_model.point import Point
from ui_model.street import Street


class Person():

    def __init__(self, size, point: Point, street: Street, color='black'):
        self.rand = random.Random()

        self.edge_offset = 0  # So that people do not walk next to the edge of the street
        self.x = point.x
        self.y = point.y
        self.street = street
        self.is_on_crossroad = street.isPointInCrossrRoad(point, self.edge_offset)

        self.size = size
        self.color = color
        self.speed = self.rand.randint(-5, 6)

        self.move_x = self.speed if street.IsHorizontal else 0
        self.move_y = self.speed if street.IsVertiacal else 0
        self.circle = None

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
