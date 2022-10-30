class StreetMap():
    def __init__(self) -> None:
        self.streets = []
        self.crossroads= []

    def add_street(self):
        new_street = None # to do think of what to pass
        for s in self.streets:
            self.calculate_crossroad(new_street, s)
        self.streets.append(new_street)

    def calculate_crossroad(self, s1, s2):
        # calculate if intersect
        # if so add to crossroads list
        pass

