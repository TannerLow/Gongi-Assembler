from helper import runTest

source = "./asm/simple_typing.asm"
destination = "./output/simple_typing.mem"

exitCode = runTest(source, destination)

print("[TEST]", __file__ + ", exitCode:", exitCode)