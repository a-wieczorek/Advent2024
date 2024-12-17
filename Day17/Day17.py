with open('Input.txt', 'r') as f:
    regA, regB, regC, instructions = [row.split(' ')[-1] for row in f.read().split('\n') if row]

regA, regB, regC = int(regA), int(regB), int(regC)
instructions = [int(op) for op in instructions.split(',')]


class Computer:
    def __init__(self, regA: int, regB: int, regC: int):
        self.regA = regA
        self.regB = regB
        self.regC = regC
        self.output = []

    def process(self, pointer: int) -> int:
        def get_combo_operand(operand: int) -> int:
            if operand == 4:
                return self.regA
            elif operand == 5:
                return self.regB
            elif operand == 6:
                return self.regC
            return operand

        opcode = instructions[pointer]
        operand = instructions[pointer + 1]
        if opcode in [0, 6, 7]:
            val = self.regA // (2**get_combo_operand(operand))
            if opcode == 0:
                self.regA = val
            elif opcode == 6:
                self.regB = val
            elif opcode == 7:
                self.regC = val
        elif opcode == 1:
            self.regB = self.regB ^ operand
        elif opcode == 2:
            self.regB = get_combo_operand(operand) % 8
            pass
        elif opcode == 3:
            if self.regA != 0:
                return operand
        elif opcode == 4:
            self.regB = self.regB ^ self.regC
        elif opcode == 5:
            self.output.append(get_combo_operand(operand) % 8)
        return pointer + 2


computer = Computer(regA, regB, regC)
i = 0
while i + 1 in range(len(instructions)):
    print({'A': computer.regA, 'B': computer.regB, 'C': computer.regC})
    i = computer.process(i)

print(','.join([str(out) for out in computer.output]))


