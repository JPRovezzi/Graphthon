import numpy as np
import matplotlib.pyplot as plt
from data import tiritation, time, time_error
# Datos proporcionados

density = np.array([0.78,0.80])

#mass = np.array([butanol, octanoico,solvente, PTSA·H2O]) 
comp_mass = np.array([40.27, 79.46,0,6.51])  # Masa de los reactivos en gramos
comp_density = [
    np.array([0.81, 0.91, 0, 0]), #25ºC
    np.array([0.7783, 0.91, 0, 0]), #60ºC
    np.array([0., 0.91, 0, 0]), #70ºC
    np.array([0.81, 0.91, 0, 0])  #80ºC
    ]  # Densidad de los reactivos en g/ml
# Calcular el volumen maximo y minimo por la densidad
total_mass = comp_mass.sum()  # Masa total de los reactivos
reaction_mass = comp_mass[:2].sum()  # Masa de los reactivos sin PTSA·H2O ni solvente
additive_volume = comp_mass[0] / comp_density[0] + comp_mass[1] / comp_density[1]  # Volumen aditivo de COOH y COH en ml
volume_max = reaction_mass / density[0]  # Volumen máximo en ml
volume_min = reaction_mass / density[1]  # Volumen mínimo en ml
total_volume = additive_volume
'''
print("Volumen de COH a 25ºC: {:.2f} ml".format(comp_mass[0] / comp_density[0]))
print("Volumen de COOH a 25ºC: {:.2f} ml".format(comp_mass[1] / comp_density[1]))
print("Volumen aditivo de (COOH + COH) a 25ºC: {:.2f} ml".format(comp_mass[0] / comp_density[0] + comp_mass[1] / comp_density[1]))
print("Densidad máxima (COOH + COH) a 60ºC: {:.2f} g/ml".format(density[1]))
print("Densidad mínima (COOH + COH)a 60ºC: {:.2f} g/ml".format(density[0]))
print(f'Volumen maximo (COOH + COH) a 60ºC: {volume_max:.2f} ml \n Volumen minimo a 60ºC: {volume_min:.2f} ml')
'''



labels = ['80ºC', '70ºC', '60ºC','60ºC']

colors = ['blue', 'green', 'red', 'red']
# Crear la figura
plt.figure(figsize=(12, 6))

for index,values in enumerate(tiritation):
    if index in [0,1,3]:
        # Ajusto los valores de titulación a la concentración del NaOH como si fuera 0.1M
        values = values / (0.089/0.1)
        # Multiplico el volumen de titulación por la concentración del NaOH para obtener los equivalentes cada 100 microlitros.
        values = values * 0.1  # Ajustar a la concentración del NaOH (0.1M)
        # Multiplico los equivalentes por 10 para obtener los equivalentes por ml
        values = values * 10  # Convertir a equivalentes por ml
        # Multiplico por el volumen total

        values = values * total_volume  # Ajustar al volumen total de la reacción para obtener los equivalentes totales del sistema




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

