from ui_model.point import Point

class CrossRoad():
    def __init__(self, crossed_street, point_top: Point, point_bottom: Point) -> None:
        self.crossed_street = crossed_street
        self.top=point_top
        self.bottom = point_bottom

    def isPointOnCrossRoad(self, point: Point):
        if(point.x >= self.top.x and point.x <= self.bottom.x):
            if point.y >= self.top.y and point.y <= self.bottom.y :
                return True
        return False