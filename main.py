import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

TURNS = 4        # сколько витков
POINTS = 400     # сколько точек в спирали (больше - глаже)
RADIUS = 1.0     # радиус спирали
HEIGHT = 10.0    # высота
SPEED = 0.05     # скорость вращения

z = np.linspace(0, HEIGHT, POINTS)
phase = z / HEIGHT * TURNS * 2 * np.pi

fig = plt.figure(figsize=(6, 8))
ax = fig.add_subplot(projection="3d")
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(0, HEIGHT)
ax.set_box_aspect((1, 1, 3))
ax.axis("off")

line1, = ax.plot([], [], [], lw=3, color="tab:blue")
line2, = ax.plot([], [], [], lw=3, color="tab:red")


def update(frame):
    a = phase + frame * SPEED
    line1.set_data_3d(RADIUS * np.cos(a), RADIUS * np.sin(a), z)
    line2.set_data_3d(RADIUS * np.cos(a + np.pi), RADIUS * np.sin(a + np.pi), z)
    return line1, line2


anim = FuncAnimation(fig, update, interval=20, cache_frame_data=False)
plt.show()
