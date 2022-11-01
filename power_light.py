from light import Light
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

    def __init__(self,canvas, x, y, light_number, color='yellow'):
        super(Power_Light,self).__init__(canvas, x, y, light_number, color='yellow')
        self.power = 0
        self.current_energy = []
        self.accumulated_energy = []    

    def __check_distance(self, x1, y1, x2, y2):
        # return distance between current light bulb and a person
        return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

    def adjust_light(self, people):
        # get the distance of the nearest person
        nearest_person_distance = sys.maxsize
        for person in people:
            nearest_person_distance = min(nearest_person_distance,self.__check_distance(person.x, person.y, self.x, self.y))
        
        # adjust light based on the distance of the nearest person
        if nearest_person_distance <= self.size: 
            # the nearest person is within current light bulb
            self.power = 2
            self.turn_on_the_light()
        elif self.size < nearest_person_distance <= 3*self.size:
            # the nearest person is in the neighbor light bulb
            self.power = 1
            self.turn_on_the_light()
        else: 
            # the nearest person is out of activated area
            self.power = 0
            self.turn_off_the_light()

    def calculate_energy(self):
        self.current_energy.append(self.power)
        self.accumulated_energy.append(sum(self.current_energy))
    
    def output_data(self,dir):
        # output data to dir in 3 csv files
        # dir = "./data/experiment_0"
        if not os.path.exists(dir):
            os.makedirs(dir)
            df1 = pd.DataFrame(data={self.light_no+"_current_energy":self.current_energy})
            df2 = pd.DataFrame(data={self.light_no+"_accumulated_energy":self.accumulated_energy})
            df3 = pd.DataFrame(data={"light_number":self.light_no,
                                    "light_x":self.x,
                                    "light_y":self.y,
                                    "total_energy":self.accumulated_energy[-1]},index=[0])
            df1.to_csv(dir+"/current_energy.csv",index=False)
            df2.to_csv(dir+"/accumulated_energy.csv",index=False)
            df3.to_csv(dir+"/overall.csv",index=False)
        else:
            df1 = pd.read_csv(dir+"/current_energy.csv")
            df1[self.light_no+"_current_energy"] = self.current_energy

            df2 = pd.read_csv(dir+"/accumulated_energy.csv")
            df2[self.light_no+"_accumulated_energy"] = self.accumulated_energy
            
            df3 = pd.read_csv(dir+"/overall.csv")
            new_row = pd.DataFrame({"light_number":self.light_no,
                    "light_x":self.x,
                    "light_y":self.y,
                    "total_energy":self.accumulated_energy[-1]},index=[0])
            df3 = pd.concat([df3,new_row])

            df1.to_csv(dir+"/current_energy.csv",index=False)
            df2.to_csv(dir+"/accumulated_energy.csv",index=False)
            df3.to_csv(dir+"/overall.csv",index=False)