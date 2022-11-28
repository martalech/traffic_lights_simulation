from configuration_parser.parser import parse_scenario
from generators.people_generator import PeopleGenerator
from model.time import Time
from ui_model.power_light import Power_Light
import os
import datetime



def simulate_number_of_people(people_number, scenario_file_name, resolution):
    time = Time()
    time.resolution = resolution # we say that 1 tick is 2 sec
    street_map, lights = parse_scenario(scenario_file_name)
    people = PeopleGenerator.generate_people(people_number, street_map)
    street_map.remove_people()
    street_map.add_people(people)
    power_consumptions = []
    anxiety = {}
    try:
        energy = []
        current_anxiety = {}

        while True:
            time.tick()
            shift_factor = time.get_shift_factor()
            # update the environment
            if shift_factor !=1 :
                street_map.adjust_traffic(shift_factor)
            if time.current_hour != time.previous_hour and time.incrementer == 0: # change of hour
                # save data for previous hour
                power_consumptions.append(sum(energy) / (time.resolution * 1000) ) # kilo wats per hour
                energy = []
                for idx, _ in enumerate(street_map.people):
                    if idx not in anxiety:
                        anxiety[idx] = []
                    if idx in current_anxiety:
                        anxiety[idx].append(sum(current_anxiety[idx])/time.resolution)  
                    else:
                        anxiety[idx].append(0)
                    current_anxiety = {}

            # gather the data for power:
            for l in lights:
                l.adjust_light(street_map.people)
                l.calculate_energy()
                energy.append(l.power) 
            # gather data for anxiety:
            for idx,p in enumerate(street_map.people):
                anx = p.calculate_anxiety(lights)
                if(idx not in current_anxiety):
                    # print("if ", anx, idx)
                    current_anxiety[idx] = []
                if anx is not  None:
                    current_anxiety[idx].append(anx)
                # print(current_anxiety[idx])
                      
    except:
        # handle last hour
        # print("here")
        power_consumptions.append(sum(energy)/ (time.resolution * 1000))
        for idx, p in enumerate(street_map.people):
            if idx not in anxiety:
                anxiety[idx] = []
            if idx in current_anxiety:
                anxiety[idx].append(sum(current_anxiety[idx])/time.resolution)  
            else:
                anxiety[idx].append(0)
    normal_lights = [len(lights)*100/ 1000] * 13
    return power_consumptions, normal_lights, anxiety