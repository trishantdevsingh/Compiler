## 👤 Author

**Trishant Dev Singh**  
📧 Email: tdsingh099.btech2023@cse.nitrr.ac.in <br>
🎓 Roll No: 23115099  
📚 Semester: 4th  
🏫 College: NIT Raipur  
🧠 Branch: Computer Science and Engineering

---

# Custom Instruction Compiler Project

This project demonstrates a minimal compiler pipeline for a language that detects a specific pattern in expressions and replaces it with a custom assembly instruction `MSQ`.

---

## 🔧 Features

- **Lexical Analysis:** Tokenizes source code using regular expressions.
- **Parsing:** Builds an Abstract Syntax Tree (AST) using a recursive descent parser.
- **Intermediate Code Generation:** Outputs pseudo-assembly instructions(One Address Code).
- **Assembler:** Converts Intermediate code to machine code.
- **Linker:** Makes an object file (test.o)
- **Emulator:** Simulates a CPU and Executes the code to provide actual results.

---

## 📁 File Overview

| File                | Purpose |
|---------------------|---------|
| `lexer.py`          | Converts raw source code into a stream of tokens. |
| `parser.py`         | Builds the AST-like structure. |
| `codegen.py`        | Generates pseudo-assembly code. |
| `assembler.py`      | Generates machine code. |
| `linker.py`         | Creates a object file from machine code. |
| `emulator.py`       | Executes the machine code by mimicking a CPU. |
| `compiler.py`       | Main file for connecting all components. |
| `test.math`         | Contains an example test code segment. |

---

## 🧩 Dependencies:
 - **OS:** Linux, MacOS, Windows(8+)
 - **Python :** 3.10+

---

## 🚀 How to Run

### Step 1: Clone the Repository
```bash
    git clone https://github.com/trishantdevsingh/Compiler.git
    cd Compiler
```

### Step 2: Compile the test.math file by
```bash
    python3 compiler.py test.math test.o
```

This will:
- Print token stream
- Print AST
- Print the one address code
- Print the machine code
- Generate and save `test.o`
- Print result of simulated execution
---

## 💡 Example

### Sample Input (Code.py)
```
    x = ADD(5, 3);
    y = SUB(10, 2);
    z = MUL(4, 5);
    w = DIV(20, 4);
    result = MSQ(2 , 4);
```

### Console Output
```bash
    <====Tokenisation====>

    ('ID', 'x')
    ('ASSIGN', '=')
    ('ADD', 'ADD')
    ('LPAREN', '(')
    ('NUMBER', '5')
    ('COMMA', ',')
    ('NUMBER', '3')
    ('RPAREN', ')')
    ('SEMICOLON', ';')
    ('ID', 'y')
    ('ASSIGN', '=')
    ('SUB', 'SUB')
    ('LPAREN', '(')
    ('NUMBER', '10')
    ('COMMA', ',')
    ('NUMBER', '2')
    ('RPAREN', ')')
    ('SEMICOLON', ';')
    ('ID', 'z')
    ('ASSIGN', '=')
    ('MUL', 'MUL')
    ('LPAREN', '(')
    ('NUMBER', '4')
    ('COMMA', ',')
    ('NUMBER', '5')
    ('RPAREN', ')')
    ('SEMICOLON', ';')
    ('ID', 'w')
    ('ASSIGN', '=')
    ('DIV', 'DIV')
    ('LPAREN', '(')
    ('NUMBER', '20')
    ('COMMA', ',')
    ('NUMBER', '4')
    ('RPAREN', ')')
    ('SEMICOLON', ';')
    ('ID', 'result')
    ('ASSIGN', '=')
    ('AVG', 'AVG')
    ('LPAREN', '(')
    ('NUMBER', '10')
    ('COMMA', ',')
    ('NUMBER', '20')
    ('RPAREN', ')')
    ('SEMICOLON', ';')

    <==== Abstract Parse Tree ====>

    ('ASSIGN', 'x', ('ADD', '5', '3'))
    ('ASSIGN', 'y', ('SUB', '10', '2'))
    ('ASSIGN', 'z', ('MUL', '4', '5'))
    ('ASSIGN', 'w', ('DIV', '20', '4'))
    ('ASSIGN', 'result', ('AVG', '10', '20'))

    <==== Intermediate Code ====>

    LOAD 5
    ADD 3
    STORE x
    LOAD 10
    SUB 2
    STORE y
    LOAD 4
    MUL 5
    STORE z
    LOAD 20
    DIV 4
    STORE w
    LOAD 10
    AVG 20
    STORE result


    ✅ Successfully compiled to test.o
    Execution complete. Final state:

    Registers: [10, 0, 0, 0, 0, 0, 0, 0]
    
    Memory: [8, 8, 20, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]... (first 16 bytes)
```
## Output Explanation
In the above output we can see the state of Registers and Memory after the execution is complete.
- The Registers part only has data in the first position i.e. the first Register , and every other register is empty.
  This is because the register only contains the output of current execution and hence after the completion of execution R1 would contain the output of last instruction. In this case that instruction is the MSQ(2 , 4) instruction and hence the register contains the output  (2*2 + 4*4)/2 which is 10.
- The Memory part has the values of the variables in the order that they were declared.
  So in this case ,
  x = 8
  y = 8
  z = 20
  w = 5
  result = 10

---
## One can also run objdump on the test.o file to disassemble the object file
```bash
    objdump -d test.o
```

---
## Need for simulation of a CPU.
A CPU has predefined instructions like `ADD`, `IMUL` etc. To implement a custom instruction like `MSQ` would mean one would have to add a particular component to perform the given instruction in the CPU.(for 5 marks?)<br>
Hence , we make , in layman's term , a fake CPU which only knows ADD, SUB, MUL ,DIV and MSQ to demonstrate exactly how does a compiler deals with instructions. 

---
## 🎓 Project Objective

This project was built for an academic assignment:

> Design a custom instruction for a given equation in a compiler.

It showcases a working frontend + backend compiler flow and integrates a custom-designed instruction.

---
