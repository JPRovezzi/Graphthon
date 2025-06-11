import pandas as pd
from abc import ABC, abstractmethod

class Result(ABC):
    def __init__(self, name: str, description: str, data: pd.DataFrame):
        self._name = name
        self._description = description
        self._data = data
    @property
    def name(self):
        return self._name
    @property
    def description(self):
        return self._description
    @property
    def data(self):
        return self._data

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_data(self):
        return self.data
    
    def set_name(self, name: str):
        self._name = name
    def set_description(self, description: str):
        self._description = description
    def set_data(self, data: pd.DataFrame):
        self._data = data
 

class Result_Titration(Result):
    def __init__(self, name: str, description: str, data: pd.DataFrame):
        super().__init__(name, description, data)
