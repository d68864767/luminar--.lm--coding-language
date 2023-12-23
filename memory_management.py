```python
class MemoryManager:
    def __init__(self):
        self.memory = {}

    def allocate(self, name, data_type):
        if name in self.memory:
            raise NameError(f'Variable {name} already exists.')
        self.memory[name] = data_type.default_value

    def deallocate(self, name):
        if name not in self.memory:
            raise NameError(f'Variable {name} does not exist.')
        del self.memory[name]

    def read(self, name):
        if name not in self.memory:
            raise NameError(f'Variable {name} does not exist.')
        return self.memory[name]

    def write(self, name, value, data_type_checker):
        if name not in self.memory:
            raise NameError(f'Variable {name} does not exist.')
        if not data_type_checker.check(type(value).__name__, value):
            raise TypeError(f'Invalid value for variable {name}. Expected {type(self.memory[name]).__name__}, got {type(value).__name__}.')
        self.memory[name] = value

class MemoryError(Error):
    def __init__(self, description):
        super().__init__('MemoryError', description)
```
