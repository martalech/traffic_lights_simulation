from generators.street_generator import StreetGenerator
from street_models.street_map import StreetMap
from ui_model.power_light import Power_Light

def parse_street(values, new_map):
    start_x = int(values[0])
    start_y = int(values[1])
    end_x = int(values[2])
    if values[3] == "horizontal":
        new_map.add_street(StreetGenerator.generate_horizontal_street(start_x, start_y, end_x))
    elif values[3] == "vertical":
        new_map.add_street(StreetGenerator.generate_vertical_street(start_x, start_y, end_x))
    else:
        raise Exception()

def parse_light(values, new_lights):
    x = int(values[0])
    y = int(values[1])
    new_lights.append(Power_Light(x, y))

def parse_setting(setting, new_map, new_lights):
    if setting[0] == "street":
        values = setting[1].strip().split(',')
        parse_street(values, new_map)
    elif setting[0] == "light":
        values = setting[1].strip().split(',')
        parse_light(values, new_lights)
    else:
        raise Exception()

def parse_scenario(filename, draw_gui):
    new_map = StreetMap()
    new_lights = []
    with open(filename) as file:
        for line in file.readlines():
            setting = line.split(':')
            parse_setting(setting, new_map, new_lights)
    
    draw_gui.remove_strets()
    draw_gui.remove_lights()
    draw_gui.add_streets(new_map)
    draw_gui.add_lights(new_lights)
    draw_gui.draw_streets()
    draw_gui.draw_lights()
