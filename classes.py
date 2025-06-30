import numpy as np
import matplotlib.pyplot as plt
from unit_handler import temperature_conversion
from data import time, time_error
class Compound:
    def __init__(self, name, molar_mass, mass=0., moles=0.):
        """
        Inicializa un compuesto químico.
        :param name: Nombre del compuesto.
        :param molar_mass: Masa molar del compuesto en g/mol.
        :param mass: Masa del compuesto en gramos (opcional, p+6or defecto 0).
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
        
        temperature = temperature_conversion(
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
            temp = temperature_conversion(temp, 
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
        
        volume_calculation = True
        try:
            alcohol.density(temperature, unit="celsius")
            acid.density(temperature, unit="celsius")
        except NotImplementedError:
            volume_calculation = False
        
        if volume_calculation:
            if alcohol.mass > 0:
                # Volumen del alcohol a la temperatura dada
                self.volume_alcohol = alcohol.mass_to_volume(temperature=temperature)
            elif alcohol.moles > 0:
                # Volumen del alcohol a la temperatura dada
                self.volume_alcohol = alcohol.moles_to_volume(temperature=temperature)
            else:
                self.volume_alcohol = 0
            if acid.mass > 0:
                # Volumen del ácido a la temperatura dada
                self.volume_acid = acid.mass_to_volume(temperature=temperature)
            elif acid.moles > 0:
                # Volumen del ácido a la temperatura dada
                self.volume_acid = acid.moles_to_volume(temperature=temperature)
            else:
                self.volume_acid = 0
            
            # Volumen total del sistema a la temperatura dada
            self.ideal_volume = self.volume_alcohol + self.volume_acid
            if volume is not None:
                self.total_volume = volume
            else:
                self.total_volume = self.ideal_volume  # Volumen total del sistema (ideal)
            # Densidad del sistema a la temperatura dada
            self.density = self.total_mass / self.total_volume if self.total_volume > 0 else 0
        else:
            self.volume_alcohol = 0
            self.volume_acid = 0
            self.total_volume = 0
            self.ideal_volume = 0
            self.density = 0

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
    
