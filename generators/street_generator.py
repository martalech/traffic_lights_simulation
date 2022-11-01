from ui_model.point import Point
from ui_model.street import Street

class StreetGenerator():
    street_width = 110

    @staticmethod
    def generate_horizontal_street(start_x, start_y, end_x, canvas):
        startp = Point(start_x, start_y)
        endp = Point(end_x, StreetGenerator.street_width + start_y)
        return Street(startp, endp, canvas, True)

    @staticmethod
    def generate_vertical_street(start_x, start_y, end_y, canvas):
        startp = Point(start_x, start_y)
        endp = Point(StreetGenerator.street_width + start_x, end_y)
        return Street(startp, endp, canvas, False)