from ui_model.light import Light
import sys

# simple intelligent light, turns on when people are in range, turns off otherwise
class Simple_Light(Light):

    def __init__(self, x, y, color='yellow'):
        super(Simple_Light,self).__init__(x, y, color='yellow')

    def adjust_light(self, people):
        # get the distance of the nearest person
        nearest_person_distance = sys.maxsize
        for person in people:
            nearest_person_distance = min(nearest_person_distance,self.check_distance(person.x, person.y, self.x, self.y))
        
        # adjust light based on the distance of the nearest person
        if nearest_person_distance <= self.size: 
            # the nearest person is within current light bulb
            self.power = 100
        else: 
            # the nearest person is out of activated area
            self.power = 0
    
    def calculate_light_gui(self):
        return int(self.power / 110 * 255)