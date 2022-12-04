class TrafficDistribution:
    def __init__(self):
        # Key is an hour, value is traffic intensity
        # E.g. at 6pm, there is traffic intensity of 9 (0-10) scale
        self.distribution_week_days = {
            18: 7,
            19: 6,
            20: 6,
            21: 7,
            22: 6,
            23: 4,
            0: 2,
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 2,
            6: 4
        }
        self.distribution_weekends = {
            18: 8,
            19: 7,
            20: 6,
            21: 7,
            22: 6,
            23: 8,
            0: 7,
            1: 6,
            2: 5,
            3: 4,
            4: 3,
            5: 2,
            6: 2
        }

    def get_intensity_weekdays(self, hour):
        return self.distribution_week_days[hour]

    def get_intensity_weekends(self, hour):
        return self.distribution_weekends[hour]

