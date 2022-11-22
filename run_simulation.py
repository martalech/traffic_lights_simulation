from simulation.simulation import simulate

pow_cons, anx = simulate(10, "./example_scenarios/simplelight_gui.txt")

print(pow_cons)
print(anx)
print(len(anx), len(pow_cons))