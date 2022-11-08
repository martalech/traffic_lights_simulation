class TrafficDistribution:
    def __init__(self):
        # Key is an hour, value is traffic intensity
        # E.g. at 6pm, there is traffic intensity of 9 (0-10) scale
        self.distribution = {
            18: 9,
            19: 1, # change to 10
            20: 10,
            21: 1, # change to 9
            22: 8,
            23: 7,
            0: 9,
            1: 8,
            2: 6,
            3: 4,
            4: 1,
            5: 3,
            6: 7
        }

    def get_intensity(self, hour):
        return self.distribution[hour]

