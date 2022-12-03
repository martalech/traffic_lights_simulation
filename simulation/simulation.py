from configuration_parser.parser import parse_scenario
from generators.people_generator import PeopleGenerator
from model.time import Time

def simulate_number_of_people(scenario_file_name, resolution, people_number=10, should_remove_people=False):
    time = Time()
    time.resolution = resolution # we say that 1 tick is 2 sec
    street_map, lights = load_simulation_data(scenario_file_name, should_remove_people, people_number)
    power_consumptions = []
    anxiety = []
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
                power_consumptions.append(sum(energy) / (time.resolution * 1000) ) # kilo wats per hour
                energy = []
                anxiety.append(sum(current_anxiety)/time.resolution) 
                current_anxiety = []
            # move people
            for p in street_map.people:
                p.move(1400, 1200)
            # gather the data for power:
            for l in lights:
                l.adjust_light(street_map.people)
                l.calculate_energy()
                energy.append(l.power) 
            # gather data for anxiety:
            temp_anx = []
            for p in street_map.people:
                anx = p.calculate_anxiety(lights)
                temp_anx.append(anx)
            current_anxiety.append(sum(temp_anx)/ len(temp_anx))
                      
    except:
        # handle last hour
        power_consumptions.append(sum(energy)/ (time.resolution * 1000))
        anxiety.append(sum(current_anxiety)/time.resolution)  
          

    return power_consumptions, anxiety

def load_simulation_data(scenario_file_name, should_remove_people=False, people_number=10 ):
    street_map, lights = parse_scenario(scenario_file_name)
    if should_remove_people:
        people = PeopleGenerator.generate_people(people_number, street_map)
        street_map.remove_people()
        street_map.add_people(people)

    return street_map, lights