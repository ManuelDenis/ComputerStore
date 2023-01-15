from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    warehouse = []
    profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == 'Laptop':
            lap = Laptop(manufacturer, model, processor, ram)
            self.warehouse.append(lap)
            return lap.configure_computer(processor, ram)
        elif type_computer == 'Desktop Computer':
            desk = DesktopComputer(manufacturer, model, processor, ram)
            self.warehouse.append(desk)
            return desk.configure_computer(processor, ram)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for comp in self.warehouse:
            if comp.price <= client_budget and wanted_processor == comp.processor and comp.ram >= wanted_ram:
                self.profits = client_budget - comp.price
                return f"{comp} sold for {client_budget}$."
        return f"Sorry, we don't have a computer for you."
