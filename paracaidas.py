import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros del paracaidista
m = 80  # masa (kg)
g = 9.81  # gravedad (m/s^2)
k = 0.25  # coeficiente de resistencia del aire (kg/m)
v_t = np.sqrt(m * g / k)  # velocidad terminal (m/s)

# Función para calcular la derivada de la velocidad
def dvdt(v, t):
    return g - (k / m) * v**2 

# Simulación con método de Euler
def euler_method(v0, dt, t_max):
    t_vals = np.arange(0, t_max, dt)
    v_vals = np.zeros_like(t_vals)
    v_vals[0] = v0
    for i in range(1, len(t_vals)):
        v_vals[i] = v_vals[i - 1] + dvdt(v_vals[i - 1], t_vals[i - 1]) * dt
    return t_vals, v_vals

# Simulación
v0 = 0  # velocidad inicial (m/s)
dt = 0.1  # paso de tiempo
t_max = 20  # tiempo máximo de simulación (s)
t_vals, v_vals = euler_method(v0, dt, t_max)

# Crear la figura y el eje
fig, ax = plt.subplots()
ax.set_xlim(0, t_max)
ax.set_ylim(0, max(v_vals))
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Velocidad (m/s)')
ax.set_title('Velocidad del paracaidista en función del tiempo (Euler)')

line, = ax.plot([], [], lw=2)
vel_text = ax.text(0.8, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    vel_text.set_text('')
    return line, vel_text

def update(frame):
    line.set_data(t_vals[:frame], v_vals[:frame])
    vel_text.set_text(f'v = {v_vals[frame]:.2f} m/s')
    
    if frame == len(t_vals) - 1:
        ani.event_source.stop()
    
    return line, vel_text

ani = FuncAnimation(fig, update, frames=len(t_vals), init_func=init, blit=True, interval=50)
plt.grid()
plt.show(block=True)
