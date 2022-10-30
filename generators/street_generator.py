from ui_model.point import Point
from ui_model.street import Street

class StreetGenerator():
    def __init__(self) -> None:
        self.street_width = 110
        
    def generate_horizontal_street(self, start_x, start_y, end_x, canvas):
        startp = Point(start_x, start_y)
        endp = Point(end_x, self.street_width + start_y)
        return Street(startp, endp, canvas)

    def generate_vertical_street(self, start_x, start_y, end_y, canvas):
        startp = Point(start_x, start_y)
        endp = Point(self.street_width + start_x, end_y)
        return Street(startp, endp, canvas)