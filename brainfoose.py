#!/usr/bin/env python3

BOLD = '\033[1m'
END_BOLD = '\033[0m'

def main():
    def new_tape():
        return [0] * 30000
    print(BOLD + "\nBrainfoose REPL" + END_BOLD)
    tape = new_tape()
    while True:
        program = input(BOLD + "\nbg > " + END_BOLD)
        end_index = len(program) - 1
        pointer = 0
        program_location = 0
        while program_location <= end_index:
            token = program[program_location]
            if token == ">":
                pointer += 1
            elif token == "<":
                pointer -= 1
            elif token == "+":
                tape[pointer] += 1
            elif token == "-":
                tape[pointer] -= 1
            elif token == ".":
                print(chr(tape[pointer]), end="")
            elif token == ",":
                tape[pointer] = ord(input("input > ")[0])
            elif token == "[":
                if tape[pointer] == 0:
                    loop_level = 1
                    while loop_level > 0:
                        program_location += 1
                        character = program[program_location]
                        if character == "[":
                            loop_level += 1
                        elif character == "]":
                            loop_level -= 1
            elif token == "]":
                loop_level = 1
                while loop_level > 0:
                    program_location -= 1
                    character = program[program_location]
                    if character == "[":
                        loop_level -= 1
                    elif character == "]":
                        loop_level += 1
                program_location -= 1
            elif token == "&":
                tape = new_tape()
            program_location += 1
    print("\n")


if __name__ == '__main__':
    main()
