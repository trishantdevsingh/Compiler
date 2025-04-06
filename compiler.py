from lexer import Lexer
from parser import Parser
from codegen import CodeGenerator
from assembler import Assembler
from emulator import CPUEmulator
from linker import Linker
import sys

def compile_and_run(input_file , output_file):
    with open(input_file, 'r') as f:
        source_code = f.read()
    
    # Lexical analysis
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    print("\n============= Tokenisation ===============")
    print(" ")
    for item in tokens:
        print(item)
    print(" ")
    parser = Parser(tokens)
    ast = parser.parse()
    print("\n============= Abstract Syntax Tree =============")
    print(" ")
    for item in ast:
        print(item)
    print(" ")
    # Code generation
    codegen = CodeGenerator(ast)
    intermediate_code = codegen.generate()
    print("\n============= Intermediate Code =============")
    for item in intermediate_code:
        print(item)
    print(" ")
    # Assembly
    assembler = Assembler(intermediate_code)
    machine_code = assembler.assemble()

    Linker.create_object_file(machine_code, output_file)
    print(f"Successfully compiled to {output_file}")
    print(" ")

    cpu = CPUEmulator(machine_code)
    cpu.run()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compiler.py <input.math> <output>")
        sys.exit(1)
    
    compile_and_run(sys.argv[1], sys.argv[2])