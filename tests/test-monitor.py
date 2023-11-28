from helper import runTest

source = "./asm/monitor.asm"
destination = "./output/monitor.mem"

exitCode = runTest(source, destination)

print("[TEST]", __file__ + ", exitCode:", exitCode)