from helper import runTest

source = "./asm/simple_typing_2.asm"
destination = "./output/simple_typing_2.mem"

exitCode = runTest(source, destination)

print("[TEST]", __file__ + ", exitCode:", exitCode)