import numpy as np
import matplotlib.pyplot as plt
from data import time, time_error
# Datos proporcionados

weights = [
    # 80ºC Reaction
    # 80ºC Empty
    np.array([
        0.87195,0.87195,0.87195,

        0.84582,0.89385,0.86690,
        0.86810,0.87454,0.87636,
        0.86485

    ]),
    # 80ºC Filled
    np.array([
        0.94593,0.94593,0.94593,

        0.92413,0.96705,0.94823,
        0.94212,0.95798,0.95439,
        0.94255

    ]),
    # 80ºC TwoPhases
    # Empty
    np.array([
        0.86963,0.88239
    ]),
    # Filled
    np.array([
        0.94025,0.99702
    ]),
    # 70ºC Reaction
    # 70ºC Empty
    np.array([
    ]),
    # 70ºC Filled
    np.array([

    ]),
    # 70ºC TwoPhases
    # Empty
    np.array([

    ]),
    # Filled
    np.array([
    ]),
    # 60ºC Reaction
    # 60ºC Empty
    np.array([
        0.86454,0.85173,0.89721,
        0,0,0,
        0,0,0,
        0,0,0,
        0,0,0,
        0.86500,0.87305,0.86594,
        0,0,0,
        0.87042,0.88489,0.88329,
        0,0,0,
        0,0,0,
        0.87577,0.89495,0.85190,
        0,0,0,
        0.89094,0.86164,0.79512
    ]),
    # 60ºC Filled
    np.array([
        0.94374,0.92961,0.97819,
        0,0,0,
        0,0,0,
        0,0,0,
        0,0,0,
        0.94562,0.94971,0.94631,
        0,0,0,
        0.94839,0.96504,0.96426,
        0,0,0,
        0,0,0,
        0.95601,0.97738,0.93304,
        0,0,0,
        0.97030,0.94071,0.87527,
    ]),
    # 60ºC TwoPhases
    # Empty
    np.array([
        1.02097,0.90546
    ]),
    # Filled
    np.array([
        1.09563,1.00515
    ]),
]


labels = ['80ºC','70ºC','60ºC']

colors = ['blue','green','red']
# Crear la figura
plt.figure(figsize=(12, 6))

for index,values in enumerate(weights):
    if index in [0,8]:
        if True:
            #empty = []
            #for v in values:
                #empty.extend([v - 0.00001, v, v + 0.00001])
            #filled = []
            #for v in weights[index + 1]:
                #filled.extend([v - 0.00001, v, v + 0.00001])
            #filled = np.array(filled)
            #empty = np.array(empty)
            #vpt = 9 # Number of values per time point
            # Agrupar los datos en listas para cada tiempo
            #grouped_values = [values[i*vpt:(i+1)*vpt] for i in range(len(time))]
            #time_real = time + time_error[2]
            
            empty = weights[index]
            filled = weights[index + 1]
            
            values = (filled-empty)/ 0.1  # Subtract the empty weight from the filled weight
            tpos = int(index / 4)  # Determine the position based on index


            # Excluir valores cero de cada grupo
            grouped_values = []
            for group in [values[:3], values[3:]]:
                nonzero_group = [v for v in group if v != 0]
                grouped_values.append(nonzero_group)

            values = (weights[index+3] - weights[index+2]) / 0.1
            for group in [values[:1], values[1:]]:
                nonzero_group = [v for v in group if v != 0]
                grouped_values.append(nonzero_group)
        
            if index == 0:
                positions = [0, 3, 3, 3]
            elif index == 8:
                positions = [2, 5, 5, 5]
            plt.boxplot(
                grouped_values,
                positions=positions,
                #widths=10,
                showfliers=False,
                notch=False,
                patch_artist=False,
                boxprops=dict(
                    # facecolor='gray', 
                    color=colors[tpos]),
                medianprops=dict(color=colors[tpos],),
                whiskerprops=dict(color=colors[tpos],),
                capprops=dict(color=colors[tpos],),
                whis=[0, 100],
                label=labels[tpos],
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
plt.xlabel('Tiempo')
#plt.xlim(-15, time.max()+60)  # Ajustar límites del eje X
#plt.xticks(ticks=time,labels=time, rotation=45)  # Asegurar escala correcta del eje X
plt.xticks(ticks=[
    0,1,2,3,4,5],
           labels=[
               "COOH+COH\n80ºC",
               "COOH+COH\n70ºC",
               "COOH+COH\n60ºC",
               "R\n80ºC",
               "R\n70ºC",
               "R\n60ºC"], rotation=0)

plt.ylabel('densidad (g/mL)')
plt.ylim(0.7, 1.2)  # Set y-axis limits
#plt.yticks(np.linspace(0.80, 4.00, 17))
#plt.yticks(np.linspace(0.80, 5, 22))

#plt.title('Volumen de titulación con NaOH 0,1M en función del tiempo de reacción \n para alicuotas de 100 uL del sistema Butanol, Ácido octanoico y PTSA·H2O')
plt.legend()

plt.grid(True)
# Gráfico de cajas con posiciones correctas en eje X

plt.show()

