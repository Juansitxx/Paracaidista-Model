import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros del paracaidista
m = 80  # masa en kg
g = 9.81  # gravedad en m/s^2
k = 0.25  # coeficiente de resistencia del aire en kg/m
dt = 0.5  # paso de tiempo
t_max = 20  # tiempo máximo en segundos

# Ecuación diferencial: dv/dt = g - (k/m) * v^2
def dvdt(v):
    return g - (k / m) * v**2

# Método de Heun para la simulación
def heun_method(v0, dt, t_max):
    t_vals = np.arange(0, t_max, dt)
    v_vals = np.zeros_like(t_vals)
    v_vals[0] = v0
    
    for i in range(1, len(t_vals)):
        v_predict = v_vals[i - 1] + dt * dvdt(v_vals[i - 1])
        v_vals[i] = v_vals[i - 1] + (dt / 2) * (dvdt(v_vals[i - 1]) + dvdt(v_predict))
    
    return t_vals, v_vals

# Simulación
v0 = 0  # velocidad inicial en m/s
t_vals, v_vals = heun_method(v0, dt, t_max)

# Crear la figura y el eje
fig, ax = plt.subplots()
ax.set_xlim(0, t_max)
ax.set_ylim(0, max(v_vals))
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Velocidad (m/s)')
ax.set_title('Velocidad del paracaidista en función del tiempo (Heun)')

# Línea que será actualizada en la animación
line, = ax.plot([], [], lw=2)
vel_text = ax.text(0.8, 0.9, '', transform=ax.transAxes)

# Función de inicialización para la animación
def init():
    line.set_data([], [])
    vel_text.set_text('')
    return line, vel_text

# Función de actualización para la animación
def update(frame):
    line.set_data(t_vals[:frame], v_vals[:frame])
    vel_text.set_text(f'v = {v_vals[frame]:.2f} m/s')
    
    # Detener la animación si llega al último frame
    if frame == len(t_vals) - 1:
        ani.event_source.stop()
    
    return line, vel_text

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(t_vals), init_func=init, blit=True, interval=50)

# Mostrar la animación y bloquear la ventana hasta que se cierre manualmente
plt.grid()
plt.show(block=True)
