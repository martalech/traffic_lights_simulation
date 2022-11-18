from datetime import datetime

import math
import uuid

class Light():

    temp_light_start = None
    temp_light_end = None

    def __init__(self, x, y, color='yellow'):
        self.x = x  
        self.y = y
        self.size = 120
        self.light_no = uuid.uuid4()
