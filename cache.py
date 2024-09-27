# Cache handles turn off, turn on, flush, read and write to cache

from memory_bus import MemoryBus

class Cache:
    def __init__(self, memory_bus):
        self.enabled = True             # cache is enabled by default
        self.data = {}                  # dictionary to simulate cache storage
        self.memory_bus = memory_bus    # connect to memory bus

    def turn_off(self):
        self.enabled = False
        print("Cache is now turned off.")

    def turn_on(self):
        self.enabled = True
        print("Cache is now turned on.")

    def flush(self):
        self.data.clear()
        print("Cache has now been flushed.")
    
    # check if cache is enabled
    def is_enabled(self):
        return self.enabled

    def read(self, memory_address):
        # read data from cache at specific address if cache enabled
        if self.enabled:
            return self.data.get(memory_address, None)  # return None if memory_address not in cache
        else:
            print("Cache is disabled. Reading directly from memory.")
            return self.memory_bus.read(memory_address)

    def write(self, memory_address, value):
        # write data to cache at specific address if cache enabled
        if self.enabled:
            self.data[memory_address] = value
            print(f"Written to cache: address {memory_address}, value {value}.")
        else:
            print("Cache is disabled. Writing directly to memory.")
            return self.memory_bus.write(memory_address, value)
    
    def print_cache(self):
        print("Cache contents:")
        for address, value in self.data.items():
            print(f"Address: {address}, Value: {value}")