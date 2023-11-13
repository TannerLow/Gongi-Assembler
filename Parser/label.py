from Lexer.tokens import Token


class Label:
    def __init__(self, tokenSet):
        # Member variables
        self.isValid = False
        self.identifier = None

        # Logic
        if len(tokenSet) == 2 and len(tokenSet[0]) == 2:
            if tokenSet[0][0] == Token.LABEL and tokenSet[1][0] == Token.COLON:
                self.identifier = tokenSet[0][1]
                self.isValid = True

    def print(self) -> None:
        if self.isValid:
            print(self.identifier)
        else:
            print("Invalid label")