import json

# Define your lexer
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def get_next_token(self):
        if self.pos >= len(self.text):
            return Token(TokenTypes.EOF, None)

        current_char = self.text[self.pos]

        if current_char.isdigit():
            value = int(current_char)
            self.pos += 1
            return Token(TokenTypes.INT, value)

        if current_char == '+':
            self.pos += 1
            return Token(TokenTypes.PLUS, current_char)

        if current_char == '-':
            self.pos += 1
            return Token(TokenTypes.MINUS, current_char)

        if current_char == '*':
            self.pos += 1
            return Token(TokenTypes.MULTIPLY, current_char)

        if current_char == '/':
            self.pos += 1
            return Token(TokenTypes.DIVIDE, current_char)

        raise ValueError(f'Invalid character: {current_char}')

# Define your parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        left = self.parse_term()

        while self.peek().type in (TokenTypes.PLUS, TokenTypes.MINUS):
            op = self.get_next_token()
            right = self.parse_term()

            if op.type == TokenTypes.PLUS:
                left += right
            elif op.type == TokenTypes.MINUS:
                left -= right

        return left

    def parse_term(self):
        left = self.parse_factor()

        while self.peek().type in (TokenTypes.MULTIPLY, TokenTypes.DIVIDE):
            op = self.get_next_token()
            right = self.parse_factor()

            if op.type == TokenTypes.MULTIPLY:
                left *= right
            elif op.type == TokenTypes.DIVIDE:
                left /= right

        return left

    def parse_factor(self):
        token = self.get_next_token()

        if token.type == TokenTypes.INT:
            return token.value

        raise ValueError('Expected an integer')

    def peek(self):
        if self.pos >= len(self.tokens):
            return Token(TokenTypes.EOF, None)

        return self.tokens[self.pos]

    def get_next_token(self):
        if self.pos >= len(self.tokens):
            return Token(TokenTypes.EOF, None)

        token = self.tokens[self.pos]
        self.pos += 1
        return token

# Define your Token and TokenTypes classes
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'

class TokenTypes:
    INT = 'INT'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    EOF = 'EOF'

# Define your main function
def main():
    with open('data.json', 'r') as f:
        data = json.load(f)

    source_code = data['source_code']

    lexer = Lexer(source_code)
    tokens = []
    token = lexer.get_next_token()

    while token.type != TokenTypes.EOF:
        tokens.append(token)
        token
