import numpy as np
import paths
import os

os.makedirs(paths.data / "sim", exist_ok=True)

# simple and stupid function
def run(x, y):
    return np.array([x + y, x*y])

data = run(x=25, y=10)
# comment add for test##########
np.save(paths.data / "simulation_1", data)
