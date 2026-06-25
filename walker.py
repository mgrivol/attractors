import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

rng = np.random.default_rng(42)


def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array"""
    start_pos = rng.random(3)
    steps = rng.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk


def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        line.set_data_3d(walk[:num, :].T)
    return lines


num_steps = 30
walks = [random_walk(num_steps) for index in range(40)]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

lines = [ax.plot([], [], [])[0] for _ in walks]

ax.set(xlim3d=(0, 1), xlabel="X")
ax.set(ylim3d=(0, 1), ylabel="Y")
ax.set(zlim3d=(0, 1), zlabel="Z")

ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100
)

plt.show()

