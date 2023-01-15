from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str, processor: str = None, ram: int = None, price: int = 0):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = processor
        self.ram = ram
        self.price = price

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        if manufacturer.isspace():
            raise ValueError("Manufacturer name cannot be empty.")
        else:
            self._manufacturer = manufacturer

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if model.isspace():
            raise ValueError("Manufacturer name cannot be empty.")
        else:
            self._model = model

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        return Computer(self.manufacturer, self.model, processor, ram)

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"






