import numpy as np
import matplotlib


N = 50
time_step = 5
num_of_steps = 100
G = 6.67430e-11
softening = 2

positions = []
velocities = []
masses = []
forces = []
positions_over_time = []

position = np.array([x, y, z])
velocity = np.array([vx, vy, vz])
force = np.array([fx, fy, fz])
mass = m

for i in range (N):
    # Random position within a certain range, for example, between -100 and 100 for each axis
    position = np.random.uniform()  # 3D position
    positions.append(position)
    
    # Random velocity, within some range (e.g., -10 to 10 for each axis)
    velocity = np.random.uniform()  # 3D velocity
    velocities.append(velocity)
    
    # Random mass, let's say between 1e20 and 1e25 kg
    mass = np.random.uniform()
    masses.append(mass)
    
    # Random force (for simplicity, let's assume it’s within -1e22 to 1e22 Newtons in each direction)
    force = np.random.uniform()  # 3D force
    forces.append(force)