import pandas as pd
class experiment:
    def __init__(self):
        pass


class Titration(experiment):
    """Titration experiment class."""
    def __init__(
            self,
            titration_data = pd.DataFrame()
            ):
        
        super().__init__()
        self.name = None
        self.type = "Titration"
        self.description = None
        self.titration_data = titration_data
        self.temperature = None
        