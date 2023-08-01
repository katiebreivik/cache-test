import simulation
import matplotlib.pyplot as plt
import paths
import numpy as np

# Run the simulation for some inputs

data1 = np.load(paths.data / "simulation_1.npy")

# Plot the results#
fig, ax = plt.subplots(1)
ax.plot(data1, color="k", label="data 1")
ax.legend()
fig.savefig(paths.figures / "figure.pdf")

