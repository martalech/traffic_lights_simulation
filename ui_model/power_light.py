from ui_model.light import Light
import sys

# intelligent light based on the people's distance
class Power_Light(Light):

    def __init__(self, x, y, color='yellow'):
        super(Power_Light,self).__init__(x, y, color='yellow')
        self.ratio = 0.1 # ratio of intelligent part power and light power 

    def adjust_light(self, people):

        light_power_max = 100
        intelligent_power = light_power_max*self.ratio

        # get the distance of the nearest person
        nearest_person_distance = sys.maxsize
        for person in people:
            nearest_person_distance = min(nearest_person_distance,self.check_distance(person.x, person.y, self.x, self.y))
        
        # adjust light based on the distance of the nearest person
        if nearest_person_distance <= self.size: 
            # the nearest person is within current light bulb
            self.power = light_power_max*0.9+intelligent_power
        elif self.size < nearest_person_distance <= 3*self.size:
            # the nearest person is in the first neighbor light bulb
            self.power = light_power_max*0.6+intelligent_power
        elif 3*self.size < nearest_person_distance <= 5*self.size:
            # the nearest person is in the second neighbor light bulb
            self.power = light_power_max*0.3+intelligent_power
        else: 
            # the nearest person is out of activated area
            self.power = light_power_max*0.1+intelligent_power

    def calculate_light_gui(self):
        return int(self.power / 110 * 255)

