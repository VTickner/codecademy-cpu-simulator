# MemoryBus handles reading and writing to memory along with initialising memory with data from file

class MemoryBus:
    def __init__(self):
        self.memory = {}        # dictionary to simulate memory storage

    def read(self, memory_address):
        # read data from memory at specific address
        if memory_address in self.memory:
            return self.memory[memory_address]
        else:
            raise KeyError(f"Memory address {memory_address} not found.")

    def write(self, memory_address, value):
        # write data to memory at specific address
        self.memory[memory_address] = value
    
    def initialise_memory(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    address, value = map(int, line.strip().split(','))
                    self.memory[address] = value
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filename}' was not found.")
        except ValueError as e:
            raise ValueError(f"Could not convert data from file. {e}")
    
    def print_memory_bus(self):
        if not self.memory:
            print("Memory is empty.")
        else:
            print("Memory contents:")
            for address, value in self.memory.items():
                print(f"Address: {address}, Value: {value}")