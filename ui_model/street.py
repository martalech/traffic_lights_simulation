from typing import List
from ui_model.point import Point
from ui_model.crossroad import CrossRoad


class Street():
    def __init__(self, start_point:  Point, end_point: Point, isHorizontal) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.IsHorizontal = isHorizontal
        self.IsVertiacal = not isHorizontal
        self.crossroads= []

    def add_crossroad(self, crossRoad: CrossRoad):
        self.crossroads.append(crossRoad)

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
        
