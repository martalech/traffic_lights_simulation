from configuration_parser.parser import parse_scenario
from generators.people_generator import PeopleGenerator
from model.time import Time
<<<<<<< HEAD
from ui_model.power_light import Power_Light
import os
import datetime
import pandas as pd


=======
>>>>>>> e2ce4e1670dad1de363f37c1af52efcd35380232

def simulate_number_of_people(scenario_file_name, resolution, people_number=10, should_remove_people=False):
    time = Time()
    time.resolution = resolution # we say that 1 tick is 2 sec
    street_map, lights = load_simulation_data(scenario_file_name, should_remove_people, people_number)
    power_consumptions = []
    anxiety = []
    anxiety_df = {"time":[],"x":[],"y":[],"anx":[]}
    try:
        energy = []
        current_anxiety = []

        while True:
            time.tick()
            shift_factor = time.get_shift_factor()
            # update the environment
            if shift_factor !=1 :
                street_map.adjust_traffic(shift_factor)
            if time.current_hour != time.previous_hour and time.incrementer == 0: # change of hour
                # save data for previous hour
                power_consumptions.append(sum(energy)) 
                energy = []
                anxiety.append(sum (current_anxiety)/len(current_anxiety))  
                current_anxiety = []
            # move people
            for p in street_map.people:
                p.move(1400, 1200)
            # gather the data for power:
            for l in lights:
                l.adjust_light(street_map.people)
                l.calculate_energy()
                energy.append((l.power)/(time.resolution * 1000)) # kilo wats per hour
            # gather data for anxiety:
            temp_anx = []
            for p in street_map.people:
                anx = p.calculate_anxiety(lights)
                anxiety_df.get("time").append(time.current_hour)
                anxiety_df.get("x").append(p.x)
                anxiety_df.get("y").append(p.y)
                anxiety_df.get("anx").append(anx)
                temp_anx.append(anx)
            current_anxiety.append(sum(temp_anx)/ len(temp_anx))
                      
    except:
        # handle last hour
        for l in lights:
            l.adjust_light(street_map.people)
            l.calculate_energy()
            energy.append(l.power) 
        # gather data for anxiety:
        for p in street_map.people:
            anx = p.calculate_anxiety(lights)
            anxiety_df.get("time").append(time.current_hour)
            anxiety_df.get("x").append(p.x)
            anxiety_df.get("y").append(p.y)
            anxiety_df.get("anx").append(anx)
            current_anxiety.append(anx)

        power_consumptions.append(sum(energy)/ (time.resolution * 1000))
        anxiety.append(sum(current_anxiety)/len(current_anxiety))  

    # output result to data folder
    # default directory name = scenario name + power ratio + time
    dir = "./data/" + scenario_file_name.split("/")[-1].split(".")[0] 
    if isinstance(lights[0], Power_Light):
        dir += '_' + str(lights[0].ratio)
    time_now  = datetime.datetime.now().strftime('_%Y%m%d_%H%M%S') 
    dir = dir + time_now
    if os.path.exists(dir):
        raise FileExistsError
    else:
        for light in lights:
            light.output_data(dir)
        pd.DataFrame(anxiety_df).to_csv(dir+"/anxiety_detail.csv")
        pd.DataFrame([anxiety]).transpose().to_csv(dir+"/anxiety_overall.csv",index=True,header=False)

    return power_consumptions, anxiety

def load_simulation_data(scenario_file_name, should_remove_people=False, people_number=10 ):
    street_map, lights = parse_scenario(scenario_file_name)
    if should_remove_people:
        people = PeopleGenerator.generate_people(people_number, street_map)
        street_map.remove_people()
        street_map.add_people(people)

    return street_map, lights