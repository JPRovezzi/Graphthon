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

times = np.array([])
for exp in data.time:
    times = np.append(times, exp)
time_max = times.max()

labels = ['80ºC', '70ºC', '60ºC','60ºC', '60ºC Tolueno']

colors = ['blue', 'green', 'red', 'red', 'purple']


if True:
    for index, df in enumerate(titration_results):
        if index in [0,1,3,4]:

            NaOH = 0.1  # mol / L
            alicuota = 0.1  # ml

            temperature = int(titration_results[index].description["temperature"])
            mixture_density = float(titration_results[index].data["d"].values[1])
            total_volume = (alcohol.mass + acid.mass + cat.mass) / mixture_density
            eq_butanol = (NaOH/1000)*(alcohol.density(temperature) * alcohol.mass /alicuota)*0.110
            eq_PTSA_old = (NaOH/1000)*(alcohol.density(temperature) * alcohol.mass/alicuota)*(0.753-0.110)
            eq_PTSA = (6.51/1.10)*(NaOH/1000)*((49.99/1.02)/1)*(1.15)
            print(f"{cat.mass_to_moles(cat.mass):.3f};{eq_PTSA:.3f};{eq_PTSA_old:.3f}")



            values = titration_results[index].data['vt_mean'][1:]
            # Multiplico el volumen de titulación por la concentración del NaOH para obtener los equivalentes cada 100 microlitros.
            values = values * (NaOH/1000) 

            values = values / alicuota    # Convertir a equivalentes por ml
            # Ajustar al volumen total de la reacción para obtener los equivalentes totales del sistema
            values = values * total_volume
            
            values = values - eq_PTSA  # Restar los equivalentes de PTSA·H2O


            # Equivalentes de ácido octanoico
            zero_value = (titration_results[index].data['vt_median'].values[0] * (NaOH/1000) * total_volume / alicuota )
            eq_octanoico =  zero_value - eq_butanol


            conversion = np.zeros(len(values)+1)
            for i, value in enumerate(values):
                conversion[i+1] = (eq_octanoico - value) / eq_octanoico * 100  # Conversión en porcentaje

            time_real = time[index] + time_error[index]


            print(len(conversion), len(time_real))
            print(conversion)
            print(time_real)
            
            # Graficar los resultados
            plt.plot(time_real, conversion, label=labels[index], color=colors[index], markersize=3, marker='o')
            plt.xlabel('Tiempo (minutos)')
            plt.ylabel('Conversión (%)')
            plt.title('Conversión de Ácido Octanoico a Butanol')
            plt.xticks(np.arange(0, time_max + 1, 30))
            plt.yticks(np.arange(0, 101, 5))
            plt.xlim(0, time_max+30)
            plt.ylim(0, 100)
            plt.grid(   which='both', linestyle='--', linewidth=0.5)
            plt.legend()


            


    plt.tight_layout()
    plt.show()

    plt.close()
#------------------------------------------------------------------------------
# Now I would like to plot blox plots of the conversion at 80ºC vs time. 
# Each box plot should represent the conversion at a specific time point, and the x-axis should represent the time points.
# The y-axis should represent the conversion percentage.
# To create box plots, we need to collect the conversion data at each time point for the 80ºC experiment.
# We have three titration per time point, so we can create a box plot for each time point: vt_01, vt_02, vt_03. 80ºC is the first index in titration_results.
# There will be len(titration_results[0].data) box plots, one for each time point.


for index, exp in enumerate(titration_results):
    if index not in [0,1,3,4]:
        continue
    
    # Calculate conversion for each titration at each time point for 80ºC (index 0)
    titr = titration_results[index]
    NaOH = 0.1  # mol / L
    alicuota = 0.1  # ml
    temperature = int(titr.description["temperature"])
    mixture_density = float(titr.data["d"].values[1])
    total_volume = (alcohol.mass + acid.mass + cat.mass) / mixture_density
    eq_butanol = (NaOH/1000)*(alcohol.density(temperature) * alcohol.mass /alicuota)*0.110
    eq_PTSA = (6.51/1.10)*(NaOH/1000)*((49.99/1.02)/1)*(1.15)

    # Equivalentes de ácido octanoico
    zero_value = (titr.data['vt_median'].values[0] * (NaOH/1000) * total_volume / alicuota )
    eq_octanoico =  zero_value

    # Collect conversion data for each titration at each time point
    conversion = []
    for i in range(len(titr.data)):
        conversions_at_time = []
        for vt_col in ['vt_01', 'vt_02', 'vt_03']:
            vt_value = titr.data[vt_col].values[i]
            eq_value = (vt_value * (NaOH/1000) * total_volume / alicuota) - eq_PTSA
            conversion_ = (eq_octanoico - eq_value) / eq_octanoico * 100
            conversions_at_time.append(conversion_)
        conversion.append(conversions_at_time)

    # Prepare time points for x-axis
    time_points = data.time[index]+data.time_error[index]

    #plt.figure()
    plt.boxplot(
        conversion,
        positions=time_points,
        label=labels[index],
        widths=10,
        patch_artist=True,
        boxprops=dict(facecolor='white', color=colors[index]),
        medianprops=dict(color=colors[index]),
        whiskerprops=dict(color=colors[index]),
        capprops=dict(color=colors[index]),
        flierprops=dict(marker='o', color=colors[index], markersize=5, linestyle='none'))


plt.xlabel('Tiempo (minutos)')
plt.ylabel('Conversión (%)')
plt.title('Conversión de Ácido Octanoico a Butanol')
plt.xticks(np.arange(0, int(time_max+30), 30),np.arange(0, int(time_max+30), 30))
plt.yticks(np.arange(0, 101, 5))
plt.xlim(0, int(time_max+30))
plt.ylim(0, 100)
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()


#------------------------------------------------------------------------------
# Plot both the box plots and the line plots together in a single figure.
plt.figure(figsize=(10, 6))
# Plot line plots for each experiment
for index, df in enumerate(titration_results):
    if index in [0,1,3,4]:
        NaOH = 0.1  # mol / L
        alicuota = 0.1  # ml

        temperature = int(titration_results[index].description["temperature"])
        mixture_density = float(titration_results[index].data["d"].values[1])
        total_volume = (alcohol.mass + acid.mass + cat.mass) / mixture_density
        eq_butanol = (NaOH/1000)*(alcohol.density(temperature) * alcohol.mass /alicuota)*0.110
        eq_PTSA = (6.51/1.10)*(NaOH/1000)*((49.99/1.02)/1)*(1.15)

        values = titration_results[index].data['vt_mean'][1:]
        values = values * (NaOH/1000) 
        values = values / alicuota    
        values = values * total_volume
        values = values - eq_PTSA

        zero_value = (titration_results[index].data['vt_median'].values[0] * (NaOH/1000) * total_volume / alicuota )
        eq_octanoico =  zero_value - eq_butanol

        conversion = np.zeros(len(values)+1)
        for i, value in enumerate(values):
            conversion[i+1] = (eq_octanoico - value) / eq_octanoico * 100  # Conversión en porcentaje

        time_real = data.time[index] + data.time_error[index]

        plt.plot(time_real, conversion, label=labels[index], color=colors[index], markersize=3, marker='o')
# Plot box plots for each experiment
for index, exp in enumerate(titration_results):
    if index not in [0,1,3,4]:
        continue
    titr = titration_results[index]
    NaOH = 0.1  # mol / L
    alicuota = 0.1  # ml
    temperature = int(titr.description["temperature"])
    mixture_density = float(titr.data["d"].values[1])
    total_volume = (alcohol.mass + acid.mass + cat.mass) / mixture_density
    eq_butanol = (NaOH/1000)*(alcohol.density(temperature) * alcohol.mass /alicuota)*0.110
    eq_PTSA = (6.51/1.10)*(NaOH/1000)*((49.99/1.02)/1)*(1.15)
    zero_value = (titr.data['vt_median'].values[0] * (NaOH/1000) * total_volume / alicuota )
    eq_octanoico =  zero_value
    conversion = []
    for i in range(len(titr.data)):
        conversions_at_time = []
        for vt_col in ['vt_01', 'vt_02', 'vt_03']:
            vt_value = titr.data[vt_col].values[i]
            eq_value = (vt_value * (NaOH/1000) * total_volume / alicuota) - eq_PTSA
            conversion_ = (eq_octanoico - eq_value) / eq_octanoico * 100
            conversions_at_time.append(conversion_)
        conversion.append(conversions_at_time)
    time_points = data.time[index]+data.time_error[index]
    plt.boxplot(
        conversion,
        positions=time_points,
        label=labels[index],
        widths=10,
        patch_artist=True,
        boxprops=dict(facecolor='white', color=colors[index]),
        medianprops=dict(color=colors[index]),
        whiskerprops=dict(color=colors[index]),
        capprops=dict(color=colors[index]),
        flierprops=dict(marker='o', color=colors[index], markersize=5, linestyle='none'))
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Conversión (%)')
plt.title('Conversión de Ácido Octanoico a Butanol')
plt.xticks(np.arange(0, int(time_max+30), 30), np.arange(0, int(time_max+30), 30))
plt.yticks(np.arange(0, 101, 5))
plt.xlim(0, int(time_max+30))
plt.ylim(0, 100)
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()

            
