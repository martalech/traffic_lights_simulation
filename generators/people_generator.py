import random

from ui_model.person import Person
from street_models.street_map import StreetMap

class PeopleGenerator():
    person_size = 10
    random.seed(10)

    @staticmethod
    def generate_person(map: StreetMap):
        point, street = map.find_spawning_spot()
        speed = random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
        person = Person(PeopleGenerator.person_size, point, street, int(speed))
        return person

    @staticmethod
    def generate_people(number_of_people, street_map):
        result = []
        for i in range(number_of_people):
            result.append(PeopleGenerator.generate_person(street_map))

        return result