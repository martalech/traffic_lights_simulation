import math
'''
In this section, you should input the person's coordinates and light intensity of two adjacent lights

if you want to use the function "get_intensity", you need to offer the lights' coordinates
'''

class Intensity:
    
    def __init__(self, x, y,L1,L2):
        #the unit is mm.
        self.light_hight = 3000
        self.person_hight = 1800
        self.x = x
        self.y = y
        self.threshold = 20 #lux
        
        #L1 is the Intensity of the first light
        #L2 is the Intensity of the second one.
        self.L1 = L1 
        self.L2 = L2
        
        #redius is the range that each lamp can illuminate（circle）
        self.radius = 2000
        #redius_Insection is the intersection part
        self.radius_insection = 500
        self.light_intensity = 0
        
    def get_intensity(self, x1,y1,x2,y2):
        #(x1,y1) is the coordinates of the Lamp 1
        #(x2,y2) is the coordinates of the Lamp 2

        distance1 = math.sqrt((x1 - self.x)**2 +(y1 - self.y)**2)
        #distance1 = math.sqrt((self.light_hight - self.person_hight)**2 + distance1_1**2)
        
        distance2 = math.sqrt((x2 - self.x)**2 +(y2 - self.y)**2)
        #distance2 = math.sqrt((self.light_hight - self.person_hight)**2 + distance2_1**2)
        
        light_intensity1  = (1 - distance1/self.radius) * self.L1
        light_intensity2  = (1 - distance2/self.radius) * self.L2   
        
        
        #if the person is located within the range of the first light while not in the intersecting area
        if distance1 < self.radius and distance2 > self.radius:
            self.light_intensity = light_intensity1
            
        #if the person is locatedin the intersectiong area
        elif distance1_1<self.radius and distance2 < self.radius:
            self.light_intensity = light_intensity1 + light_intensity2
        
        #If the person is out of bounds, we assume that the two lights are not illuminating him。
        else:
            self.light_intensity = 0
            
        
            
        return self.light_intensity
    
      
  
  
  
