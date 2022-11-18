import random
import math
import sys
import os
import pandas as pd


class Person():
    def __init__(self,mode):
        self.rand = random.Random()
        self.t = self.rand.randint(1, 1000)
        self.size = 10
        self.x=0
        self.y=0
        self.move_x=0
        self.move_y=0
        if mode==1:
            self.x = self.t
            self.y = 100 
            self.move_x = self.rand.randint(-20, 21)
            self.move_y = 0
        elif mode==2:
            self.x = self.t
            self.y = 1000 
            self.move_x = self.rand.randint(-20, 21)
            self.move_y = 0
        elif mode==3:
            self.x = 100
            self.y = self.t
            self.move_x = 0
            self.move_y = self.rand.randint(-20, 21) 
        elif mode==4:
            self.x = 1000
            self.y = self.t 
            self.move_x = 0
            self.move_y = self.rand.randint(-20, 21) 
        elif mode==5:
            self.x = self.t
            self.y = self.t
            self.move_x = self.rand.randint(-20, 21)
            self.move_y = self.move_x
        elif mode==6:
            self.x = 1000-self.t
            self.y = self.t 
            self.move_x = self.rand.randint(-20, 21)
            self.move_y = -1*self.move_x
    def move(self):
        self.x = self.x + self.move_x
        self.y = self.y + self.move_y


class Power_Light():
    def __init__(self,x,y,light_num):
        self.light_no = light_num
        self.x=x
        self.y=y
        self.size=70
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
        elif self.size < nearest_person_distance <= 3*self.size:
            # the nearest person is in the neighbor light bulb
            self.power = 1
        else: 
            # the nearest person is out of activated area
            self.power = 0
    
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


if __name__ == '__main__':
    lights=[]
    lights.append(Power_Light(500,500, '0'))
    for i in range(1,11):
        light1 = Power_Light(100,i*100, str(i))
        light2 = Power_Light(1000,i*100, str(i+10))
        lights.append(light1)
        lights.append(light2)
        if i!=1:
            light3 = Power_Light(i*100,100, str(i+19))
            light4 = Power_Light(i*100,i*100, str(i+28))
            lights.append(light3)
            lights.append(light4)
        if i!=10:
            light5 = Power_Light(i*100,1000, str(i+38))
            light6 = Power_Light((11-i)*100,i*100, str(i+47))
            lights.append(light5)
            lights.append(light6)
        
    people = []
    for i in range(50):
        person = Person(random.Random().randint(1, 7))
        people.append(person)

    def move():
        for person in people:
            person.move()
        for light in lights:
            light.adjust_light(people)
            light.calculate_energy()

    total_time = 100
    for i in range(100):
        move()

    for light in lights:
        dir = "./data/experiment_demo"
        light.output_data(dir)