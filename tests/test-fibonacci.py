from helper import runTest

source = "./asm/fibonacci.asm"
destination = "./output/fibonacci.mem"

exitCode = runTest(source, destination)

print("[TEST]", __file__ + ", exitCode:", exitCode)