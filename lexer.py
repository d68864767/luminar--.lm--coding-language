```python
import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        # Define the regular expressions for each token
        token_specs = [
            ('NUMBER',   r'\b\d+\b'),
            ('STRING',   r'"[^"]*"'),
            ('NAME',     r'\b[A-Za-z_][A-Za-z_0-9]*\b'),
            ('OPERATOR', r'[+\-*/]'),
            ('EQUALS',   r'='),
            ('LPAREN',   r'\('),
            ('RPAREN',   r'\)'),
            ('LBRACE',   r'\{'),
            ('RBRACE',   r'\}'),
            ('COMMA',    r','),
            ('SEMICOLON',r';'),
            ('NEWLINE',  r'\n'),
            ('SKIP',     r'[ \t]+'),  # Skip over spaces and tabs
            ('MISMATCH', r'.')        # Any other character
        ]

        # Join all the regular expressions into a single one
        regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)

        # Initialize the list of tokens
        tokens = []

        # Scan the source code and generate tokens
        for mo in re.finditer(regex, self.source_code):
            kind = mo.lastgroup
            value = mo.group()

            if kind == 'NUMBER':
                value = int(value)
            elif kind == 'STRING':
                value = value[1:-1]  # Remove the quotes
            elif kind == 'NAME' and value in ['if', 'else', 'for', 'while']:
                kind = 'KEYWORD'

            if kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'{value!r} unexpected')

            tokens.append(Token(kind, value))

        return tokens
```
