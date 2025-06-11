#Carga de las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import data
from classes import *
#------------------------------------------------------------------------------

# Datos experimentales


alcohol= Butanol(mass=40.27*0.994)  # Masa de Butanol en gramos
acid = OctanoicAcid(mass=79.46*0.98)  # Masa de Ácido octanoico en gramos
cat = PTSA·H2O(mass=6.51)  # Masa de PTSA·H2O en gramos (no se usa en este cálculo)


titration_results = data.get_results()


labels = ['80ºC', '70ºC', '60ºC','60ºC']

colors = ['blue', 'green', 'red', 'red']
# Crear la figura
plt.figure(figsize=(12, 6))

for index,values in enumerate(titration_results):
    if index in [0,1,3]:
        system = System(alcohol, acid, cat, temperature=temperatures[index], volume=total_volume)
        expanded_values = []
        NaOH = 0.1
        
        alicuota=0.1

        # Expand each value by adding one before (value - 0.03) and one after (value + 0.03)
        for v in values:
            expanded_values.extend([v - 0.03, v, v + 0.03])
        values = np.array(expanded_values)
        # Multiplico el volumen de titulación por la concentración del NaOH para obtener los equivalentes cada 100 microlitros.
        values = values * (NaOH/1000) 

        values = values / alicuota    # Convertir a equivalentes por ml
        
        # Multiplico por el volumen total
        total_volume = system.total_mass / mixture_density[index] # Volumen total de la mezcla en ml a la temperatura dada
        system = System(alcohol, acid, cat, temperature=temperatures[index], volume=total_volume)
        # Ajustar al volumen total de la reacción para obtener los equivalentes totales del sistema
        values = values * total_volume 

        
        eq_butanol = (NaOH/1000)*(system.volume_alcohol/alicuota)*0.110
        eq_PTSA_old = (NaOH/1000)*(system.volume_alcohol/alicuota)*(0.753-0.110)
        eq_PTSA = (6.51/1.10)*(NaOH/1000)*((49.99/1.02)/1)*(1.15)
        print(f"{system.catalyst.moles:.3f};{eq_PTSA:.3f};{eq_PTSA_old:.3f}")

        # Mi valor 
        #zero_value = values[0] - eq_butanol + eq_PTSA  # Valor inicial de equivalentes a 0 minutos
        zero_value = values[0]

        eq_octanoico =  zero_value




        values = (
            (zero_value) - (values - eq_PTSA)) *100 / (eq_octanoico)  


        

        
 
        
        
        time_real = time + time_error[index]

        # Agrupar los datos en listas para cada tiempo
        grouped_values = [values[i*9:(i+1)*9] for i in range(len(time))]




        plt.boxplot(
            grouped_values[1:],
            positions=time_real[1:],
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
        if True:
            medians = [np.median(group) for group in grouped_values[1:]]
            plt.plot(
                time_real[1:],
                medians,
                color=colors[index],
                marker='o',
                linestyle='dotted',
                markersize=1,
                #label='Medianas'
                )


# Ajustes finales
plt.xlabel('Tiempo de reacción (minutos)')
plt.xlim(-15, time.max()+60)  # Ajustar límites del eje X
plt.xticks(ticks=time,labels=time, rotation=45)  # Asegurar escala correcta del eje X


plt.ylabel('Conversión (%)')
plt.ylim(0, 105)  # Set y-axis limits
#plt.yticks(np.linspace(0.80, 4.00, 17))
plt.yticks(np.linspace(0, 100, 21))

plt.title('Conversión función del tiempo de reacción \n para alicuotas del sistema Butanol, Ácido octanoico y PTSA·H2O')
plt.legend()

plt.grid(True)
# Gráfico de cajas con posiciones correctas en eje X

plt.show()

