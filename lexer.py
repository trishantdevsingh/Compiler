import re

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_pos = 0
        self.keywords = {'ADD', 'SUB', 'MUL', 'DIV', 'MSQ'}

    def tokenize(self):
        token_specs = [
            ('NUMBER', r'\d+'),
            ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('ASSIGN', r'='),
            ('SEMICOLON', r';'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('COMMA', r','),
            ('WHITESPACE', r'\s+'),
        ]
        
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)
        
        for mo in re.finditer(tok_regex, self.source_code):
            kind = mo.lastgroup
            value = mo.group()
            
            if kind == 'WHITESPACE':
                continue
            elif kind == 'ID' and value in self.keywords:
                kind = value
                
            self.tokens.append((kind, value))
        
        return self.tokens