import matplotlib.pyplot as pplot

from simulation.simulation import simulate_number_of_people

resolution = 120
light_system="powerlight_simulation"
filename =f"./example_scenarios/{light_system}.txt"
filename_normal_lights = "./example_scenarios/light_simulation.txt"

energy = []
normal_energy=[]
people = range(1000, 5001, 100)
for i in people:
    pow_cons, anx = simulate_number_of_people(filename, resolution,i, True)
    pow_cons_normal_light, anx_normal_light = simulate_number_of_people(filename_normal_lights, resolution,i, True)
    normal_energy.append(sum(pow_cons_normal_light))
    energy.append(sum(pow_cons))

pplot.plot(people, energy, label="Intelligent lights")
pplot.plot(people, normal_energy, label="Normal lights")
pplot.xlabel("Amount of people")
pplot.ylabel("Energy consumption in one day in kW")
pplot.legend()
pplot.savefig("find_treshold.png")
