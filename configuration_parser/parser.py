from generators.street_generator import StreetGenerator
from street_models.street_map import StreetMap
from ui_model.person import Person
from ui_model.point import Point
from ui_model.power_light import Power_Light
from ui_model.light import Light
from ui_model.simple_light import Simple_Light


def parse_street(street_cords, people_cords, new_map):
    start_x = int(street_cords[0])
    start_y = int(street_cords[1])
    end_x = int(street_cords[2])
    if street_cords[3] == "horizontal":
        street = StreetGenerator.generate_horizontal_street(start_x, start_y, end_x)
    elif street_cords[3] == "vertical":
        street = StreetGenerator.generate_vertical_street(start_x, start_y, end_x)
    else:
        raise Exception()
    people = parse_people(people_cords, street)
    new_map.add_street(street)
    new_map.add_people(people)


def parse_people(people_cords, street):
    people = []
    for person_cord in people_cords:
        x, y, speed = person_cord.split(',')
        people.append(Person(10, Point(int(x), int(y)), street, int(speed)))
    return people


def parse_light(values, new_lights, light_type):
    x = int(values[0])
    y = int(values[1])
    if light_type == "light":
        new_lights.append(Light(x, y))
    elif light_type == "power_light":
        new_lights.append(Power_Light(x, y))
    elif light_type == "simple_light":
        new_lights.append(Simple_Light(x, y))

def parse_setting(setting, new_map, new_lights):
    if setting[0] == "street":
        street = setting[1].strip().split(',')
        people = []
        if len(setting) == 3:
            people = setting[2].strip().split(';')
        parse_street(street, people, new_map)
    elif "light" in setting[0]:
        light = setting[1].strip().split(',')
        parse_light(light, new_lights, setting[0])
    else:
        raise Exception()


def parse_scenario_to_draw_gui(filename, draw_gui):
    new_map, new_lights = parse_scenario(filename)
    draw_gui.remove_strets()
    draw_gui.remove_lights()
    draw_gui.remove_people()
    draw_gui.add_streets(new_map)
    draw_gui.add_lights(new_lights)
    draw_gui.draw_streets()
    draw_gui.draw_lights()
    draw_gui.draw_people()

def parse_scenario(filename) -> tuple[StreetMap, list[Power_Light]]:
    new_map = StreetMap()
    new_lights = []
    with open(filename) as file:
        for line in file.readlines():
            setting = line.split(':')
            parse_setting(setting, new_map, new_lights)
    new_map.add_lights_to_streets(new_lights)
    return new_map, new_lights

