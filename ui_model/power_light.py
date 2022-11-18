from ui_model.light import Light
import math
import sys
import os
import pandas as pd


'''
running demo:

for i in range(total_time):
    for light in power_lights:
        light.adjust_light(people)
        light.calculate_energy()
    for person in people:
        person.move()

for light in power_lights:
    dir = "./data/experiment_0"
    light.output_data(dir)
'''


class Power_Light(Light):

    def __init__(self, x, y, color='yellow'):
        super(Power_Light,self).__init__(x, y, color='yellow')
        self.power = 0
        self.current_energy = []
        self.accumulated_energy = []    
        self.ratio = 0.1 # ratio of intelligent part power and light power 

    def __check_distance(self, x1, y1, x2, y2):
        # return distance between current light bulb and a person
        return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

    def adjust_light(self, people):

        light_power_max = 100
        intelligent_power = light_power_max*self.ratio

        # get the distance of the nearest person
        nearest_person_distance = sys.maxsize
        for person in people:
            nearest_person_distance = min(nearest_person_distance,self.__check_distance(person.x, person.y, self.x, self.y))
        
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

    def calculate_energy(self):
        self.current_energy.append(self.power)
        self.accumulated_energy.append(sum(self.current_energy))
    
    def output_data(self,dir):
        # output data to dir in 3 csv files
        # dir = "./data/experiment_0"
        if not os.path.exists(dir):
            os.makedirs(dir)
            df1 = pd.DataFrame(data={str(self.x)+'_'+str(self.y)+"_current_energy":self.current_energy})
            df2 = pd.DataFrame(data={str(self.x)+'_'+str(self.y)+"_accumulated_energy":self.accumulated_energy})
            df3 = pd.DataFrame(data={
                                    "light_x":self.x,
                                    "light_y":self.y,
                                    "total_energy":self.accumulated_energy[-1]},index=[0])
            df1.to_csv(dir+"/current_energy.csv",index=False)
            df2.to_csv(dir+"/accumulated_energy.csv",index=False)
            df3.to_csv(dir+"/overall.csv",index=False)
        else:
            df1 = pd.read_csv(dir+"/current_energy.csv")
            df1[str(self.x)+'_'+str(self.y)+"_current_energy"] = self.current_energy

            df2 = pd.read_csv(dir+"/accumulated_energy.csv")
            df2[str(self.x)+'_'+str(self.y)+"_accumulated_energy"] = self.accumulated_energy
            
            df3 = pd.read_csv(dir+"/overall.csv")
            new_row = pd.DataFrame({
                    "light_x":self.x,
                    "light_y":self.y,
                    "total_energy":self.accumulated_energy[-1]},index=[0])
            df3 = pd.concat([df3,new_row])

            df1.to_csv(dir+"/current_energy.csv",index=False)
            df2.to_csv(dir+"/accumulated_energy.csv",index=False)
            df3.to_csv(dir+"/overall.csv",index=False)

    def get_luminance(self):
        return self.power * 117  # 117 is Luminous efficacy for most streetlights

