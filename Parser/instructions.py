from Lexer.tokens import Token
from Constants.specification import operators, operands, opcodes, registerCodes


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


# attempt to convert to a number, if not possible, returns the orignal string
def tryConvertToNumber(numberString: str) -> int:
    value = None

    try:
        if len(numberString) > 2:
            if numberString[:2] == "0x":
                value = int(numberString, 16)
            elif numberString[:2] == "0b":
                value = int(numberString, 2)
            else:
                value = int(numberString)
        else:
            value = int(numberString)
    except:
        return numberString

    return value


def toHexString(binaryString: str) -> str:
    hexString  = format(int(binaryString[  : 4], 2), 'x')
    hexString += format(int(binaryString[4 : 8], 2), 'x')
    hexString += format(int(binaryString[8 :12], 2), 'x')
    hexString += format(int(binaryString[12:  ], 2), 'x')
    return hexString


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

    # 4 hex characters for regular instruction, 8 if theres an immediate
    # if there is a label then the first 4 chars are hex followed by the label identifer
    # ex. 1010_1011_1100_1101 loop1 -> ABCDloop1
    # Motivation: we may not know the value of the label until the full program is parsed
    def assemble(self) -> str | None:
        if not self.isValid:
            return None

        hexCode = None
        binaryString = ""
        immediate = None
        
        # immediate bit (1)
        if self.hasImmediate or self.hasLabel:
            binaryString += '1'
        else:
            binaryString += '0'

        # opcode bits (5)
        binaryString += opcodes[self.operation]
        
        # unused bits (2)
        binaryString += "00"

        # operand bits (8)
        if self.operandA in registerCodes.keys():
            binaryString += registerCodes[self.operandA]
        else:
            binaryString += registerCodes["immediate"]
            immediate = tryConvertToNumber(self.operandA)

        if self.operandB in registerCodes.keys():
            binaryString += registerCodes[self.operandB]
        else:
            binaryString += registerCodes["immediate"]
            immediate = tryConvertToNumber(self.operandB)

        hexCode = toHexString(binaryString)

        # handle immediate/label
        if self.hasImmediate:
            hexCode += format(immediate, '04x')
        elif self.hasLabel:
            hexCode += immediate

        return hexCode

    def print(self) -> None:
        if self.isValid:
            print(self.operation, self.operandA, self.operandB, "| Immediate:", self.hasImmediate, "| Label:", self.hasLabel)
        else:
            print("Invalid instruction")