import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint



# Lorenz system parameters
SIGMA = 10.
RHO = 28.
BETA = 8. / 3.


def lorenz(state, t, sigma=SIGMA, rho=RHO, beta=BETA):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]


# Integrate system over time
dt = 0.01
n_steps = 10000
t = np.arange(0, n_steps * dt, dt)

state_0 = [1.0, 1.0, 1.0]

trajectory = odeint(lorenz, state_0, t)
x, y, z = trajectory[:, 0], trajectory[:, 1], trajectory[:, 2]

# Plot
fig = plt.figure(figsize=(9, 7), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')
ax.set_axis_off()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min(), y.max())
ax.set_zlim(z.min(), z.max())
ax.set_title('Lorenz Attractor', color='white', fontsize=14)

# Line that traces the full path so far, and a "head" marker
line, = ax.plot([], [], [], lw=0.8, color='cyan')
head, = ax.plot([], [], [], 'o', color='white', markersize=4)

# Slowly rotate the camera
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    head.set_data([], [])
    head.set_3d_properties([])
    return line, head


# Number of points to draw per frame (speeds up the animation)
step = 5
n_frames = n_steps // step


def update(frame):
    idx = frame * step
    line.set_data(x[:idx], y[:idx])
    line.set_3d_properties(z[:idx])
    
    if idx > 0:
        head.set_data(
            [x[idx - 1]],
            [y[idx - 1]]
        )
        head.set_3d_properties([z[idx - 1]])

    # Rotate the view slowly
    ax.view_init(elev=25, azim=0.3 * frame)
    return line, head


ani = FuncAnimation(
    fig,
    update,
    frames=n_frames,
    init_func=init,
    interval=20,
    blit=False
)

# To display interact, uncomment:
plt.show()

# To save as GIF (pillow) or MP4 (ffmpeg), uncomment:
# ani.save("lorenz_attractor.gif", writer='pillow', fps=30, dpi=150)