from datetime import datetime

import math
import uuid

class Light():

    temp_light_start = None
    temp_light_end = None

    def __init__(self, x, y, color='yellow'):
        self.x = x  
        self.y = y
        self.size = 70
        self.light_no = uuid.uuid4()
        # i think we dont need this
        # self.light_time = 0
        # self.is_turn_on = False
        # self.temp_light_start = None
        # self.temp_light_end = None

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
