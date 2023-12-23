```python
import unittest
from lexer import Lexer, Token
from parser import Parser, ParserError
from interpreter import Interpreter, InterpreterError
from compiler import Compiler, CompilerError
from data_types import Integer, String, Boolean
from control_structures import If, For, While

class TestLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer('')

    def test_tokenize_number(self):
        self.lexer.source_code = '123'
        tokens = self.lexer.tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, 'NUMBER')
        self.assertEqual(tokens[0].value, 123)

    def test_tokenize_string(self):
        self.lexer.source_code = '"hello"'
        tokens = self.lexer.tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, 'STRING')
        self.assertEqual(tokens[0].value, 'hello')

    # Add more tests for the lexer...

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser(iter([]))

    def test_parse_assignment(self):
        self.parser.tokens = iter([Token('NAME', 'x'), Token('EQUALS', '='), Token('NUMBER', 123)])
        self.parser._advance()
        self.parser._parse_assignment()
        self.assertEqual(self.parser.current_token, None)

    def test_parse_assignment_error(self):
        self.parser.tokens = iter([Token('NAME', 'x'), Token('NUMBER', 123)])
        self.parser._advance()
        with self.assertRaises(ParserError):
            self.parser._parse_assignment()

    # Add more tests for the parser...

class TestInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def test_assign_and_lookup(self):
        self.interpreter.assign('x', 123)
        self.assertEqual(self.interpreter.lookup('x'), 123)

    def test_lookup_error(self):
        with self.assertRaises(InterpreterError):
            self.interpreter.lookup('x')

    # Add more tests for the interpreter...

class TestCompiler(unittest.TestCase):
    def setUp(self):
        self.compiler = Compiler()

    def test_compile(self):
        source_code = 'x = 123'
        self.compiler.compile(source_code)
        self.assertEqual(self.compiler.interpreter.lookup('x'), 123)

    def test_compile_error(self):
        source_code = 'x = '
        with self.assertRaises(CompilerError):
            self.compiler.compile(source_code)

    # Add more tests for the compiler...

# Add tests for data types and control structures...

if __name__ == '__main__':
    unittest.main()
```
