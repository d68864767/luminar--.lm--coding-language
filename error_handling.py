```python
class Error:
    def __init__(self, error_name, description):
        self.error_name = error_name
        self.description = description

    def __str__(self):
        return f'{self.error_name}: {self.description}'

class ErrorHandler:
    def __init__(self):
        self.errors = []

    def new_error(self, error_name, description):
        self.errors.append(Error(error_name, description))

    def has_errors(self):
        return len(self.errors) > 0

    def report_errors(self):
        for error in self.errors:
            print(error)

    def clear_errors(self):
        self.errors = []

class SyntaxError(Error):
    def __init__(self, description):
        super().__init__('SyntaxError', description)

class TypeError(Error):
    def __init__(self, description):
        super().__init__('TypeError', description)

class NameError(Error):
    def __init__(self, description):
        super().__init__('NameError', description)

class ValueError(Error):
    def __init__(self, description):
        super().__init__('ValueError', description)

class RuntimeError(Error):
    def __init__(self, description):
        super().__init__('RuntimeError', description)
```
