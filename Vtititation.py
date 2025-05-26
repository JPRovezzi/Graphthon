import numpy as np
import matplotlib.pyplot as plt
from data import tiritation, time, time_error
# Datos proporcionados



labels = ['80ºC', '70ºC', '60ºC','60ºC']

colors = ['blue', 'green', 'red', 'red']
# Crear la figura
plt.figure(figsize=(12, 6))

for index,values in enumerate(tiritation):
    if index in [0,1,3]:
        values = values / (0.089/0.1)
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
            label=labels[index],
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
plt.yticks(np.linspace(0.80, 5, 22))

plt.title('Volumen de titulación con NaOH 0,1M en función del tiempo de reacción \n para alicuotas de 100 uL del sistema Butanol, Ácido octanoico y PTSA·H2O')
plt.legend()

plt.grid(True)
# Gráfico de cajas con posiciones correctas en eje X

plt.show()

