```python
class ExtensionError(Exception):
    pass

class Extension:
    def __init__(self, name, source_code):
        self.name = name
        self.source_code = source_code

class ExtensionManager:
    def __init__(self):
        self.extensions = {}

    def load_extension(self, extension):
        if extension.name in self.extensions:
            raise ExtensionError(f'Extension {extension.name} already loaded')
        self.extensions[extension.name] = extension

    def unload_extension(self, name):
        if name not in self.extensions:
            raise ExtensionError(f'Extension {name} not loaded')
        del self.extensions[name]

    def get_extension(self, name):
        if name not in self.extensions:
            raise ExtensionError(f'Extension {name} not loaded')
        return self.extensions[name]

    def execute_extension(self, name, interpreter):
        extension = self.get_extension(name)
        lexer = Lexer(extension.source_code)
        tokens = lexer.tokenize()
        interpreter.interpret(tokens)
```
