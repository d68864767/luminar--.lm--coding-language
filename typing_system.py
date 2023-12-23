```python
from data_types import DataTypeChecker, DataTypeError

class TypingSystem:
    def __init__(self):
        self.data_type_checker = DataTypeChecker()

    def check_type(self, data_type, value):
        try:
            return self.data_type_checker.check(data_type, value)
        except DataTypeError as e:
            print(e)
            return False

    def cast(self, data_type, value):
        if self.check_type(data_type, value):
            return value
        else:
            try:
                if data_type == 'Integer':
                    return int(value)
                elif data_type == 'String':
                    return str(value)
                elif data_type == 'Boolean':
                    return bool(value)
                elif data_type == 'Array':
                    return list(value)
                elif data_type == 'List':
                    return list(value)
                elif data_type == 'Dictionary':
                    return dict(value)
                else:
                    raise DataTypeError(f'Cannot cast {value} to {data_type}')
            except (ValueError, TypeError):
                raise DataTypeError(f'Cannot cast {value} to {data_type}')

    def declare_variable(self, data_type, name, value=None):
        if value is None:
            value = self.data_type_checker.data_types[data_type].default_value
        else:
            value = self.cast(data_type, value)

        return {name: value}
```
