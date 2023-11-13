from Lexer.tokens import Token
from .instructions import Instruction
from .label import Label


# may need changes to support macro operands, suggestion: make a preParser
def parseTokens(lexTokenSets: list[list[list[Token | str]]]) -> list[Instruction | Label]:
    instructions = []
    for tokenSet in lexTokenSets:
        if tokenSet[0][0] == Token.OPERATOR:
            instructions.append(Instruction(tokenSet))
        elif tokenSet[0][0] == Token.LABEL:
            instructions.append(Label(tokenSet))
        else:
            print("Parser encountered erro TODO fail gracefully")
            exit(3)
    return instructions

