class Device():
    def __init__(self, name: str, connected_by: str):
        self.name = name
        self.connected_by = connected_by
        self.is_connected = True

    def __str__(self):
        return f"Device {self.name} is connected by {self.connected_by},\
        \nconnection status: {self.is_connected}"

    def disconnect(self):
        self.is_connected = False
        print(F"Device {self.connected_by} disconnected successfully 😒")


class Printer(Device):
    def __init__(self, name: str, connected_by: str, capacity: int):
        super().__init__(name=name, connected_by=connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} \n{self.remaining_pages} pages remaining"
    
    def print_pages(self, page: int, data: list[str]):
        if self.is_connected:
            self.remaining_pages -= page
            print(data)
        else:
            print("Printer is not connected 😡")
