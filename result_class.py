import pandas as pd
from abc import ABC, abstractmethod

class Result(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_data(self):
        pass
    

    


class Result_Titrarion(Result):
    def __init__(self, name: str, description: str, data: pd.DataFrame):
        self._name = name
        self._description = description
        self._data = data

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_data(self):
        return self._data