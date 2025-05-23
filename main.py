import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
values_old = np.array([
    3.84, 3.84, 3.72, 3.4, 3.38, 3.38, 1.53, 1.43, 1.5, 1.35, 1.23, 1.34, 1.16,
    1.1, 1.15, 1.16, 1.18, 1.13, 1.1, 1.08, 1.04, 1.01, 0.99, 1.03, 1, 0.96,
    0.97, 0.88, 0.94, 0.94, 0.91, 0.95, 0.94, 0.94, 0.89, 0.95, 0.9, 0.92, 0.9
])
time = np.array([0, 0, 15, 30, 45, 60, 90, 120, 180, 240, 300, 360, 420])
# Si tienes un array de tamaño 2, por ejemplo:
arrays = [
    np.array([
    3.84, 3.84, 3.72, 
    3.4, 3.38, 3.38, 
    1.53, 1.43, 1.5, 
    1.35, 1.23, 1.34, 
    1.16, 1.1, 1.15, 
    1.16, 1.18, 1.13,
    1.1, 1.08, 1.04,
    1.01, 0.99, 1.03,
    1, 0.96, 0.97,
    0.88, 0.94, 0.94,
    0.91, 0.95, 0.94,
    0.94, 0.89, 0.95,
    0.9, 0.92, 0.9
    ]),
    np.array([
    3.75,3.88,3.84,
    3.45,3.50,3.67,
    1.86,2.18,1.87,
    1.73,1.90,1.60,
    1.50,1.44,1.70,
    1.70,1.37,1.30,
    1.51,1.29,1.32,
    1.25,1.19,1.22,
    1.06,1.28,1.10,
    1.06,1.12,1.08,
    1.04,1.05,1.05,
    1.01,1,1,
    0.96,0.96,0.97
    ]),
    np.array([
    4.12,4.40,4.40,
    0.00,0.00,0.00,
    2.81,2.78,2.34,
    2.17,2.00,2.07,
    1.93,1.48,1.40,
    1.67,1.21,1.55,
    1.31,0.93,1.11,
    1.40,1.43,1.08,
    1.33,0.96,1.07,
    0.90,1.04,1.25,
    0.82,0.84,0.98,
    0,0,0,
    0,0,0,
    ]),
    ]  # Reemplaza [...] con tus datos


time_error = [
    np.array([-0,0,3, 1,2,0,4,2,0,0,0,3,40]),
    np.array([-0,0,3,-1,0,0,1,0,0,0,4,0,0]),
    np.array([-0,0,0,1,2,1,0,2,0,2,-1,0,0])
    ]

colors = ['blue', 'green', 'red']
# Crear la figura
plt.figure(figsize=(12, 6))

for index,values in enumerate(arrays):
    # Expand each value by adding one before (value - 0.03) and one after (value + 0.03)
    expanded_values = []
    for v in values:
        expanded_values.extend([v - 0.03, v, v + 0.03])
    values = np.array(expanded_values)
    
    time_real = time + time_error[index]

    # Agrupar los datos en listas para cada tiempo
    grouped_values = [values[i*9:(i+1)*9] for i in range(len(time))]




    plt.boxplot(
        grouped_values,
        positions=time_real,
        widths=10,
        showfliers=False,
        notch=False,
        patch_artist=False,
        boxprops=dict(
            # facecolor='gray', 
            color=colors[index],),
        medianprops=dict(color=colors[index],),
        whiskerprops=dict(color=colors[index],),
        capprops=dict(color=colors[index],),
        whis=[0, 100],
        )

    # Agregar puntos individuales de cada muestra
    #for i, t in enumerate(time):
        #plt.scatter([t]*3, grouped_values[i], color='black', alpha=0.7)

    # Agregar una linea que conecte las medianas de cada grupo
    if False:
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
plt.ylim(0.80, 4)  # Set y-axis limits
#plt.yticks(np.linspace(0.80, 4.00, 17))
plt.yticks(np.linspace(0.80, 4.60, 20))

plt.title('Volumen de titulación con NaOH 0,01M en función del tiempo de reacción a 80ºC \n para alicuotas de 100 uL del sistema Butanol, Ácido octanoico y PTSA·H2O')
#plt.legend()

plt.grid(True)
# Gráfico de cajas con posiciones correctas en eje X

plt.show()

