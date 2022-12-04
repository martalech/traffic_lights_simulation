from ui_model.point import Point
from ui_model.crossroad import CrossRoad

class Street():
    def __init__(self, start_point:  Point, end_point: Point, isHorizontal) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.IsHorizontal = isHorizontal
        self.IsVertiacal = not isHorizontal
        self.crossroads= []
        self.lights = []

    def add_crossroad(self, crossRoad: CrossRoad):
        self.crossroads.append(crossRoad)
        
    def add_lights(self, lights):
        for light in lights:
            if self.is_light_on_the_street(light):
                self.lights.append(light)

    def isPointInCrossrRoad(self, p: Point):
        for c in self.crossroads:
            if c.isPointOnCrossRoad(p):
                return True, c.crossed_street
        return False, None

    def isPointInCrossrRoad(self, p: Point, offset: int):
        for c in self.crossroads:
            if c.isPointOnCrossRoad(p, offset):
                return True, c.crossed_street
        return False, None

    def isPointOnTheStreet(self, p: Point):
        if self.IsHorizontal:
            return self.start_point.y <= p.y and self.end_point.y >= p.y
        return self.start_point.x <= p.x and self.end_point.x >= p.x

    def is_light_on_the_street(self, light):

        if self.IsHorizontal:
            middle_of_the_street =  (self.start_point.y + self.end_point.y)/2
            distance = abs(light.y-middle_of_the_street)
        else:
            middle_of_the_street =  (self.start_point.x + self.end_point.x)/2
            distance = abs(light.x-middle_of_the_street)
        return distance < 100
