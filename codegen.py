class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.code = []
        self.var_count = 0
    
    def generate(self):
        for node in self.ast:
            if node[0] == 'ASSIGN':
                self.generate_assignment(node)
        return self.code
    
    def generate_assignment(self, node):
        var_name, expr = node[1], node[2]
        if isinstance(expr, tuple):  # Operation
            op, arg1, arg2 = expr
            self.code.append(f'LOAD {arg1}')
            self.code.append(f'{op} {arg2}')
            # if op == 'AVG':
                # self.code.append('DIV 2')
                # self.code.append('DIV')
            self.code.append(f'STORE {var_name}')
        else:  # Direct assignment
            self.code.append(f'LOAD {expr}')
            self.code.append(f'STORE {var_name}')
    
    def generate_operation(self, node):
        op, arg1, arg2 = node
        self.code.append(f'LOAD {arg1}')
        
        if op == 'ADD':
            self.code.append(f'ADD {arg2}')
        elif op == 'SUB':
            self.code.append(f'SUB {arg2}')
        elif op == 'MUL':
            self.code.append(f'MUL {arg2}')
        elif op == 'DIV':
            self.code.append(f'DIV {arg2}')
        elif op == 'MSQ':
            self.code.append(f'MSQ {arg2}')
            # self.code.append('DIV 2')
            # self.code.append('DIV')