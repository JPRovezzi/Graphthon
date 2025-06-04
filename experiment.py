import pandas as pd
class experiment:
    def __init__(self):
        pass

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
        self.name = None
        self.type = "Titration"
        self.description = None
        self.titration_data = titration_data
        self.temperature = None
        self.titrant = None
        self
        