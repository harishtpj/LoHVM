# The main Virtual Machine Class
from enum import Enum
from .chunk import OpCode, Chunk
from .stack import Stack

class InterpretResult(Enum):
    OK = 0
    COMPILE_ERROR = 1
    RUNTIME_ERROR = 2

class HVM:
    def __init__(self) -> None:
        self.chunk = None
        self.pc = -1
        self.stack = Stack()
    
    def interpret(self, chunk: Chunk) -> InterpretResult:
        self.chunk = chunk
        self.pc = 0
        return self.run()
    
    def run(self) -> InterpretResult:
        while True:
            if __debug__:
                print(self.stack)
                self.chunk.dis_inst(self.pc)
            instruction = self.read_byte()
            match instruction:
                case OpCode.CONST:
                    constant = self.read_const()
                    self.stack.push(constant)
                
                case OpCode.ADD: self.stack.add()
                case OpCode.SUB: self.stack.minus()
                case OpCode.MUL: self.stack.mul()
                case OpCode.DIV: self.stack.div()
                case OpCode.NEGATE: self.stack.negate()

                case OpCode.RET:
                    print(self.stack.pop())
                    return InterpretResult.OK
    
    def free(self):
        pass

    def read_byte(self) -> OpCode:
        byte = self.chunk.code[self.pc]
        self.pc += 1
        return byte
    
    def read_const(self) -> float:
        return self.chunk.constants.values[self.read_byte()]