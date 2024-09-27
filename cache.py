# Cache handles turn off, turn on, flush, read and write to cache

from memory_bus import MemoryBus

class Cache:
    def __init__(self, memory_bus):
        self.enabled = True             # cache is enabled by default
        self.data = {}                  # dictionary to simulate cache storage
        self.memory_bus = memory_bus    # connect to memory bus

    def turn_off(self):
        self.enabled = False

    def turn_on(self):
        self.enabled = True

    def flush(self):
        self.data.clear()

    def read(self, memory_address):
        # read data from cache at specific address if cache enabled
        if self.enabled:
            if memory_address in self.data:
                # cache hit
                return self.data.get[memory_address]
            else:
                # cache miss, read from memory and update cache
                value = self.memory_bus.read(memory_address)
                self.data[memory_address] = value
        else:
            # if cache is disable, read directly from memroy
            return self.memory_bus.read(memory_address)

    def write(self, memory_address, value):
        # write data to cache at specific address if cache enabled
        if self.enabled:
            self.data[memory_address] = value
        # always write to memory
        self.memory_bus.write(memory_address, value)
    
    def print_cache(self):
        if not self.data:
            print("Cache is empty.")
        else:
            print("Cache contents:")
            for address, value in self.data.items():
                print(f"Address: {address}, Value: {value}")