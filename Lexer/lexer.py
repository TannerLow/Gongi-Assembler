from .tokens import Token
from Constants.specification import comment


def stripComment(asmLine: str) -> str:
    return asmLine.split(comment)[0]


def identifyCommas(tokenStrings: list[str]) -> list[str]:
    for i in range(len(tokenStrings)):
        lastIndex = len(tokenStrings[i]) - 1
        if tokenStrings[i][lastIndex] == ",":
            tokenStrings[i] = tokenStrings[i][:-1]
            tokenStrings.insert(i + 1, ",")
            break
    return tokenStrings


def identifyColon(tokenStrings: list[str]) -> list[str]:
    for i in range(len(tokenStrings)):
        lastIndex = len(tokenStrings[i]) - 1
        if tokenStrings[i][lastIndex] == ":":
            tokenStrings[i] = tokenStrings[i][:-1]
            tokenStrings.insert(i + 1, ":")
            break
    return tokenStrings


def toLower(tokenStrings: list[str]) -> list[str]:
    for i in range(len(tokenStrings)):
        tokenStrings[i] = tokenStrings[i].lower()
    return tokenStrings


def categorizeTokenStrings(tokenStrings: list[str]) -> list[list[Token | str]]:
    categorizedTokens = []
    for tokenString in tokenStrings:
        token = Token.categorize(tokenString)
        categorizedTokens.append([token, tokenString])
    return categorizedTokens


def removeEmptyTokenSets(tokenSets):
    return [tokenSet for tokenSet in tokenSets if len(tokenSet) != 0]


def lexFile(filename: str) -> list[list[list[Token | str]]]:
    lines = None
    with open(filename, 'r') as file:
        lines = file.readlines()

    if not lines:
        print("Unable to read file or file is empty:", filename)
        return None

    tokenSets = []
    for line in lines:
        line = line.strip()
        line = stripComment(line)
        tokenStrings = line.split()
        tokenStrings = identifyCommas(tokenStrings)
        tokenStrings = identifyColon(tokenStrings)
        tokenStrings = toLower(tokenStrings)
        categorizedTokens = categorizeTokenStrings(tokenStrings)
        if len(categorizedTokens) != 0:
            tokenSets.append(categorizedTokens)
    return tokenSets


