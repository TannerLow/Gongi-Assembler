from helper import runTest

source = "./asm/registers.asm"
destination = "./output/registers.mem"

exitCode = runTest(source, destination)

print("[TEST]", __file__ + ", exitCode:", exitCode)