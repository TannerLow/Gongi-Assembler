from Parser.instructions import Instruction
from Parser.label import Label


def assembleInstructions(instructions: list[Instruction | Label]) -> list[str]:
    hexCodes = []

    labelLookupTable = dict()
    labelPlaceHolders = dict()

    for instruction in instructions:
        if isinstance(instruction, Label):
            labelLookupTable[instruction.identifier] = len(hexCodes)
            continue
        else:
            hexCode = instruction.assemble()
        
        if not hexCode:
            print("[Error] Failed during assembly TODO fail gracefully")
            exit(4)
        
        hexCodes.append(hexCode[:4])
        if len(hexCode) > 4:
            extra = hexCode[4:]

            if instruction.hasLabel:
                if extra in labelPlaceHolders.keys():
                    labelPlaceHolders[extra].append(len(hexCodes))
                else:
                    labelPlaceHolders[extra] = [len(hexCodes)]

            hexCodes.append(extra)

    # fill in placeholders for labels we've seen
    for label, placeholders in labelPlaceHolders.items():
        for index in placeholders:
            if label in labelLookupTable.keys():
                hexCodes[index] = format(labelLookupTable[label], "04x")
            else:
                print("[Error] Reference to non-existant label TODO fail gracefully")
                exit(5)
    
    # for code in hexCodes:
    #     print(code)

    return hexCodes