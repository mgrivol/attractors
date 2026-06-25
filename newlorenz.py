import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint


# Lorenz system parameters
SIGMA = 10.0
RHO   = 28.0
BETA  = 8.0 / 3.0

# Animation parameters
DT = 0.01
N_STEPS = 10000


def lorenz(state, t, sigma=SIGMA, rho=RHO, beta=BETA):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]


def main():
    # Integrate system over time
    t = np.arange(0, N_STEPS * DT, DT)
    initial_state = [1.0, 1.0, 1.0]

    trajectory = odeint(lorenz, initial_state, t)
    print(type(trajectory), trajectory.shape)
    print(trajectory[:10])
    
    state = initial_state
    for i in range(10):
        dx, dy, dz = lorenz(state, i)
        state = np.array(state) + np.array([dx, dy, dz]) * DT
        print(f'{state[0]:.3f} {state[1]:.3f} {state[2]:.3f} --> {trajectory[i+1, 0]:.3f} {trajectory[i+1, 1]:.3f} {trajectory[i+1, 2]:.3f}')

    


if __name__ == '__main__':
    main()
