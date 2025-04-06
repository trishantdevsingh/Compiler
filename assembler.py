class Assembler:
    def __init__(self, intermediate_code):
        self.intermediate_code = intermediate_code
        self.machine_code = []
        self.opcodes = {
            'LOAD': 0x10,
            'STORE': 0x11,
            'ADD': 0x20,
            'SUB': 0x21,
            'MUL': 0x22,
            'DIV': 0x23,
        }
        self.vars = {}
        self.next_var_addr = 0
    
    def assemble(self):
        for instruction in self.intermediate_code:
            parts = instruction.split()
            op = parts[0]
            
            if op in self.opcodes:
                self.machine_code.append(self.opcodes[op])
                if len(parts) > 1:
                    operand = parts[1]
                    if operand.isdigit():
                        self.machine_code.append(int(operand))
                    else:
                        if operand not in self.vars:
                            self.vars[operand] = self.next_var_addr
                            self.next_var_addr += 1
                        self.machine_code.append(self.vars[operand]) # yoyoyoyoyyoyoyoyyoyoyoyyoyoyoyoyoy
            elif op == 'MSQ':
                # Custom AVG instruction
                self.machine_code.append(0xFF)  # Custom opcode
                if len(parts) > 1:
                    operand = parts[1]
                    if operand.isdigit():
                        self.machine_code.append(int(operand))
                    else:
                        if operand not in self.vars:
                            self.vars[operand] = self.next_var_addr
                            self.next_var_addr += 1
                        self.machine_code.append(self.vars[operand])
                # arg1, arg2 = parts[1], parts[2]
                # self.process_operand(arg1)
                # self.process_operand(arg2)
        
        return bytes(self.machine_code)#yoyoyoyoyooyyoo
    
    def process_operand(self, operand):
        if operand.isdigit():
            self.machine_code.append(int(operand))
        else:
            if operand not in self.vars:
                self.vars[operand] = self.next_var_addr
                self.next_var_addr += 1
            self.machine_code.append(self.vars[operand])