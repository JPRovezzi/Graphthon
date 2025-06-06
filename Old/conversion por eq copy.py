#Carga de las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from data import tiritation, time, time_error
from classes import *
#------------------------------------------------------------------------------

# Datos experimentales
temperatures = np.array([80,70,60,60,25])  # Temperaturas en ºC
mixture_density = np.array([0.74,(0.74+0.79)/2,0.79,0.79])

alcohol= Butanol(mass=40.27*0.994)  # Masa de Butanol en gramos
acid = OctanoicAcid(mass=79.46*0.98)  # Masa de Ácido octanoico en gramos
cat = PTSA·H2O(mass=6.51)  # Masa de PTSA·H2O en gramos (no se usa en este cálculo)



system = System(alcohol, acid, cat, temperature=25, volume=None)  # Crear el sistema de reacción a 60ºC

# Calcular el volumen maximo y minimo por la densidad
total_mass = alcohol.mass + acid.mass + cat.mass  # Masa total de la mezcla
reaction_mass =  alcohol.mass + acid.mass # Masa de los reactivos sin PTSA·H2O ni solvente
volume_max = reaction_mass / mixture_density[0]  # Volumen máximo en ml
volume_min = reaction_mass / mixture_density[1]  # Volumen mínimo en ml

print("Sistema de reacción:")
print(f"Alcohol: {alcohol.name} ({alcohol.mass:.2f} g, {alcohol.moles:.2f} moles)")
print(f"Ácido: {acid.name} ({acid.mass:.2f} g, {acid.moles:.2f} moles)")
print(f"Catálisis: {cat.name} ({cat.mass:.2f} g, {cat.moles:.2f} moles)")
print(f"Masa total de la mezcla: {total_mass:.2f} g")
print(f"Masa de los reactivos: {reaction_mass:.2f} g")
print("Relaciones")
print(f"Relación molar Butanol/Ácido: {alcohol.moles/acid.moles:.2f}")
print(f"Relación molar Butanol/PTSA·H2O: {alcohol.moles/cat.moles:.2f}")
print(f"Relación molar Ácido/PTSA·H2O: {acid.moles/cat.moles:.2f}")
print(f"Fracción molar Butanol: {system.x_alcohol:.2f}")
print(f"Fracción molar Ácido: {system.x_acid:.2f}")
print(f"Fracción molar PTSA·H2O: {system.x_catalyst:.2f}")
print(f"Fracción másica Butanol: {system.w_alcohol:.2f}")
print(f"Fracción másica Ácido: {system.w_acid:.2f}")
print(f"Fracción másica PTSA·H2O: {system.w_catalyst:.2f}")
print(f"Fracción molar ácida del Ácido: {system.xacid_acid:.2f}")
print(f"Fracción molar ácida del PTSA·H2O: {system.xacid_catalyst:.2f}")




for temperature in temperatures:
    # Calcular la densidad del butanol y del ácido octanoico a la temperatura dada
    butanol_density = alcohol.density(temperature)
    acid_density = acid.density(temperature)
    
    # Calcular el volumen de cada compuesto a la temperatura dada
    butanol_volume = alcohol.mass_to_volume(temperature=temperature)
    acid_volume = acid.mass_to_volume(temperature=temperature)
    
    print(f"Temperatura: {temperature} ºC")
    print(f"Densidad de Butanol: {butanol_density:.2f} g/ml")
    print(f"Densidad de Ácido Octanoico: {acid_density:.2f} g/ml")
    print(f"Volumen de Butanol: {butanol_volume:.2f} ml")
    print(f"Volumen de Ácido Octanoico: {acid_volume:.2f} ml")
    print(f"Volumen aditivo total de la mezcla: {acid_volume+butanol_volume:.2f} ml")
    print(f"Volumen máximo de la mezcla: {volume_max:.2f} ml")
    print(f"Volumen mínimo de la mezcla: {volume_min:.2f} ml")
    print("-" * 40)





labels = ['80ºC', '70ºC', '60ºC','60ºC']

colors = ['blue', 'green', 'red', 'red']
# Crear la figura
plt.figure(figsize=(12, 6))

for index,values in enumerate(tiritation):
    if index in [0,1,3]:
        
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

