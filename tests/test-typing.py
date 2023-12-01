from helper import runTest

source = "./asm/typing.asm"
destination = "./output/typing.mem"

exitCode = runTest(source, destination)

print("[TEST]", __file__ + ", exitCode:", exitCode)