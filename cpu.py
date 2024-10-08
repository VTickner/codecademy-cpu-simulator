# CPU handles fetching, decoding and executing instructions. It also interacts with memory and cache.

from memory_bus import MemoryBus

class CPU:
    def __init__(self, memory_bus, cache):
        self.memory_bus = memory_bus    # connect to memory bus
        self.cache = cache              # connect to cache
        self.registers = [0] * 32       # 32 registers (like MIPS)
        self.pc = 0                     # program counter (PC) for instruction that is to be processed next

    def fetch(self, filename):
        # fetch the instructions from a file and return them as a list
        try:
            with open(filename, "r") as file:
                instructions = file.readlines()
            # remove any newline characters
            return [instruction.strip() for instruction in instructions]
        except FileNotFoundError:
            raise FileNotFoundError(f"ERROR: The instruction file '{filename}' was not found.")
    
    def decode(self, instruction):
        # decode the instruction into its components (opcode, operands)
        return instruction.split(",")

    def parse_register(self, register_str):
        return int(register_str[1:])

    def execute(self, instruction):
        # executes the provided instruction, *operands captures remaining elements after opcode in a list
        opcode, *operands = instruction
        
        if opcode == "ADD":
            # get register numbers from string representation e.g. R2 -> 2
            Rd, Rs, Rt = map(self.parse_register, operands)
            # obtain data from register locations
            self.registers[Rd] = self.registers[Rs] + self.registers[Rt]
        elif opcode == "ADDI":
            Rt = self.parse_register(operands[0])
            Rs = self.parse_register(operands[1])
            immd = int(operands[2])
            self.registers[Rt] = self.registers[Rs] + immd
        elif opcode == "SUB":
            Rd, Rs, Rt = map(self.parse_register, operands)            
            self.registers[Rd] = self.registers[Rs] - self.registers[Rt]
        elif opcode == "SLT":
            Rd, Rs, Rt = map(self.parse_register, operands)
            if (self.registers[Rs] < self.registers[Rt]):
                self.registers[Rd] = 1
            else:
                self.registers[Rd] = 0
        elif opcode == "BNE":
            Rs = self.parse_register(operands[0])
            Rt = self.parse_register(operands[1])
            offset = int(operands[2])
            if (self.registers[Rs] != self.registers[Rt]):
                self.pc = (self.pc + 4) + offset * 4
        elif opcode == "J":
            target = int(operands[0])
            self.pc = target * 4
        elif opcode == "JAL":
            target = int(operands[0])
            self.registers[7] = self.pc + 4
            self.pc = target * 4
        elif opcode == "LW":
            Rt = self.parse_register(operands[0])
            offset = int(operands[1])
            Rs = self.parse_register(operands[2])
            memory_address = self.registers[Rs] + offset
            self.registers[Rt] = self.memory_bus.read(memory_address)
        elif opcode == "SW":
            Rt = self.parse_register(operands[0])
            offset = int(operands[1])
            Rs = self.parse_register(operands[2])
            memory_address = self.registers[Rs] + offset
            self.memory_bus.write(memory_address, self.registers[Rt])
        elif opcode == "CACHE":
            code = int(operands[0])
            if (code == 0):
                self.cache.turn_off()
            elif (code == 1):
                self.cache.turn_on()
            elif (code == 2):
                self.cache.flush()
            else:
                raise Exception("INVALID CACHE CODE")
        elif opcode == "HALT":
            print("Execution halted.")
            return True     # terminate execution (used in main.py)
        else:
            raise Exception("INVALID OPCODE")
        
        return False        # execution should continue (used in main.oy)
    
    def print_status(self):
        self.cache.print_cache()
        self.memory_bus.print_memory_bus()
        print("Registers:")
        for i, value in enumerate(self.registers):
            print(f"R{i}: {value}")
        print(f"PC: {self.pc}")