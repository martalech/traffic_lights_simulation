from ui_model.point import Point
from ui_model.street import Street, CrossRoad


class StreetMap():
    def __init__(self) -> None:
        self.streets = []
        self.lights= []

    def add_street(self, new_street: Street):
        for s in self.streets:
            self.calculate_crossroad(new_street, s)
        self.streets.append(new_street)

    def calculate_crossroad(self, s1: Street, s2: Street):
        isIntersection, p1, p2 = self.check_if_rectangles_intersect(s1,s2)
        if isIntersection:
            s1.add_crossroad(CrossRoad(s2, p1, p2))

    def check_if_rectangles_intersect(self, rect1: Street, rect2: Street):
        if (rect1.IsHorizontal and rect2.IsHorizontal) or (rect1.IsVertiacal and rect2.IsVertiacal): # they cannot cross
            return False, None, None        
        if rect1.IsVertiacal:
            return self.check_if_rectangles_intersect(rect2, rect1)
        if rect1.start_point.x <= rect2.end_point.x and rect1.end_point.x >= rect2.start_point.x:
            if rect1.start_point.y <= rect2.end_point.y and rect1.end_point.y >= rect2.start_point.y:
                return self.calculate_intersection(rect1, rect2)
        return False, None, None

    def calculate_intersection(self, rect1: Street, rect2: Street):
        start_p = Point(0,0)
        end_p = Point(0,0)
        if rect1.start_point.x < rect2.start_point.x:
            start_p.x = rect2.start_point.x
        else:
            start_p.x = rect1.start_point.x
        if rect1.end_point.x < rect2.end_point.x:
            end_p.x =  rect1.start_point.x
        else:
            end_p.x = rect2.start_point.x
        if rect1.start_point.y < rect2.start_point.y:
            start_p.y = rect2.start_point.y
        else:
            start_p.y = rect1.start_point.y
        if rect1.end_point.y < rect2.end_point.y:
            end_p.y = rect1.end_point.y
        else:
            end_p.y = rect2.end_point.y
        
        return True, start_p, end_p