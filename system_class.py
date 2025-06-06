import numpy as np

messages = {
    "total_mass": "No se pudo calcular la masa total del sistema. Proporcione componentes o masa total.",
}


class System:
    def __init__(self,
                temperature: float = 25., # ºC
                pressure: float = 1.0, # atm
                volume: float = None, # ml
                components: list = None,
                phases: list = None,
                total_mass: float = None,
                total_moles: float = None,
                m: np.ndarray = None,
                n: np.ndarray = None,
                x: np.ndarray = None,
                w: np.ndarray = None,
                 ):
        """
        Inicializa un sistema.
        """
        # System components
        if components is None or len(components) == 0:
            self.total_mass = 0.0
            self.total_moles = 0.0
            self.volume = 0.0
            phases = []
            self.components = []
        else:
            self.components = components
        
        # Masa total del sistema
        if total_mass is not None:
            self.total_mass = total_mass  # Masa total del sistema
        elif m is not None:
            self.total_mass = m.sum()
        elif n is not None:
            self.total_mass = np.sum(n * np.array([comp.molar_weight for comp in components]))
        else:
            raise ValueError(messages["total_mass"])

        # Moles totales del sistema
        if total_moles is None:
        self.total_moles = total_moles


     