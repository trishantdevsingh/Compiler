class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()
    
    def next_token(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = None
        return self.current_token
    
    def parse(self):
        statements = []
        while self.current_token:
            if self.current_token[0] == 'ID':
                var_name = self.current_token[1]
                self.next_token()  # Skip ID
                if self.current_token and self.current_token[0] == 'ASSIGN':
                    statements.append(self.parse_assignment(var_name))
            else:
                self.next_token()
        return statements
    
    def parse_assignment(self, var_name):
        self.next_token()  # Skip =
        if self.current_token[0] in {'ADD', 'SUB', 'MUL', 'DIV', 'MSQ'}:
            op = self.current_token[0]
            self.next_token()  # Skip op
            self.next_token()  # Skip (
            arg1 = self.current_token[1]
            self.next_token()  # Skip ,
            self.next_token()  # Skip , yoyoyyoyoyoyyoyoyoyoyyoyoyoyyoyo
            arg2 = self.current_token[1]
            self.next_token()  # Skip )
            self.next_token()  # Skip ;
            return ('ASSIGN', var_name, (op, arg1, arg2))
        else:  # Direct assignment
            value = self.current_token[1]
            self.next_token()  # Skip number
            self.next_token()  # Skip ;
            return ('ASSIGN', var_name, value)
    
    def parse_operation(self):
        op = self.current_token[0]
        self.next_token()  # Skip op
        self.next_token()  # Skip (
        arg1 = self.current_token[1]
        self.next_token()  # Skip ,
        arg2 = self.current_token[1]
        self.next_token()  # Skip )
        self.next_token()  # Skip ;
        return (op, arg1, arg2)
    
    def parse_avg(self):
        self.next_token()  # Skip AVG
        self.next_token()  # Skip (
        arg1 = self.current_token[1]
        self.next_token()  # Skip ,
        arg2 = self.current_token[1]
        self.next_token()  # Skip )
        self.next_token()  # Skip ;
        return ('MSQ', arg1, arg2)
    
    def parse_expression(self):
        if self.current_token[0] in {'ADD', 'SUB', 'MUL', 'DIV', 'MSQ'}:
            return self.parse_operation()
        else:
            return self.current_token[1]