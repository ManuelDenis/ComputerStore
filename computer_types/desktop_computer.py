from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    processors = {'AMD Ryzen 7 5700G': 500, 'Intel Core i5-12600K': 600, 'Apple M1 Max': 1800}
    rams = {2: 100, 4: 200, 8: 300, 16: 400, 32: 500, 64: 600, 128: 700}

    def __init__(self, manufacturer: str, model: str, processor: str = None, ram: int = None):
        super().__init__(manufacturer, model)
        if processor in self.processors:
            self.processor = processor
        if ram in self.rams:
            self.ram = ram

    def configure_computer(self, processor: str, ram: int):
        if processor in self.processors:
            self.processor = processor
        else:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        if ram in self.rams:
            self.ram = ram
        else:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if self.processor and self.ram:
            self.price = self.rams[self.ram] + self.processors[self.processor]
            return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

