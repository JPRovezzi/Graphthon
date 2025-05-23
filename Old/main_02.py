import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
values = np.array([
    3.84, 3.84, 3.72, 3.4, 3.38, 3.38, 1.53, 1.43, 1.5, 1.35, 1.23, 1.34, 1.16,
    1.1, 1.15, 1.16, 1.18, 1.13, 1.1, 1.08, 1.04, 1.01, 0.99, 1.03, 1, 0.96,
    0.97, 0.88, 0.94, 0.94, 0.91, 0.95, 0.94, 0.94, 0.89, 0.95, 0.9, 0.92, 0.9
],[])
# Expand each value by adding one before (value - 0.03) and one after (value + 0.03)
expanded_values = []
for v in values:
    expanded_values.extend([v - 0.03, v, v + 0.03])
values = np.array(expanded_values)

time = np.array([0, 0, 15, 30, 45, 60, 90, 120, 180, 240, 300, 360, 420])
time_error = np.array([0, 0, 3, 1,2,0,4,2,0,0,0,3,40])
time_real = time + time_error


# Agrupar los datos en listas para cada tiempo
grouped_values = [values[i*9:(i+1)*9] for i in range(len(time))]

# Crear la figura
plt.figure(figsize=(12, 6))


plt.boxplot(
    grouped_values,
    positions=time_real,
    widths=10,
    showfliers=False,
    notch=False,
    patch_artist=True,
    boxprops=dict(facecolor='gray', color='black'),
    medianprops=dict(color='blue'),
    whiskerprops=dict(color='black'),
    capprops=dict(color='black'),
    whis=[0, 100],
    )

# Agregar puntos individuales de cada muestra
#for i, t in enumerate(time):
    #plt.scatter([t]*3, grouped_values[i], color='black', alpha=0.7)

# Agregar una linea que conecte las medianas de cada grupo
medians = [np.median(group) for group in grouped_values]
plt.plot(
    time_real,
    medians,
    color='gray',
    marker='o',
    linestyle='dotted',
    markersize=1,
    label='Medianas')


# Ajustes finales
plt.xlabel('Tiempo de reacción (minutos)')
plt.xlim(-15, time.max()+60)  # Ajustar límites del eje X
plt.xticks(ticks=time,labels=time, rotation=45)  # Asegurar escala correcta del eje X


plt.ylabel('Volumen de titulación (ml)')
plt.ylim(round(min(values)), 4)  # Set y-axis limits
plt.yticks(np.linspace(round(min(values),1), round(max(values),0), 17))

plt.title('Volumen de titulación con NaOH 0,01M en función del tiempo de reacción a 80ºC \n para alicuotas de 100 uL del sistema Butanol, Ácido octanoico y PTSA·H2O')
#plt.legend()

plt.grid(True)
# Gráfico de cajas con posiciones correctas en eje X

plt.show()

