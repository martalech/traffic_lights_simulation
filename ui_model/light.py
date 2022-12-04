import os
import pandas as pd
import math
import uuid

# base light, always turned on
class Light():

    def __init__(self, x, y, color='yellow'):
        self.x = x  
        self.y = y
        self.size = 120
        self.light_no = uuid.uuid4()
        self.power = 0
        self.current_energy = []
<<<<<<< HEAD
        self.accumulated_energy = []
        # i think we dont need this
        # self.light_time = 0
        # self.is_turn_on = False
        # self.temp_light_start = None
        # self.temp_light_end = None
=======
        self.accumulated_energy = []    
>>>>>>> e2ce4e1670dad1de363f37c1af52efcd35380232
    
    def check_distance(self, x1, y1, x2, y2):
        # return distance between current light bulb and a person
        return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    
    def adjust_light(self, people):
        self.power = 100

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

    def calculate_light_gui(self):
        return int(self.power / 110 * 255)
    
    def calculate_energy(self):
        self.current_energy.append(self.power)
        self.accumulated_energy.append(sum(self.current_energy))
    
    def get_luminance(self):
        return self.power * 117  # 117 is Luminous efficacy for most streetlights
    
    def output_data(self,dir):
        # output data to dir in 3 csv files
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
