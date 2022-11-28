import matplotlib.pyplot as pplot

from simulation.simulation import simulate_number_of_people

hours = [18, 19, 20, 21, 22, 23, 0, 1 , 2, 3, 4, 5, 6]
resolution = 120
filename ="./example_scenarios/powerlight_simulation.txt"
# pow_cons, anx = simulate_number_of_people(10, filename, resolution)
# pplot.plot(pow_cons)
# pplot.show()

energy = []
normal_energy = []
people = range(1000, 5001, 100)
for i in people:
    pow_cons , normal_ligths, anx = simulate_number_of_people(i, filename, resolution)
    print("people, ", i, " energy ", sum(pow_cons))
    normal_energy.append(sum(normal_ligths))
    energy.append(sum(pow_cons))

pplot.plot(people, energy, label="intelligent lights")
pplot.plot(people, normal_energy, label="normal lights")
pplot.xlabel("Amount of people")
pplot.ylabel("Energy consumption per day in kW")
pplot.legend()
pplot.savefig("find_treshold_4.png")
