import sys
from validation import validateArgs
from Lexer.lexer import lexFile
from Parser.parser import parseTokens
from Assembler.assembler import assembleInstructions


def assemble(filename: str):
    print("[INFO] Assembling", filename)
    lexTokenSets = lexFile(filename)
    if not lexTokenSets or len(lexTokenSets) == 0:
        print("Lexer failed")
        sys.exit(2)
    instructions = parseTokens(lexTokenSets)
    hexCodes = assembleInstructions(instructions)
    

def driver(args: list[str]):
    if not validateArgs(args):
        sys.exit(1)
    assemble(args[1])


if __name__ == '__main__':
    driver(sys.argv)