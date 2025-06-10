import pandas as pd
class experiment:
    def __init__(self, name=None,type= None,description=None, data: pd.DataFrame = None):
        self.name = name
        self.type = type
        self.description = description
        self.data = data if data is not None else pd.DataFrame()


class Solution():
    """Solution class."""
    def __init__(self):
        self.name = None
        self.mass = None
        self.volume_ref = None
        self.density_ref = None
        self.temperature_ref = (298.15,"K")
        self.pressure_ref = (1,"atm")

class Titrant(Solution):
    """Titrant class."""
    def __init__(self):
        super().__init__()

class Titration(experiment):
    """Titration experiment class."""
    def __init__(
            self,
            titration_data: pd.DataFrame = None,
            ):
        super().__init__()
        self.name = name
        self.type = "Titration"
        self.description = description
        self.titration_data = titration_data
        self.temperature = None
        self.titrant = None
        self.repetitions = None
    def __repr__(self):
        return f"Titration(name={self.name}, type={self.type}, description={self.description}, temperature={self.temperature}, titrant={self.titrant}, repetitions={self.repetitions})"
    def __str__(self):
        return f"Titration: {self.name}, Type: {self.type}, Description: {self.description}, Temperature: {self.temperature}, Titrant: {self.titrant}, Repetitions: {self.repetitions}"
    def __len__(self):
        return len(self.titration_data) if self.titration_data is not None else 0
    def __getitem__(self, key):
        if self.titration_data is not None:
            return self.titration_data[key]
        else:
            raise IndexError("Titration data is not available.")
    def __setitem__(self, key, value):
        if self.titration_data is not None:
            self.titration_data[key] = value
        else:
            raise IndexError("Titration data is not available.")
    def __delitem__(self, key):
        if self.titration_data is not None:
            del self.titration_data[key]
        else:
            raise IndexError("Titration data is not available.")
    def to_dict(self):
        """Convert the Titration object to a dictionary."""
        return {
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "temperature": self.temperature,
            "titrant": self.titrant,
            "repetitions": self.repetitions,
            "titration_data": self.titration_data.to_dict() if self.titration_data is not None else None
        }
    @classmethod
    def from_dict(cls, data):
        """Create a Titration object from a dictionary."""
        instance = cls()
        instance.name = data.get("name")
        instance.type = data.get("type", "Titration")
        instance.description = data.get("description")
        instance.temperature = data.get("temperature")
        instance.titrant = data.get("titrant")
        instance.repetitions = data.get("repetitions")
        if "titration_data" in data and data["titration_data"] is not None:
            instance.titration_data = pd.DataFrame(data["titration_data"])
        return instance
    def to_dataframe(self):
        """Convert the Titration object to a pandas DataFrame."""
        if self.titration_data is not None:
            return self.titration_data
        else:
            raise ValueError("Titration data is not available.")
    @classmethod
    def from_dataframe(cls, df):
        """Create a Titration object from a pandas DataFrame."""
        instance = cls()
        instance.titration_data = df
        return instance
    def add_titration_data(self, data):
        """Add titration data to the Titration object."""
        if self.titration_data is None:
            self.titration_data = pd.DataFrame(data)
        else:
            new_data = pd.DataFrame(data)
            self.titration_data = pd.concat([self.titration_data, new_data], ignore_index=True)
    def clear_titration_data(self):
        """Clear the titration data."""
        self.titration_data = None
    def get_titration_data(self):
        """Get the titration data."""
        if self.titration_data is not None:
            return self.titration_data
        else:
            raise ValueError("Titration data is not available.")
    def set_titration_data(self, data):
        """Set the titration data."""
        if isinstance(data, pd.DataFrame):
            self.titration_data = data
        else:
            raise ValueError("Data must be a pandas DataFrame.")
    def get_titrant(self):
        """Get the titrant."""
        return self.titrant
    def set_titrant(self, titrant):
        """Set the titrant."""
        if isinstance(titrant, Titrant):
            self.titrant = titrant
        else:
            raise ValueError("Titrant must be an instance of the Titrant class.")
    def get_temperature(self):
        """Get the temperature."""
        return self.temperature
    def set_temperature(self, temperature):
        """Set the temperature."""
        if isinstance(temperature, (int, float)):
            self.temperature = temperature
        else:
            raise ValueError("Temperature must be a numeric value.")
    def get_repetitions(self):
        """Get the number of repetitions."""
        return self.repetitions
    def set_repetitions(self, repetitions):
        """Set the number of repetitions."""
        if isinstance(repetitions, int) and repetitions > 0:
            self.repetitions = repetitions
        else:
            raise ValueError("Repetitions must be a positive integer.")
    def add_repetition(self):
        """Add a repetition to the titration."""
        if self.repetitions is None:
            self.repetitions = 1
        else:
            self.repetitions += 1
    def remove_repetition(self):
        """Remove a repetition from the titration."""
        if self.repetitions is not None and self.repetitions > 0:
            self.repetitions -= 1
        else:
            raise ValueError("Repetitions cannot be less than zero.")
    def clear_repetitions(self):
        """Clear the number of repetitions."""
        self.repetitions = None
    def get_description(self):
        """Get the description of the titration."""
        return self.description
    def set_description(self, description):
        """Set the description of the titration."""
        if isinstance(description, str):
            self.description = description
        else:
            raise ValueError("Description must be a string.")
    def get_name(self):
        """Get the name of the titration."""
        return self.name
    def set_name(self, name):
        """Set the name of the titration."""
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be a string.")
    def get_type(self):
        """Get the type of the titration."""
        return self.type
    def set_type(self, type_):
        """Set the type of the titration."""
        if isinstance(type_, str):
            self.type = type_
        else:
            raise ValueError("Type must be a string.")
    def get_titration_summary(self):
        """Get a summary of the titration experiment."""
        summary = {
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "temperature": self.temperature,
            "titrant": self.titrant.name if self.titrant else None,
            "repetitions": self.repetitions,
            "titration_data": self.titration_data.describe() if self.titration_data is not None else None
        }
        return summary
    def save_to_csv(self, filename):
        """Save the titration data to a CSV file."""
        if self.titration_data is not None:
            self.titration_data.to_csv(filename, index=False)
        else:
            raise ValueError("Titration data is not available to save.")
    def load_from_csv(self, filename):
        """Load titration data from a CSV file."""
        try:
            self.titration_data = pd.read_csv(filename)
        except FileNotFoundError:
            raise ValueError(f"File {filename} not found.")
        except Exception as e:
            raise ValueError(f"An error occurred while loading the file: {e}")
    def plot_titration_curve(self):
        """Plot the titration curve."""
        pass
    def calculate_average_volume(self):
        """Calculate the average volume of titrant used in the titration."""
        pass
    def calculate_equivalence_point(self):
        """Calculate the equivalence point of the titration."""
        pass
    def calculate_end_point(self):
        """Calculate the end point of the titration."""
        pass
    def calculate_concentration(self):
        """Calculate the concentration of the analyte in the titration."""
        pass
    def calculate_molarity(self):
        """Calculate the molarity of the titrant."""
        pass
    def calculate_normality(self):
        """Calculate the normality of the titrant."""
        pass


        