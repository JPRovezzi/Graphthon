import numpy as np
import matplotlib.pyplot as plt
from data import tiritation, time, time_error
# Datos proporcionados

class Compound:
    def __init__(self, name, molar_mass, mass=0., moles=0.):
        """
        Inicializa un compuesto químico.
        :param name: Nombre del compuesto.
        :param molar_mass: Masa molar del compuesto en g/mol.
        :param mass: Masa del compuesto en gramos (opcional, por defecto 0).
        :param moles: Moles del compuesto (opcional, por defecto 0).
        """
        if mass < 0 or moles < 0:
            raise ValueError("La masa y los moles deben ser mayores o iguales a cero.")
        if mass != 0 and moles != 0:
            raise ValueError("Debe proporcionar solo uno de los parámetros: masa o moles.")
        
        self.name = name
        self.molar_mass = molar_mass  # g/mol
        self.moles = moles if moles != 0 else mass / molar_mass  # moles
        self.mass = mass if mass != 0 else molar_mass * moles # g

        
    def __repr__(self):
        return f"{self.name} (Masa molar: {self.molar_mass} g/mol, Masa: {self.mass} g)"
    def __str__(self):
        return f"{self.name} (Masa molar: {self.molar_mass} g/mol, Masa: {self.mass} g)"
    def density(self, temperature, unit="celsius", r_squared=False):
        """Calcula la densidad del compuesto a partir de la temperatura en ºC."""
        raise NotImplementedError("Este método debe ser implementado en las subclases.")
    def molecular_weight(self):
        """Devuelve la masa molar del compuesto."""
        return self.molar_mass
    def mass_to_moles(self, mass):
        """Convierte la masa del compuesto a moles."""
        if mass < 0:
            raise ValueError("La masa debe ser mayor o igual a cero.")
        return mass / self.molar_mass
    def moles_to_mass(self, moles):
        """Convierte los moles del compuesto a masa."""
        if moles < 0:
            raise ValueError("Los moles deben ser mayores o iguales a cero.")
        return moles * self.molar_mass
    def moles_to_volume(self, moles = None, temperature =25, unit="celsius"):
        """Convierte los moles del compuesto a volumen a partir de
        la temperatura en ºC."""
        if self.density(temperature, unit) <= 0:
            raise ValueError("La densidad debe ser mayor que cero para calcular el volumen.")
        if moles <= 0 or moles is None:
            moles = self.moles
        if self.moles < 0:
            raise ValueError("Los moles deben ser mayores o iguales a cero.")
        return self.moles * self.molar_mass / self.density(temperature, unit)
    def mass_to_volume(self, mass = None,temperature=25, unit="celsius"):
        """Convierte la masa del compuesto a volumen a partir de
        la temperatura en ºC."""
        if self.density(temperature, unit) <= 0:
            raise ValueError("La densidad debe ser mayor que cero para calcular el volumen.")

        if mass is None:
            mass = self.mass
        if mass <= 0:
            mass = self.mass
        if self.mass < 0:
            raise ValueError("La masa debe ser mayor o igual a cero.")
        return self.mass / self.density(temperature, unit)
    def volume_to_moles(self, volume, temperature, unit="celsius"):
        """Convierte el volumen del compuesto a moles a partir de
        la temperatura en ºC."""
        if self.density(temperature, unit) <= 0:
            raise ValueError("La densidad debe ser mayor que cero para calcular los moles.")
        return volume * self.density(temperature, unit) / self.molar_mass
    def volume_to_mass(self, volume, temperature, unit="celsius"):
        """Convierte el volumen del compuesto a masa a partir de
        la temperatura en ºC."""
        if self.density(temperature, unit) <= 0:
            raise ValueError("La densidad debe ser mayor que cero para calcular la masa.")
        return volume * self.density(temperature, unit)
    def temperature_conversion(self, temperature, from_unit, to_unit):
        """Convierte la temperatura entre diferentes unidades."""
        if from_unit == "celsius":
            if to_unit == "celsius":
                return temperature
            if to_unit == "kelvin":
                return temperature + 273.15
            elif to_unit == "fahrenheit":
                return (temperature * 9/5) + 32
            elif to_unit == "rankine":
                return (temperature + 273.15) * 9/5
            elif to_unit == "delisle":
                return (100 - temperature) * 3/2
            elif to_unit == "newton":
                return temperature * 33/100
            elif to_unit == "reaumur":
                return temperature * 4/5
            elif to_unit == "romer":
                return (temperature * 21/40) + 7.5
            else:
                raise ValueError("Unidad de temperatura no reconocida.")
        if from_unit == "kelvin":
            if to_unit == "kelvin":
                return temperature
            if to_unit == "celsius":
                return temperature - 273.15
            elif to_unit == "fahrenheit":
                return (temperature - 273.15) * 9/5 + 32
            elif to_unit == "rankine":
                return temperature * 9/5
            elif to_unit == "delisle":
                return (373.15 - temperature) * 3/2
            elif to_unit == "newton":
                return (temperature - 273.15) * 33/100
            elif to_unit == "reaumur":
                return (temperature - 273.15) * 4/5
            elif to_unit == "romer":
                return ((temperature - 273.15) * 21/40) + 7.5
            else:
                raise ValueError("Unidad de temperatura no reconocida.")
        if from_unit == "fahrenheit":
            if to_unit == "fahrenheit":
                return temperature
            if to_unit == "celsius":
                return (temperature - 32) * 5/9
            elif to_unit == "kelvin":
                return (temperature - 32) * 5/9 + 273.15
            elif to_unit == "rankine":
                return temperature + 459.67
            elif to_unit == "delisle":
                return (212 - temperature) * 5/6
            elif to_unit == "newton":
                return (temperature - 32) * 11/60
            elif to_unit == "reaumur":
                return (temperature - 32) * 4/9
            elif to_unit == "romer":
                return (temperature - 32) * 7/24 + 7.5
            else:
                raise ValueError("Unidad de temperatura no reconocida.")
        if from_unit == "rankine":
            if to_unit == "rankine":
                return temperature
            if to_unit == "celsius":
                return (temperature - 491.67) * 5/9
            elif to_unit == "kelvin":
                return temperature * 5/9
            elif to_unit == "fahrenheit":
                return temperature - 459.67
            elif to_unit == "delisle":
                return (671.67 - temperature) * 5/6
            elif to_unit == "newton":
                return (temperature - 491.67) * 11/60
            elif to_unit == "reaumur":
                return (temperature - 491.67) * 4/9
            elif to_unit == "romer":
                return (temperature - 491.67) * 7/24 + 7.5
            else:
                raise ValueError("Unidad de temperatura no reconocida.")
        if from_unit == "delisle":
            if to_unit == "delisle":
                return temperature
            if to_unit == "celsius":
                return 100 - (temperature * 2/3)
            elif to_unit == "kelvin":
                return 373.15 - (temperature * 2/3)
            elif to_unit == "fahrenheit":
                return (212 - (temperature * 2/3)) * 9/5 + 32
            elif to_unit == "rankine":
                return (671.67 - (temperature * 2/3)) * 9/5
            elif to_unit == "newton":
                return (100 - (temperature * 2/3)) * 33/100
            elif to_unit == "reaumur":
                return (100 - (temperature * 2/3)) * 4/5
            elif to_unit == "romer":
                return ((100 - (temperature * 2/3)) * 21/40) + 7.5
            else:
                raise ValueError("Unidad de temperatura no reconocida.")
            

        if from_unit == "newton":
            if to_unit == "newton":
                return temperature
            if to_unit == "celsius":
                return temperature * 100/33
            elif to_unit == "kelvin":
                return (temperature * 100/33) + 273.15
            elif to_unit == "fahrenheit":
                return (temperature * 100/33) * 9/5 + 32
            elif to_unit == "rankine":
                return (temperature * 100/33) * 9/5 + 491.67
            elif to_unit == "delisle":
                return (100 - (temperature * 100/33)) * 3/2
            elif to_unit == "reaumur":
                return temperature * 4/5
            elif to_unit == "romer":
                return (temperature * 100/33) * 7/24 + 7.5
            else:
                raise ValueError("Unidad de temperatura no reconocida.")
        if from_unit == "reaumur":
            if to_unit == "reaumur":
                return temperature
            if to_unit == "celsius":
                return temperature * 5/4
            elif to_unit == "kelvin":
                return (temperature * 5/4) + 273.15
            elif to_unit == "fahrenheit":
                return (temperature * 5/4) * 9/5 + 32
            elif to_unit == "rankine":
                return (temperature * 5/4) * 9/5 + 491.67
            elif to_unit == "delisle":
                return (100 - (temperature * 5/4)) * 3/2
            elif to_unit == "newton":
                return temperature * 33/100
            elif to_unit == "romer":
                return (temperature * 5/4) * 7/24 + 7.5
            else:
                raise ValueError("Unidad de temperatura no reconocida.")
        if from_unit == "romer":
            if to_unit == "romer":
                return temperature
            if to_unit == "celsius":
                return (temperature - 7.5) * 40/21
            elif to_unit == "kelvin":
                return ((temperature - 7.5) * 40/21) + 273.15
            elif to_unit == "fahrenheit":
                return ((temperature - 7.5) * 40/21) * 9/5 + 32
            elif to_unit == "rankine":
                return ((temperature - 7.5) * 40/21) * 9/5 + 491.67
            elif to_unit == "delisle":
                return (100 - ((temperature - 7.5) * 40/21)) * 3/2
            elif to_unit == "newton":
                return ((temperature - 7.5) * 40/21) * 33/100
            elif to_unit == "reaumur":
                return (temperature - 7.5) * 40/21 * 4/5
            else:
                raise ValueError("Unidad de temperatura no reconocida.")
        else:
            raise ValueError("Unidad de temperatura no reconocida.")
            
class OctanoicAcid(Compound):
    def __init__(self, mass=0., moles=0.):
        super().__init__("Ácido octanoico", 144.22, mass=mass, moles=moles)
    def density(self, temperature,unit="celsius", r_squared=False):
        """Calcula la densidad del ácido octanoico en g/ml a partir de la temperatura en ºC."""
        # Valores de temperatura y densidad del ácido octanoico
        # Estos valores son aproximados y deben ser ajustados según la fuente de datos de Bernado-Gil et al. 1990
        values = np.array([
            20.1293,0.907267,
            25.3839,0.904286,
            30.2648,0.900559,
            35.7069,0.897578,
            40.2127,0.893851,
            45.2811,0.890124,
            50.1619,0.886398,])
        
        # Convertir la temperatura a Celsius si es necesario
        
        temperature = self.temperature_conversion(
            temperature, from_unit = "celsius", to_unit= unit)

        temperatures = values[0::2]  # Temperaturas en ºC
        densities = values[1::2]  # Densidades en g/ml
        # Obtener los coeficientes de la regresión lineal
        coeffs = np.polyfit(temperatures, densities, 1)
        # Calcular la densidad a la temperatura dada
        density = np.polyval(coeffs, temperature)
        # obtener el R^2 para evaluar la calidad del ajuste
        r_squared = np.corrcoef(temperatures, densities)[0, 1]**2
        return density


class Butanol(Compound):
    def __init__(self, mass=0., moles=0.):
        super().__init__("Butanol", 74.12, mass=mass, moles=moles)

    def density(self, temperature, unit="celsius", r_squared=False):
        """Calcula la densidad del butanol en g/ml a partir de la temperatura en ºC."""
        # Valores de temperatura y densidad del butanol
        vals = np.array([
            293.15,0.8095, 
            303.15,0.8020, 
            313.15,0.7941, 
            323.15,0.7865, 
            333.15,0.7783, 
            343.15,0.7699, 
            353.15,0.7609, 
            363.15,0.7519, 
            373.15,0.7424, 
            383.15,0.7322,
        ])
        # Extraer las temperaturas y densidades de los valores
        temps = vals[::2]  # Temperaturas en K
        celcius_temperatures = []
        # Convertir las temperaturas de Kelvin a Celsius
        for temp in temps:
            # Convertir la temperatura a Celsius si es necesario
            temp = self.temperature_conversion(temp, 
            from_unit="kelvin", to_unit=unit)
            celcius_temperatures.append(temp)
        temps = celcius_temperatures
        densities = vals[1::2]  # Densidades en g/ml
        # Obtener los coeficientes de la regresión lineal
        coeffs = np.polyfit(temps, densities, 1)
        # Calcular la densidad a la temperatura dada
        density = np.polyval(coeffs, temperature)
                # obtener el R^2 para evaluar la calidad del ajuste
        r_squared = np.corrcoef(temps, densities)[0, 1]**2
        return density

class PTSA·H2O(Compound):
    def __init__(self,mass=0, moles=0):
        super().__init__("PTSA·H2O", 190.22, mass=mass, moles=moles)

    def density(self, temperature, unit="celsius", r_squared=False):
        """Calcula la densidad del PTSA·H2O en g/ml a partir de la temperatura en ºC."""
        raise NotImplementedError("La densidad del PTSA·H2O no está implementada. Por favor, proporcione los datos necesarios.")
class PTSA(Compound):
    def __init__(self,mass=0, moles=0):
        super().__init__("PTSA", 172.19,mass=mass, moles=moles)

    def density(self, temperature, unit="celsius", r_squared=False):
        """Calcula la densidad del PTSA en g/ml a partir de la temperatura en ºC."""
        raise NotImplementedError("La densidad del PTSA no está implementada. Por favor, proporcione los datos necesarios.")

class System:
    def __init__(self, alcohol, acid, catalyst, temperature=25, volume=None):
        """
        Inicializa un sistema de reacción con un alcohol, un ácido y un catalizador.
        :param alcohol: Compuesto de tipo Alcohol.
        :param acid: Compuesto de tipo Ácido.
        :param catalyst: Compuesto de tipo Catalizador.
        """
        self.alcohol = alcohol
        self.acid = acid
        self.catalyst = catalyst
        # Masa total del sistema
        self.total_mass = alcohol.mass + acid.mass + catalyst.mass
        # Masa reactiva del sistema (sin catalizador)
        self.reaction_mass = alcohol.mass + acid.mass  # Masa de los reactivos sin catalizador
        # Moles totales del sistema
        self.total_moles = alcohol.moles + acid.moles + catalyst.moles
        # Moles de acidos
        self.total_acid_moles = acid.moles + catalyst.moles  # Moles de ácido y catalizador
        # Volumen del alcohol a la temperatura dada
        self.volume_alcohol = alcohol.mass_to_volume(temperature=temperature)
        # Volumen del ácido a la temperatura dada
        self.volume_acid = acid.mass_to_volume(temperature=temperature)
        # Volumen total del sistema a la temperatura dada
        self.ideal_volume = self.volume_alcohol + self.volume_acid
        if volume is not None:
            self.total_volume = volume
        else:
            self.total_volume = self.ideal_volume  # Volumen total del sistema (ideal)
        # Densidad del sistema a la temperatura dada
        self.density = self.total_mass / self.total_volume if self.total_volume > 0 else 0

        #Relaciones molares y fracciones molares

        # Fracción molar del alcohol
        self.x_alcohol = alcohol.moles / self.total_moles if self.total_moles > 0 else 0
        # Fracción molar del ácido
        self.x_acid = acid.moles / self.total_moles if self.total_moles > 0 else 0
        # Fracción molar del catalizador
        self.x_catalyst = catalyst.moles / self.total_moles if self.total_moles > 0 else 0

        # Fracción acida del acido:
        self.xacid_acid = acid.moles / self.total_acid_moles if self.total_acid_moles > 0 else 0
        # Fracción acida del catalizador:
        self.xacid_catalyst = catalyst.moles / self.total_acid_moles if self.total_acid_moles > 0 else 0



        # Relación molar entre el alcohol y el ácido
        self.rmol_alcohol_acid = alcohol.moles / acid.moles if acid.moles > 0 else 0
        # Relación molar entre el alcohol y el catalizador
        self.rmol_alcohol_catalyst = alcohol.moles / catalyst.moles if catalyst.moles > 0 else 0
        # Relación molar entre el ácido y el catalizador
        self.rmol_acid_catalyst = acid.moles / catalyst.moles if catalyst.moles > 0 else 0

        # Relaciones de masa
        # Fracción másica del alcohol
        self.w_alcohol = alcohol.mass / self.total_mass if self.total_mass > 0 else 0
        # Fracción másica del ácido
        self.w_acid = acid.mass / self.total_mass if self.total_mass > 0 else 0
        # Fracción másica del catalizador
        self.w_catalyst = catalyst.mass / self.total_mass if self.total_mass > 0 else 0

        # Relaciones de volumen
        # Fracción volumétrica del alcohol
        self.v_alcohol = self.volume_alcohol / self.total_volume if self.total_volume > 0 else 0
        # Fracción volumétrica del ácido
        self.v_acid = self.volume_acid / self.total_volume if self.total_volume > 0 else 0








    def __repr__(self):
        return f"Sistema({self.alcohol}, {self.acid}, {self.catalyst})"
    


#------------------------------------------------------------------------------

mixture_density = np.array([0.78,0.80])

alcohol= Butanol(mass=40.27*0.994)  # Masa de Butanol en gramos
acid = OctanoicAcid(mass=79.46*0.98)  # Masa de Ácido octanoico en gramos
cat = PTSA·H2O(mass=6.51)  # Masa de PTSA·H2O en gramos (no se usa en este cálculo)

temperatures = np.array([25,60,70,80])  # Temperaturas en ºC

system = System(alcohol, acid, cat, temperature=60, volume=None)  # Crear el sistema de reacción a 60ºC

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
    print(f"Volumen máximo de la mezcla a 60ºC: {volume_max:.2f} ml")
    print(f"Volumen mínimo de la mezcla a 60ºC: {volume_min:.2f} ml")
    print("-" * 40)





labels = ['80ºC', '70ºC', '60ºC','60ºC']

colors = ['blue', 'green', 'red', 'red']
# Crear la figura
plt.figure(figsize=(12, 6))

for index,values in enumerate(tiritation):
    if index in [0,1,3]:
        # Expand each value by adding one before (value - 0.03) and one after (value + 0.03)
        expanded_values = []
        NaOH = 0.1
        alicuota=0.1
        for v in values:
            expanded_values.extend([v - 0.03, v, v + 0.03])
        values = np.array(expanded_values)
        # Ajusto los valores de titulación a la concentración del NaOH como si fuera 0.1M
        #values = values / (0.089/0.1)
        
        # Multiplico el volumen de titulación por la concentración del NaOH para obtener los equivalentes cada 100 microlitros.
        #values = values * 0.1  # Ajustar a la concentración del NaOH (0.1M)
        # Multiplico los equivalentes por 10 para obtener los equivalentes por ml
        #values = values * 10  # Convertir a equivalentes por ml
        # Multiplico por el volumen total

        #values = values * total_volume  # Ajustar al volumen total de la reacción para obtener los equivalentes totales del sistema

        zero_value = values[0] / (system.xacid_acid)

        values = (
            zero_value - (values)) *100 / (zero_value * system.xacid_acid)



        
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


plt.ylabel('Conversión (%)')
plt.ylim(0, 105)  # Set y-axis limits
#plt.yticks(np.linspace(0.80, 4.00, 17))
plt.yticks(np.linspace(0, 100, 21))

plt.title('Conversión función del tiempo de reacción \n para alicuotas del sistema Butanol, Ácido octanoico y PTSA·H2O')
plt.legend()

plt.grid(True)
# Gráfico de cajas con posiciones correctas en eje X

plt.show()

