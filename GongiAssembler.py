import sys
from validation import validateArgs
from Lexer.lexer import lexFile
from Parser.parser import parseTokens
from Assembler.assembler import assembleInstructions


def saveToFile(outputFilename: str, hexCodes: list[str]) -> None:
    with open(outputFilename, 'w') as file:
        for hexCode in hexCodes:
            file.write(hexCode + '\n')


def assemble(filename: str, outputFilename: str) -> None:
    print("[INFO] Assembling", filename)
    lexTokenSets = lexFile(filename)
    if not lexTokenSets or len(lexTokenSets) == 0:
        print("Lexer failed")
        sys.exit(2)
    instructions = parseTokens(lexTokenSets)
    hexCodes = assembleInstructions(instructions)
    saveToFile(outputFilename, hexCodes)
    print("[INFO] Done")

def driver(args: list[str]) -> None:
    if not validateArgs(args):
        sys.exit(1)
    assemble(args[1], args[2])


if __name__ == '__main__':
    driver(sys.argv)