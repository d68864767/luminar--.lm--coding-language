```python
from lexer import Token, Lexer

class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token = None
        self._advance()

    def _advance(self):
        self.current_token, self.next_token = self.next_token, next(self.tokens, None)

    def parse(self):
        while self.current_token is not None:
            if self.current_token.type == 'KEYWORD':
                self._parse_keyword()
            elif self.current_token.type == 'NAME':
                self._parse_assignment()
            else:
                raise ParserError(f'Unexpected token {self.current_token.type}')

    def _parse_keyword(self):
        keyword = self.current_token.value

        if keyword == 'if':
            self._parse_if_statement()
        elif keyword == 'for':
            self._parse_for_loop()
        elif keyword == 'while':
            self._parse_while_loop()
        else:
            raise ParserError(f'Unexpected keyword {keyword}')

    def _parse_assignment(self):
        name = self.current_token.value
        self._advance()

        if self.current_token.type != 'EQUALS':
            raise ParserError('Expected equals sign in assignment')

        self._advance()

        if self.current_token.type not in ['NUMBER', 'STRING', 'NAME']:
            raise ParserError('Expected number, string, or variable in assignment')

        value = self.current_token.value
        self._advance()

        # Here you would typically assign the value to the variable in your interpreter's
        # symbol table, but since this is just the parser, we'll print the assignment instead
        print(f'{name} = {value}')

    def _parse_if_statement(self):
        # This is a very simplified version of parsing an if statement
        # In a real language, you would need to handle expressions, nested statements, etc.
        self._advance()

        if self.current_token.type != 'LPAREN':
            raise ParserError('Expected left parenthesis after "if" keyword')

        self._advance()

        if self.current_token.type != 'NAME':
            raise ParserError('Expected variable in if condition')

        condition_variable = self.current_token.value
        self._advance()

        if self.current_token.type != 'RPAREN':
            raise ParserError('Expected right parenthesis after if condition')

        self._advance()

        if self.current_token.type != 'LBRACE':
            raise ParserError('Expected left brace after if condition')

        # Here you would typically start a new scope in your interpreter, but since this is
        # just the parser, we'll print the start of the if statement instead
        print(f'if ({condition_variable}) {{')

        self._advance()

        while self.current_token.type != 'RBRACE':
            self.parse()

        print('}')

    def _parse_for_loop(self):
        # This is left as an exercise for the reader
        pass

    def _parse_while_loop(self):
        # This is left as an exercise for the reader
        pass

if __name__ == "__main__":
    code = """
    x = 5;
    if (x) {
        y = 10;
    }
    """

    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(iter(tokens))
    parser.parse()
```
