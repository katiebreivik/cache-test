import simulation
import matplotlib.pyplot as plt
import paths
import numpy as np

# Run the simulation for some inputs

data1 = np.load(paths.data / "sim" / "simulation_1.npy")
data2 = np.load(paths.data / "sim" / "simulation_2.npy")

# Plot the results#
fig, ax = plt.subplots(1)
ax.plot(data1, color="k", label="data 1")
ax.plot(data2, color="red", label="data 2")
ax.legend()
fig.savefig(paths.figures / "figure.pdf")

