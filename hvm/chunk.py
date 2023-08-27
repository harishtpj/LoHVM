# 
from enum import Enum

from .values import Value

class OpCode(Enum):
    CONST = 0
    RET = 1

class Chunk:
    def __init__(self) -> None:
        self.code = []
        self.constants = Value()
        self.lines = []

    def write(self, byte: int, line: int) -> None:
        self.code.append(byte)
        self.lines.append(line)
    
    def add_constant(self, value: float, line: int) -> None:
        self.constants.write(value)
        self.write(OpCode.CONST, line)
        self.write(len(self.constants.values) - 1, line)

    def free(self) -> None:
        self.code.clear()
        self.constants.free()
        self.lines.clear()

    def disassemble(self, name: str) -> None:
        print(f"== {name} ==")

        offset = 0
        while offset < len(self.code):
            print(f"0x{offset:04x}", end=" ")

            if offset > 0 and (self.lines[offset] == self.lines[offset - 1]):
                print("   |", end=" ")
            else:
                print(f"{self.lines[offset]:4d}", end=" ")

            instruction = self.code[offset]
            if instruction == OpCode.CONST:
                const_index = self.code[offset + 1]
                const_value = self.constants.values[const_index]
                print(f"{instruction} \t[{const_index:04d}]: {const_value}")
                offset += 2
            else:
                print(instruction)
                offset += 1
