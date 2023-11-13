from Lexer.tokens import Token
from Constants.specification import operators, operands


dst = [
    [Token.OPERAND]
]

any = [
    [Token.OPERAND],
    [Token.NUMERIC_LITERAL]
]

any_or_label = any
any_or_label.append([Token.LABEL])

dst_any = [
    [Token.OPERAND, Token.COMMA, Token.OPERAND],
    [Token.OPERAND, Token.COMMA, Token.NUMERIC_LITERAL]
]

validInstructionTokenSets = dict()
for operation, params in operators.items():
    if params == ["dst", "any"] or params == ["reg", "any"]:
        validInstructionTokenSets[operation] = dst_any
    elif params == ["any"]:
        validInstructionTokenSets[operation] = any
    elif params == ["dst"]:
        validInstructionTokenSets[operation] = dst
    elif params == ["any|label"]:
        validInstructionTokenSets[operation] = any_or_label
    else:
        validInstructionTokenSets[operation] = [[]]


class Instruction:
    def __init__(self, tokens):
        # Member variables
        self.isValid = False

        self.hasImmediate = False
        self.hasLabel = False

        self.operation = "nop"
        self.operandA = "nil"
        self.operandB = "nil"

        # Logic
        if tokens[0][0] == Token.OPERATOR:
            operator = tokens[0][1]
            tokenTypes = []
            for i in range(1, len(tokens)):
                tokenTypes.append(tokens[i][0])
            if tokenTypes in validInstructionTokenSets[operator]:
                if self.followsEdgeCases(tokens, operator, tokenTypes):
                    self.isValid = True
                    self.operation = operator
                    self.hasImmediate = Token.NUMERIC_LITERAL in tokenTypes
                    self.hasLabel = Token.LABEL in tokenTypes
                    if len(tokenTypes) == 1:
                        if operator == "not":
                            self.operandB = tokens[1][1]
                        else:
                            self.operandA = tokens[1][1]
                    elif len(tokenTypes) == 3:
                        self.operandA = tokens[1][1]
                        self.operandB = tokens[3][1]

    # Returns False if instruction does not abide by edge cases
    def followsEdgeCases(self, tokens, operator, tokenTypes) -> bool:
        if operators[operator][0] == "dst":
            if tokens[1][1] not in operands["dst"]:
                return False
        if operators[operator][0] == "reg":
            if tokenTypes[0] == Token.NUMERIC_LITERAL:
                return False
        return True

    def print(self) -> None:
        if self.isValid:
            print(self.operation, self.operandA, self.operandB, "| Immediate:", self.hasImmediate, "| Label:", self.hasLabel)
        else:
            print("Invalid instruction")