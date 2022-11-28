import matplotlib.pyplot as pplot

from simulation.simulation import simulate_number_of_people

hours_lables = ["18", "19", "20", "21", "22", "23", "0", "1" , "2", "3", "4", "5", "6"]
resolution = 1800
filename ="./example_scenarios/powerlight_simulation.txt"

pow_cons, normal_lights , anx = simulate_number_of_people(100, filename, resolution)
pplot.plot(range(len(pow_cons)), pow_cons)
pplot.xticks(range(len(pow_cons)), hours_lables)
pplot.ylim([0, max(pow_cons)+1])
pplot.xlabel("Hours")
pplot.ylabel("Energy consumption in kW")
# pplot.show()
pplot.savefig("normal_1800_res_100_people_powerlight_simulation.png")

# print(anx[0])
pplot.clf()
pplot.plot(range(len(anx[0])),anx[0])
pplot.ylim([0, max(anx[0])+10])
pplot.xticks(range(len(pow_cons)), hours_lables)
pplot.xlabel("Hours")
pplot.ylabel("Anxiety level")
# pplot.show()
pplot.savefig("anxiety_1800_res_100_people_powerlight_simulation.png")
