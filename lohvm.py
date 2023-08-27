# The LoHVM - A High-level Language's Virtual Machine
from hvm.chunk import OpCode, Chunk
    
if __name__ == "__main__":
    chunk: Chunk = Chunk()
    chunk.add_constant(1.0, 123)
    chunk.write(OpCode.RET, 123)
    chunk.disassemble("test chunk")
    chunk.free()
