from model.traffic_distribution import TrafficDistribution


class Time:
    def __init__(self):
        self.bounds = [
            18,
            19,
            20,
            21,
            22,
            23,
            0,
            1,
            2,
            3,
            4,
            5,
            6
        ]
        self.traffic_distribution = TrafficDistribution()
        self.previous_hour = 18
        self.current_hour = 18
        self.current_hour_idx = 0
        self.resolution = 120 # How many times do we need to tick in order to move to the next hour
        self.incrementer = 0

    def tick(self):
        self.incrementer = self.incrementer + 1
        if self.incrementer >= self.resolution:
            if self.current_hour == 6:
                raise RuntimeError("Night is over")
            self.current_hour_idx = self.current_hour_idx + 1
            self.previous_hour = self.current_hour
            self.current_hour = self.bounds[self.current_hour_idx]
            self.incrementer = 0
            print("New hour is ", self.current_hour)

    def get_shift_factor(self):
        if self.incrementer == 0 and self.current_hour != self.previous_hour:
            return self.traffic_distribution.get_intensity_weekdays(self.current_hour) / self.traffic_distribution.get_intensity_weekdays(self.previous_hour)
            # uncomment for weekend
            # return self.traffic_distribution.get_intensity_weekends(self.current_hour) / self.traffic_distribution.get_intensity_weekends(self.previous_hour)
        return 1

