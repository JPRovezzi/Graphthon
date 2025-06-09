import numpy as np

messages = {
    "total_mass": "No se pudo calcular la masa total del sistema. Proporcione componentes o masa total.",
}


class System:
    '''Class representing a thermodynamic system.
    Attributes:
        temperature (float) [T]: Temperature in Kelvin.
        pressure (float) [P]: Pressure in atm.
        total_volume [V] (float): Total volume of the system in ml.
        components [C] (list): List of system components (e.g., substances).
        phases [F] (list): List of system phases (e.g., liquid, gas). Each phase is a system class instance. If len(phases) == 1, the system is considered a single phase and, therefore, the properties of the system are equal to the properties of the phase.
        total_mass [m] (float): Total mass of the system in grams.
        total_moles [n] (float): Total moles of the system.
        d (list): Density of the system.
    '''
    temperature: float # Temperature in Kelvin
    pressure: float # Pressure in atm
    total_volume: float # Volume in ml
    components: list # System components (e.g., substances)
    phases: list # System phases (e.g., liquid, gas)
    total_mass: float # Total mass of the system in grams
    total_moles: float # Total moles of the system
    m: list # Mass of each component in grams
    n: list # Moles of each component in moles
    d: list # Density of each component (g/ml)
    
    _valid_system_init_ = [
            #   [ T, P, V, C, F, m, n, d]
            # Empty systems
            [
            #   [ T, P, V, C, F, m, n, d]
                # Empty system with no parameters
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                # Empty T-P system
                [ 1, 1, 0, 0, 0, 0, 0, 0],
                # Empty T-V system
                [ 1, 0, 1, 0, 0, 0, 0, 0],
                # Empty P-V system
                [ 0, 1, 1, 0, 0, 0, 0, 0],
            ],
            # Defined systems
            # All the defined systems need to be monophasic, i.e., len(phases) == 1. If not the system is considered a multiphasic system and the properties of the system are derived from the properties of the phases, which are subsystems.
             # Defined T-P systems
            [
            #   [ T, P, V, C, F, m, n, d]
                # Defined empty T-P system
                [ 1, 1, 0, 1, 0, 0, 0, 0],
                # Defined T-P system with mass
                [ 1, 1, 0, 1, 1, 1, 0, 0],
                # Defined T-P system with moles
                [ 1, 1, 0, 1, 1, 0, 1, 0],
                # Defined T-P system with volume and mass
                [ 1, 1, 1, 1, 1, 1, 0, 0],
                # Defined T-P system with volume and moles
                [ 1, 1, 1, 1, 1, 0, 1, 0],
                # Defined T-P system with density and mass
                [ 1, 1, 0, 1, 1, 1, 0, 1],
                # Defined T-P system with density and moles
                [ 1, 1, 0, 1, 1, 0, 1, 1],
            ],
            # Defined T-V systems
            [
            #   [ T, P, V, C, F, m, n, d]
                # Defined empty T-V system
                [ 1, 0, 1, 1, 0, 0, 0, 0],
            ],
            # Defined P-V systems
            [
            #   [ T, P, V, C, F, m, n, d]
                # Defined empty P-V system
                [ 0, 1, 1, 1, 0, 0, 0, 0],
            ],
            # No PVT systems
            [
            #   [ T, P, V, C, F, m, n, d]
                # Defined system through phase properties
                [ 0, 0, 0, 0, 1, 0, 0, 0],
            ],
        ]

    def _get_init(self,*args):
            # Make a list of the *args
            parameters = list(args)
            print(f"Parameters received: {parameters}")
            # Check if the length of the list is 10
            param_length = len(self._valid_system_init_[0][0])
            if len(parameters) != param_length:
                raise ValueError(f"Invalid number of parameters. Expected {param_length} parameters.")

            system_init = [0] * param_length
            for i, param in enumerate(parameters):
                if param is not None:
                    system_init[i] = 1
            return system_init
    def __init__(self,
                temperature: float = 25., # ºC
                pressure: float = 1.0, # atm
                total_volume: float = None, # ml
                components: list = None,
                phases: list = None,
                total_mass: float = None,
                total_moles: float = None,
                m: list = None,
                n: list = None,
                w: list = None,
                z: list = None,
                d: list = None
                 ):
        """
        Inicializa un sistema.
        """
        _system_init = self._get_init(temperature, pressure, total_volume, components, phases, total_mass, total_moles, m, n, w, z, d)
        self._check_validity_(_system_init)

        # Empty systems
        if _system_init == self._valid_system_init_[0][0]:
            self.temperature = None
            self.pressure = None
            self.total_volume = None
            self.components = []
            self.phases = []
            self.total_mass = 0.0
            self.total_moles = 0.0
            self.m = []
            self.n = []
            self.d = []
        # Empty T-P system
        elif _system_init == self._valid_system_init_[0][1]:
            self.temperature = temperature
            self.pressure = pressure
            self.total_volume = None
            self.components = []
            self.phases = []
            self.total_mass = 0.0
            self.total_moles = 0.0
            self.m = []
            self.n = []
            self.d = []
        else:
            raise ValueError("Invalid system initialization parameters.")
        
  
        
        

    def _check_validity_(self, system_init):
        for valid_system_init in self._valid_system_init_:
            if system_init not in valid_system_init:
                return ValueError("Invalid system initialization parameters.")