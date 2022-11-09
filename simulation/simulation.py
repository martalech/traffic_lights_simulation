from configuration_parser.parser import parse_scenario
from generators.people_generator import PeopleGenerator
from model.time import Time

def simulate(people_number, scenario_file_name):
    time = Time()
    time.resolution = 1800 # we say that 1 tick is 2 sec
    street_map, lights = parse_scenario(scenario_file_name)
    people = PeopleGenerator.generate_people(people_number, street_map)
    street_map.add_people(people)
    power_consumptions = []
    anxiety = []
    try:
        energy = []
        current_anxiety= []
        while True:
            time.tick()
            shift_factor = time.get_shift_factor()
            # update the environment
            if shift_factor !=1 :
                street_map.adjust_traffic(shift_factor)
            if time.current_hour != time.previous_hour and time.incrementer == 0: # change of hour
                # save data for previous hour
                power_consumptions.append(sum(energy)) # TODO: make it per hour? or per minute maybe ?
                energy = []
                anxiety.append(sum(current_anxiety)/len(current_anxiety))  
                current_anxiety = []

            # gather the data for power:
            for l in lights:
                l.adjust_light(street_map.people)
                energy.append(l.power) # TODO: here multiply by some value for power depending on dimming...
            # gather data for anxiety:
            for p in street_map.people:
                anx = p.calculate_anxiety(lights)
                current_anxiety.append(anx)
                      
    except:
        # handle last hour
        power_consumptions.append(sum(energy))
        anxiety.append(sum(current_anxiety)/len(current_anxiety))  

    return power_consumptions, anxiety

