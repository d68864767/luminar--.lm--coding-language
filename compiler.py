```python
from lexer import Token, Lexer
from parser import Parser, ParserError
from interpreter import Interpreter, InterpreterError

class CompilerError(Exception):
    pass

class Compiler:
    def __init__(self):
        self.interpreter = Interpreter()

    def compile(self, source_code):
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()

        try:
            parser = Parser(iter(tokens))
            parser.parse(self.interpreter)
        except ParserError as e:
            raise CompilerError(f'Parser error: {e}')
        except InterpreterError as e:
            raise CompilerError(f'Interpreter error: {e}')

        return self._generate_bytecode()

    def _generate_bytecode(self):
        # This is a very simplified version of a compiler
        # In a real compiler, you would generate bytecode or machine code
        # Here we'll just return the interpreter's symbol table as a string
        return str(self.interpreter.variables)

if __name__ == "__main__":
    code = """
    x = 5;
    if (x) {
        y = 10;
    }
    """

    compiler = Compiler()
    output = compiler.compile(code)
    print(output)
```
