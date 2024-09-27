# Computer Science Projects - Portfolio Project: CPU Simulator

This portfolio project was created as part of [Codecademy's](https://www.codecademy.com) Computer Science Career Path course.

## Table of contents

- [Project Overview](#project-overview)
  - [Project objectives](#project-objectives)
- [Python CPU Simulator](#python-cpu-simulator)
- [Process](#process)
  - [Coding decisions](#coding-decisions)
  - [What I learned](#what-i-learned)
  - [Potential improvements to program](#potential-improvements-to-program)
  - [Useful resources](#useful-resources)
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
    - `is_enable()`
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

- Refactor code so could handle error messaging in a more suitable way.
- Error checking:
  - Refactored error checking in CPU class to use `raise Exception("error message")` with try/except block used to display error message.
  - Added raise/exception in MemoryBus class to better handle errors.

### What I learned

- If script is run directly, then python sets `__name__ = "__main__"`. If the same script is imported into another module, then python sets `__name__ = "main"`:

  ```python
  # checks whether current script is being executed as main program, if so will execute
  if __name__ == "__main__":
      main()
  ```

- `enumerate()` to create a list of registers so can enable printing out status of each register.

### Potential improvements to program

- TODO ...

### Useful resources

- TODO ...

## Author

- V. Tickner
