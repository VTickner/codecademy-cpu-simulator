from memory_bus import MemoryBus
from cache import Cache
from cpu import CPU

def main():
    memory_bus = MemoryBus()
    cache = Cache(memory_bus)
    cpu = CPU(memory_bus, cache)

    memory_bus.initialise_memory("data_input.txt")

    instructions = cpu.fetch("instruction_input.txt")
    for instruction in instructions:
        operands = cpu.decode(instruction)
        try:
            # execute the instruction, but terminate execution if HALT encountered
            if cpu.execute(operands):
                break
        except Exception as e:
            print(f"ERROR: {e}")
    
    cpu.print_status()

# checks whether current script is being executed as main program, if so will execute
if __name__ == "__main__":
    main()