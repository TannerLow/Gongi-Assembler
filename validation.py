import os


def validateFilename(filename: str) -> bool:
    if os.path.isfile(filename):
        return True
    else:
        print("File not found:", filename)
        return False


def validateArgs(args: list[str]) -> bool:
    filename = args[0]
    usage = filename + " <asm_file> <output_file>"
    argc = len(args)
    if argc < 3:
        print("Not enough arguments")
        print(usage)
        return False
    elif argc == 3:
        return validateFilename(args[1])
    else:
        print("Invalid arguments")
        print(usage)
        return False


def isNumericLiteral(tokenString: str) -> bool:
    try:
        if len(tokenString) > 2:
            if tokenString[:2] == "0x":
                int(tokenString, 16)
            elif tokenString[:2] == "0b":
                int(tokenString, 2)
            else:
                int(tokenString)
        else:
            int(tokenString)
    except:
        return False
    
    return True