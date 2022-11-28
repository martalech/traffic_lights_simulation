import matplotlib.pyplot as pplot

from simulation.simulation import simulate_number_of_people

hours_lables = ["18", "19", "20", "21", "22", "23", "0", "1" , "2", "3", "4", "5", "6"]
resolution = 10
light_system="powerlight_simulation"
filename =f"./example_scenarios/{light_system}.txt"

result_energy = []
result_anxiety = []
for _ in range(0,10):
    pow_cons, anx = simulate_number_of_people(filename, resolution)
    result_energy.append(pow_cons)
    result_anxiety.append(anx)

 # calculate average per hour:
energy_average = [sum(sub_list) / len(sub_list) for sub_list in zip(*result_energy)]
anxiety_average = [sum(sub_list) / len(sub_list) for sub_list in zip(*result_anxiety)]

 # generate diagrams   
pplot.plot(range(len(energy_average)), energy_average)
pplot.xticks(range(len(energy_average)), hours_lables)
pplot.ylim([0, max(energy_average)+1])
pplot.xlabel("Hours")
pplot.ylabel("Energy consumption in kW")
pplot.savefig(f'energy_{resolution}_res_{light_system}.png')

pplot.clf()
pplot.plot(range(len(anxiety_average)),anxiety_average)
pplot.ylim([0, max(anxiety_average)+10])
pplot.xticks(range(len(anxiety_average)), hours_lables)
pplot.xlabel("Hours")
pplot.ylabel("Anxiety level")
pplot.savefig(f'anxiety_{resolution}_res_{light_system}.png')
