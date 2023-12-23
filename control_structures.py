```python
from lexer import Token, Lexer
from data_types import Integer, String, Boolean, Array, List

class ControlStructure:
    def __init__(self, name):
        self.name = name

class IfStatement(ControlStructure):
    def __init__(self, condition, true_block, false_block=None):
        super().__init__('IfStatement')
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

class ForLoop(ControlStructure):
    def __init__(self, variable, iterable, block):
        super().__init__('ForLoop')
        self.variable = variable
        self.iterable = iterable
        self.block = block

class WhileLoop(ControlStructure):
    def __init__(self, condition, block):
        super().__init__('WhileLoop')
        self.condition = condition
        self.block = block

class FunctionDefinition(ControlStructure):
    def __init__(self, name, parameters, block):
        super().__init__('FunctionDefinition')
        self.name = name
        self.parameters = parameters
        self.block = block

class FunctionCall(ControlStructure):
    def __init__(self, function, arguments):
        super().__init__('FunctionCall')
        self.function = function
        self.arguments = arguments

class LambdaFunction(ControlStructure):
    def __init__(self, parameters, expression):
        super().__init__('LambdaFunction')
        self.parameters = parameters
        self.expression = expression

class ListComprehension(ControlStructure):
    def __init__(self, expression, iterable, condition=None):
        super().__init__('ListComprehension')
        self.expression = expression
        self.iterable = iterable
        self.condition = condition
```
