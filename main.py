from memory_bus import MemoryBus
from cache import Cache
from cpu import CPU

def main(data_input_file="data_input.txt", instruction_input_file="instruction_input.txt"):
    memory_bus = MemoryBus()
    cache = Cache(memory_bus)
    cpu = CPU(memory_bus, cache)

    memory_bus.initialise_memory(data_input_file)
    if not memory_bus.memory:
        raise Exception("ERROR: Memory not initialised properly.")

    instructions = cpu.fetch(instruction_input_file)
    if not instructions:
        raise Exception("ERROR: No instructions loaded from file.")

    for instruction in instructions:
        operands = cpu.decode(instruction)
        try:
            # execute the instruction, but terminate execution if HALT encountered
            if cpu.execute(operands):
                break
        except Exception as e:
            print(f"ERROR: Problem executing instruction '{instruction}': {e}")
    
    cpu.print_status()

# checks whether current script is being executed as main program, if so will execute
if __name__ == "__main__":
    main()