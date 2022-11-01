from ui_model.person import Person
import math
import uuid

class Light():

    def __init__(self, x, y, color='yellow'):
        self.x = x  
        self.y = y
        self.size = 70
        self.light_no = uuid.uuid4()

    def should_turn_on_the_light(self, people):
        turn_on = False
        for person in people:
            if self.check_intersection(person.x, person.y, person.size, self.x, self.y, self.size):
                turn_on = True
        if turn_on:
            return True
        else:
            return False

    def check_intersection(self, x1, y1, r1, x2, y2, r2):
        d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        if(d <= r1 - r2):
            return False
        elif(d <= r2 - r1):
            return True
        elif(d < r1 + r2):
            return True
        elif(d == r1 + r2):
            return True
        else:
            return False
