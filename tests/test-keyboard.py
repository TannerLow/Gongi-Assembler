from helper import runTest

source = "./asm/keyboard.asm"
destination = "./output/keyboard.mem"

exitCode = runTest(source, destination)

print("[TEST]", __file__ + ", exitCode:", exitCode)