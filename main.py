from memory_bus import MemoryBus
from cache import Cache
from cpu import CPU

def main():
    memory_bus = MemoryBus()
    cache = Cache(memory_bus)
    cpu = CPU(memory_bus, cache)

    memory_bus.initialize_memory("data_input.txt")

    instructions = cpu.fetch("instruction_input.txt")
    for instruction in instructions:
        operands = cpu.decode(instruction)
        # execute the instruction, but terminate execution if HALT encountered
        if cpu.execute(operands):
            break
    
    cpu.print_status()

# if script run directly, python sets __name__ = "__main__"
# if same script is imported into another module, python sets __name__ = "main"

# checks whether current script is being executed as main program, if so will execute
if __name__ == "__main__":
    main()