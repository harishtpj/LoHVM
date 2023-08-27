# The LoHVM - A High-level Language's Virtual Machine
from hvm.chunk import OpCode, Chunk
from hvm.vm import HVM
    
if __name__ == "__main__":
    vm: HVM = HVM()
    chunk: Chunk = Chunk()

    chunk.add_constant(1.2, 123)
    chunk.add_constant(3.4, 123)
    chunk.write(OpCode.ADD, 123)
    chunk.add_constant(5.6, 123)
    chunk.write(OpCode.DIV, 123)
    chunk.write(OpCode.NEGATE, 123)
    chunk.write(OpCode.RET, 123)

    vm.interpret(chunk)
    
    vm.free()
    chunk.free()
