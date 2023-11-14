import os


def runTest(source: str, destination: str) -> int:
    folderName = "output"
    if not os.path.exists(folderName):
        os.makedirs(folderName)

    exitCode = os.system("python ../GongiAssembler.py " + source + " " + destination)

    return exitCode