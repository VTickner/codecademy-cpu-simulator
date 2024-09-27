# MemoryBus handles reading and writing to memory

class MemoryBus:
    def __init__(self):
        self.memory = {}        # dictionary to simulate memory storage

    def read(self, memory_address):
        # read data from memory at specific address
        return self.memory[memory_address]

    def write(self, memory_address, value):
        # write data to memory at specific address
        self.memory[memory_address] = value
    
    def print_memory_bus(self):
        print("Memory contents:")
        for address, value in self.memory.items():
            print(f"Address: {address}, Value: {value}")
    
    def initialize_memory(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    address, value = map(int, line.strip().split(','))
                    self.memory[address] = value
        except FileNotFoundError:
            print(f"ERROR: The file '{filename}' was not found.")
        except ValueError as e:
            print(f"ERROR: Could not convert data from file. {e}")