import re
import math

def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = [line.split() for line in file.read().split("\n")]
        registers = {
            'A': 0,
            'B': 0,
            'C': 0
        }
        program = []
        passed_half = False
        for line in lines:
            if line == []:
                passed_half = True
            elif passed_half:
                program = re.findall(r'-?\d+', line[1])
            else:
                if 'A' in line[1]:
                    registers['A'] = int(line[2])
                if 'B' in line[1]:
                    registers['B'] = int(line[2])
                if 'C' in line[1]:
                    registers['C'] = int(line[2])
        return registers, program


def parse_program_input(registers, program, pointer):
    instruction = int(program[pointer])
    literal_operand = int(program[pointer + 1])
    combo_operand = literal_operand
    if literal_operand == 4:
        combo_operand = registers['A']
    elif literal_operand == 5:
        combo_operand = registers['B']
    elif literal_operand == 6:
        combo_operand = registers['C']
    return instruction, combo_operand, literal_operand


def run_program(registers, program, pointer):
    out_addition = None
    instruction, combo_operand, literal_operand = parse_program_input(registers, program, pointer)
    new_pointer = None
    if instruction == 0:
        registers['A'] = math.trunc(registers['A']/(2**combo_operand))
    elif instruction == 1:
        # Bitwise XOR of register B and instruction's literal operand
        registers['B'] = registers['B'] ^ literal_operand
    elif instruction == 2:
        registers['B'] = combo_operand % 8
    elif instruction == 3:
        if registers['A'] != 0:
            new_pointer = literal_operand
    elif instruction == 4:
        # Bitwise XOR of register B and register C
        registers['B'] = registers['B'] ^ registers['C']
    elif instruction == 5:
        out_addition = combo_operand % 8
    elif instruction == 6:
        registers['B'] = math.trunc(registers['A']/(2**combo_operand))
    elif instruction == 7:
        registers['C'] = math.trunc(registers['A']/(2**combo_operand))
    return registers, str(out_addition), new_pointer

def main():
    registers, program = read_file()
    pointer = 0
    out = []
    while pointer < len(program)-1:
        registers, out_addition, new_pointer = run_program(registers, program, pointer)
        if out_addition != 'None':
            out.append(out_addition)
        if new_pointer is None:
            pointer += 2
        else:
            pointer = new_pointer
    print(out)
    return ','.join(out)

answer = main()

print(answer)

