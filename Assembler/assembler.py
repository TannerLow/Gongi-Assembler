from Parser.instructions import Instruction
from Parser.label import Label


def assembleInstructions(instructions: list[Instruction | Label]) -> list[str]:
    print("assembling bleep bloop")