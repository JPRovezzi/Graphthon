from system_class import System
class Phase(System):
    """
    A class representing a phase in a system.
    Inherits from the System class.
    """
    
    def __init__(self, temperature=None, pressure=None, name=None,):
        """
        Initializes a Phase instance.

        :param name: The name of the phase.
        :param description: A brief description of the phase.
        """
        super().__init__()