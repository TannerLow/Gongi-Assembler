from helper import runTest

source = "./asm/carry.asm"
destination = "./output/carry.mem"

exitCode = runTest(source, destination)

print("[TEST]", __file__ + ", exitCode:", exitCode)