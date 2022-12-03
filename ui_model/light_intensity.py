import math

from ui_model.power_light import Power_Light

class Intensity:

    def __init__(self, x, y, light1: Power_Light, light2: Power_Light):
        # the unit is mm.
        self.light_height = 3000
        self.x = x
        self.y = y
        self.threshold = 20  # lux
        self.light1 = light1
        self.light2 = light2
        self.light1_luminance = light1.get_luminance()
        self.light2_luminance = light2.get_luminance()

        # radius is the range that each lamp can illuminate（circle）
        self.radius = light1.size
        # radius_insection is the intersection part
        self.radius_insection = 500
        self.light_intensity = 0

    def get_intensity(self):

        distance1 = math.sqrt((self.light1.x - self.x) ** 2 + (self.light1.y - self.y) ** 2)

        distance2 = math.sqrt((self.light2.x - self.x) ** 2 + (self.light2.y - self.y) ** 2)

        light_intensity1 = max((1 - distance1 / self.radius) * self.light1_luminance, 0)
        light_intensity2 = max((1 - distance2 / self.radius) * self.light2_luminance, 0)

        # if the person is located within the range of the first light while not in the intersecting area
        if distance1 < self.radius and distance2 > self.radius:
            self.light_intensity = light_intensity1

        # if the person is located in the intersection area
        elif distance1 < self.radius and distance2 < self.radius:
            self.light_intensity = light_intensity1 + light_intensity2

        return self.light_intensity
