from typing import List
from ui_model.point import Point
from ui_model.crossroad import CrossRoad


class Street():
    def __init__(self, start_point:  Point, end_point: Point, canvas, isHorizontal) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.canvas = canvas
        self.IsHorizontal = isHorizontal
        self.IsVertiacal = not isHorizontal
        self.crossroads= []
        self.draw_street()

    def draw_street(self):
        self.rectangle = self.canvas.create_rectangle(self.start_point.x, self.start_point.y, self.end_point.x, self.end_point.y, fill='gray')
        self.canvas.tag_lower(self.rectangle )

    def add_crossroad(self, crossRoad: CrossRoad):
        self.crossroads.append(crossRoad)

    def isPointInCrossrRoad(self, p: Point):
        for c in self.crossroads:
            if c.isPointOnCrossRoad(p):
                return True, c.crossed_street
        return False, None
        
