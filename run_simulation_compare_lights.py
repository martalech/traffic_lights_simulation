import matplotlib.pyplot as pplot

from simulation.simulation import simulate_number_of_people

hours_lables = ["18", "19", "20", "21", "22", "23", "0", "1" , "2", "3", "4", "5", "6"]
resolution = 1800
filename_power_light ="./example_scenarios/powerlight_simulation.txt"
filename_simple_lights = "./example_scenarios/simplelight_simulation.txt"
filename_lights = "./example_scenarios/light_simulation.txt"

result_energy_pl = []
result_anxiety_pl = []
result_energy_sl = []
result_anxiety_sl = []
result_energy_l = []
result_anxiety_l = []

for _ in range(0,10):
    # power light
    pow_cons_pl, anx_pl = simulate_number_of_people(filename_power_light, resolution)
    result_energy_pl.append(pow_cons_pl)
    result_anxiety_pl.append(anx_pl)
    # simple light
    pow_cons_sl, anx_sl = simulate_number_of_people(filename_simple_lights, resolution)
    result_energy_sl.append(pow_cons_sl)
    result_anxiety_sl.append(anx_sl)
    # basic light
    pow_cons_l, anx_l = simulate_number_of_people(filename_lights, resolution)
    result_energy_l.append(pow_cons_l)
    result_anxiety_l.append(anx_l)

 # calculate average per hour:
energy_average_power = [sum(sub_list) / len(sub_list) for sub_list in zip(*result_energy_pl)]
energy_average_simple = [sum(sub_list) / len(sub_list) for sub_list in zip(*result_energy_sl)]
energy_average_basic = [sum(sub_list) / len(sub_list) for sub_list in zip(*result_energy_l)]

anxiety_average_power = [sum(sub_list) / len(sub_list) for sub_list in zip(*result_anxiety_pl)]
anxiety_average_simple = [sum(sub_list) / len(sub_list) for sub_list in zip(*result_anxiety_sl)]
anxiety_average_basic = [sum(sub_list) / len(sub_list) for sub_list in zip(*result_anxiety_l)]

 # generate diagrams   
pplot.plot(range(len(energy_average_power)), energy_average_power, label="Intelligent lights")
pplot.plot(range(len(energy_average_power)), energy_average_simple, label="Simple intelligent lights")
pplot.plot(range(len(energy_average_basic)), energy_average_basic, label="Standard lights")
pplot.xticks(range(len(energy_average_power)), hours_lables)
pplot.ylim([0, max(energy_average_power)+1])
pplot.xlabel("Hours")
pplot.ylabel("Energy consumption in kW")
pplot.legend()
pplot.savefig(f'energy_{resolution}_compare_systems.png')

pplot.clf()
pplot.plot(range(len(anxiety_average_power)),anxiety_average_power, label="Intelligent lights")
pplot.plot(range(len(anxiety_average_simple)),anxiety_average_simple, label="Simple intelligent lights")
pplot.plot(range(len(anxiety_average_basic)), anxiety_average_basic, label="Standard lights")
pplot.ylim([0, max(anxiety_average_power)+10])
pplot.xticks(range(len(anxiety_average_power)), hours_lables)
pplot.xlabel("Hours")
pplot.ylabel("Anxiety level")
pplot.legend()
pplot.savefig(f'anxiety_{resolution}_res_compare_systems.png')

print(sum(energy_average_basic), sum(energy_average_power), sum(energy_average_simple))
