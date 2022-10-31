from ui_model.point import Point

class Street():
    def __init__(self, start_point:  Point, end_point: Point, canvas) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.canvas = canvas
        self.draw_street()

    def draw_street(self):
        self.rectangle = self.canvas.create_rectangle(self.start_point.x, self.start_point.y, self.end_point.x, self.end_point.y, fill='gray')
        self.canvas.tag_lower(self.rectangle )