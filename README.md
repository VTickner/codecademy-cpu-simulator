# Computer Science Projects - Portfolio Project: CPU Simulator

This portfolio project was created as part of [Codecademy's](https://www.codecademy.com) Computer Science Career Path course.

## Table of contents

- [Project Overview](#project-overview)
  - [Project objectives](#project-objectives)
- [Python CPU Simulator](#python-cpu-simulator)
- [Process](#process)
  - [Coding decisions](#coding-decisions)
  - [What I learned](#what-i-learned)
  - [Results of cpu.print_status()](#results-of-cpuprint_status)
- [Author](#author)

## Project Overview

"Welcome to the portfolio project for CS104: Computer Architecture! In this portfolio project, you will research, design, and build a Python program that simulates the functionalities of a CPU." - [Codecademy](https://www.codecademy.com)

### Project objectives

- Design and implement a working Python program that simulates the inner workings of a CPU.
- Use Git version control.
- Use the command line and file navigation.
- Develop locally on your computer.
- Write a technical blog post on the project.

## Python CPU Simulator

"While it is completely up to you to decide what to implement for your CPU simulator, here are some ideas for what your program could accomplish:

- Create classes that mimic the functionalities of a CPU, cache, and memory bus.
- Fetch and parse instructions from an input file.
- Fetch and parse initialization values for the Memory Bus from a separate input file.
- Send CPU instructions and initial Memory Bus values to the CPU and Memory Bus, respectively.
- Provide console output to the user documenting the stages of input processing.
- Implement an ISA that can handle MIPS Instructions such as the following:"

  | Instruction | Operand        | Meaning                                                        |
  | ----------- | -------------- | -------------------------------------------------------------- |
  | ADD         | Rd, Rs, Rt     | Rd <- Rs + Rt                                                  |
  | ADDI        | Rt, Rs, immd   | Rt <- Rs + immd                                                |
  | SUB         | Rd, Rs, Rt     | Rd <- Rs - Rt                                                  |
  | SLT         | Rd, Rs, Rt     | If (Rs < Rt) then Rd <- 1 else Rd <- 0                         |
  | BNE         | Rs, Rt, offset | If (Rs not equal Rt) then PC <- (PC + 4) + offset \* 4         |
  | J           | target         | PC <- target \* 4                                              |
  | JAL         | target         | R7 <- PC + 4; PC <- target \* 4                                |
  | LW          | Rt, offset(Rs) | Rt <- MEM[Rs + offset]                                         |
  | SW          | Rt, offset(Rs) | MEM[Rs + offset] <- Rt                                         |
  | CACHE       | Code           | Code = 0(Cache off), Code = 1(Cache on), Code = 2(Flush cache) |
  | HALT        | ;              | Terminate Execution                                            |

  \- [Codecademy](https://www.codecademy.com)

For this particular project I decided to simulate working with the cache, the memory bus along with the CPU. Using the data and instruction input files provided by Codecademy which utilised the MIPS instructions above.

- Solution URL: [CPU Simulator](./main.py)
- Classes:
  - [CPU](./cpu.py)
  - [Cache](./cache.py)
  - [Memory Bus](./memory_bus.py)
- Input files provided by Codecademy:
  - [data_input.txt](./data_input.txt) contains an initial set of data values to populate a simulated MemoryBus for your project. Each line contains a memory address within the Memory Bus, followed by its initial integer value: `<ADDRESS>,<VALUE>`.
  - [instruction_input.txt](./instruction_input.txt) contains a list of instructions to be loaded by your CPU. Instructions are of the format `<INSTRUCTION>,<ARG_1>,...,<ARG_n>`.

## Process

- Think of what parts want to simulate as part of the CPU.
- Project brainstorming on how the CPU simulation will work:
  - Separate different parts of the CPU into different classes.
  - CPU class will need:
    - `\_\_init\_\_()`
    - `fetch()`
    - `decode()`
    - `execute()`.
  - Cache class will need:
    - `\_\_init\_\_()`
    - `turn_off()`
    - `turn_on()`
    - `flush()`
    - `read()`
    - `write()`.
  - MemoryBus class will need:
    - `\_\_init\_\_()`
    - `read()`
    - `write()`
    - `initialise_memory()`.
  - `main()` to:
    - Initialise CPU
    - Initialise cache
    - Initialise memory bus.
    - Read in `data_input.txt`
    - Read in `instruction_input.txt`
- Set up a GitHub repository.
- Set up Git version control.
- Write CPU simulation program.
  - Realised when testing that I needed to be able to print out the status of the CPU, memory bus and cache so added:
    - `print_status()` to CPU class
    - `print_cache()` to Cache class
    - `print_memory_bus()` to MemoryBus class
    - call `cpu.print_status()` in `main()`
- Refactor program.
- Create blog post about project. (This README file is my post about the project I have created.)

### Coding decisions

There are a number of decisions I made as to how to approach and code this game. So below is an explanation as to the what and why I wrote the code in the way that I did.

- Refactor code:

  - So could handle error messaging in a more suitable way.
  - Improving flexibility of input files by removing hardcoded filenames and passing them as arguments instead.
  - Added extra function `cpu.parse_register()` as using the same functionality multiple times in `cpu.execute()`

    ```python
    def parse_register(self, register_str):
        return int(register_str[1:])

    def execute(self, instruction):
        # executes the provided instruction, *operands captures remaining elements after opcode in a list
        opcode, *operands = instruction

        if opcode == "ADD":
            # get register numbers from string representation e.g. R2 -> 2
            Rd, Rs, Rt = map(self.parse_register, operands)
    ```

- Error checking:
  - Refactored error checking in all classes to use `raise Exception("error message")` style error messages.
  - Added checks for data and instruction files being properly loaded.

### What I learned

- If script is run directly, then python sets `__name__ = "__main__"`. If the same script is imported into another module, then python sets `__name__ = "main"`:

  ```python
  # checks whether current script is being executed as main program, if so will execute
  if __name__ == "__main__":
      main()
  ```

- `enumerate()` to create a list of registers so can enable printing out status of each register.

### Results of cpu.print_status()

- Memory contents matches up with `data_input.txt`
- Registers and PC match up with expected outcomes of `instruction_input.txt`:

  - Cache enabled
  - R2 = R2 + 2 -> R2 = 0 + 2 -> R2 = 2
  - R3 = R2 + R1 -> R3 = 2 + 0 -> R3 = 2
  - J8 -> PC = 8 \* 4 -> PC = 32

  ```
  Execution halted.
  Cache is enabled? True
  Cache is empty.
  Memory contents:
  Address: 1, Value: 4
  Address: 10, Value: 5
  Address: 11, Value: 6
  Address: 100, Value: 7
  Address: 101, Value: 2
  Address: 110, Value: 3
  Address: 111, Value: 9
  Registers:
  R0: 0
  R1: 0
  R2: 2
  R3: 2
  R4: 0
  R5: 0
  R6: 0
  R7: 0
  R8: 0
  R9: 0
  R10: 0
  R11: 0
  R12: 0
  R13: 0
  R14: 0
  R15: 0
  R16: 0
  R17: 0
  R18: 0
  R19: 0
  R20: 0
  R21: 0
  R22: 0
  R23: 0
  R24: 0
  R25: 0
  R26: 0
  R27: 0
  R28: 0
  R29: 0
  R30: 0
  R31: 0
  PC: 32
  ```

## Author

- V. Tickner
