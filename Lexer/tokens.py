from enum import Enum
from validation import isNumericLiteral
from Constants.specification import comment, operators, operands


class Token(Enum):
    OPERATOR = 1
    OPERAND = 2
    COMMA = 3
    COLON = 4
    NUMERIC_LITERAL = 5
    LABEL = 6

    @classmethod
    def categorize(cls, tokenString: str) -> 'Token':
        if tokenString in operators.keys():
            return cls.OPERATOR
        elif tokenString in operands["any"]:
            return cls.OPERAND
        elif tokenString == ",":
            return cls.COMMA
        elif tokenString == ":":
            return cls.COLON
        elif isNumericLiteral(tokenString):
            return cls.NUMERIC_LITERAL
        else:
            return cls.LABEL

