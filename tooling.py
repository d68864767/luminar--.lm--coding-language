```python
class ToolingError(Exception):
    pass

class IDE:
    def __init__(self, compiler):
        self.compiler = compiler

    def run_code(self, source_code):
        try:
            tokens = self.compiler.lexer.tokenize(source_code)
            self.compiler.parser.parse(tokens)
            self.compiler.interpreter.interpret(tokens)
        except Exception as e:
            raise ToolingError(f'Error while running code: {str(e)}')

class Debugger:
    def __init__(self, interpreter):
        self.interpreter = interpreter

    def debug(self, tokens):
        try:
            self.interpreter.interpret(tokens)
        except Exception as e:
            raise ToolingError(f'Error while debugging: {str(e)}')

class Linter:
    def __init__(self, parser):
        self.parser = parser

    def lint(self, tokens):
        try:
            self.parser.parse(tokens)
        except Exception as e:
            raise ToolingError(f'Error while linting: {str(e)}')
```
