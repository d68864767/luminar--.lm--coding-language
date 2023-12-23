```python
from lexer import Token, Lexer
from parser import Parser, ParserError

class InterpreterError(Exception):
    pass

class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, tokens):
        parser = Parser(iter(tokens))
        parser.parse(self)

    def assign(self, name, value):
        self.variables[name] = value

    def lookup(self, name):
        if name not in self.variables:
            raise InterpreterError(f'Undefined variable {name}')
        return self.variables[name]

    def start_if(self, condition_variable):
        if self.lookup(condition_variable):
            return True
        else:
            return False

    def start_for(self, start, end):
        # This is a very simplified version of a for loop
        # In a real language, you would need to handle more complex expressions
        return range(self.lookup(start), self.lookup(end))

    def start_while(self, condition_variable):
        while self.lookup(condition_variable):
            return True
        return False

if __name__ == "__main__":
    code = """
    x = 5;
    if (x) {
        y = 10;
    }
    """

    lexer = Lexer(code)
    tokens = lexer.tokenize()
    interpreter = Interpreter()
    interpreter.interpret(tokens)
    print(interpreter.variables)
```
