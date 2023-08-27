# Constant Pool for chunks

class Value:
    def __init__(self) -> None:
        self.values = []
    
    def write(self, value: float) -> None:
        self.values.append(value)
    
    def free(self) -> None:
        self.values.clear()