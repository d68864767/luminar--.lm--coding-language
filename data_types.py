```python
class DataType:
    def __init__(self, name, default_value):
        self.name = name
        self.default_value = default_value

class Integer(DataType):
    def __init__(self):
        super().__init__('Integer', 0)

class String(DataType):
    def __init__(self):
        super().__init__('String', "")

class Boolean(DataType):
    def __init__(self):
        super().__init__('Boolean', False)

class Array(DataType):
    def __init__(self, element_type):
        super().__init__('Array', [])
        self.element_type = element_type

class List(DataType):
    def __init__(self, element_type):
        super().__init__('List', [])
        self.element_type = element_type

class Dictionary(DataType):
    def __init__(self, key_type, value_type):
        super().__init__('Dictionary', {})
        self.key_type = key_type
        self.value_type = value_type

class DataTypeError(Exception):
    pass

class DataTypeChecker:
    def __init__(self):
        self.data_types = {
            'Integer': Integer(),
            'String': String(),
            'Boolean': Boolean(),
            'Array': Array(None),
            'List': List(None),
            'Dictionary': Dictionary(None, None)
        }

    def check(self, data_type, value):
        if data_type not in self.data_types:
            raise DataTypeError(f'Invalid data type: {data_type}')

        if isinstance(value, self.data_types[data_type].__class__):
            return True
        else:
            return False
```
