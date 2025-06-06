def temperature_conversion(temperature, from_unit, to_unit):
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