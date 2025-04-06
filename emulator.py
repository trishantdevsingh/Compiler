class CPUEmulator:
    def __init__(self, machine_code):
        self.machine_code = machine_code
        self.registers = [0] * 8  # R0-R7
        self.memory = [0] * 256
        self.pc = 0  # Program counter
    
    def run(self):
        while self.pc < len(self.machine_code):
            opcode = self.machine_code[self.pc]
            self.pc += 1
            
            if opcode == 0x10:  # LOAD
                operand = self.machine_code[self.pc]
                #print(operand)
                self.pc += 1
                if isinstance(operand, int):
                # if operand < 128:
                    self.registers[0] = operand
                else:
                    self.registers[0] = self.memory[operand]
            
            elif opcode == 0x11:  # STORE
                addr = self.machine_code[self.pc]
                self.pc += 1
                self.memory[addr] = self.registers[0]
            
            elif opcode == 0x20:  # ADD
                operand = self.machine_code[self.pc]
                self.pc += 1
                if isinstance(operand, int):
                # if operand < 128:
                    self.registers[0] += operand
                else:
                    self.registers[0] += self.memory[operand]
            
            elif opcode == 0x21:  # SUB
                operand = self.machine_code[self.pc]
                self.pc += 1
                if isinstance(operand, int):
                # if operand < 128:
                    self.registers[0] -= operand
                else:
                    self.registers[0] -= self.memory[operand]
            
            elif opcode == 0x22:  # MUL
                operand = self.machine_code[self.pc]
                self.pc += 1
                if isinstance(operand, int):
                # if operand < 128:
                    self.registers[0] *= operand
                else:
                    self.registers[0] *= self.memory[operand]
            
            elif opcode == 0x23:  # DIV
                operand = self.machine_code[self.pc]
                self.pc += 1
                if isinstance(operand, int):
                # if operand < 128:
                    self.registers[0] //= operand
                else:
                    self.registers[0] //= self.memory[operand]
            
            elif opcode == 0xFF:  # Custom inst (msq)
                a = self.machine_code[self.pc]
                self.pc += 1
                # b = self.machine_code[self.pc]
                # self.pc += 1
                
                # Get values
                val_a = a if isinstance(a, int) else self.memory[a]
                # val_b = b if isinstance(b, int) else self.memory[b]
                
                self.registers[0] = ((val_a*val_a) + (self.registers[0]*self.registers[0])) // 2
        
        # Print final state
        print("Execution complete. Final state:")
        print(" ")
        print(f"Registers: {self.registers}")
        print(" ")
        print(f"Memory: {self.memory[:16]}... (first 16 bytes)")
        print(" ")