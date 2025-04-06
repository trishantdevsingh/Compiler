import struct
import os

class Linker:
    @staticmethod
    def create_object_file(machine_code, output_file):
        """
        Creates a minimal ELF object file with:
        - ELF header
        - Single .text section
        - Provided machine code
        
        Args:
            machine_code (bytes): The compiled machine code to include
            output_file (str): Path to output file
        """
        # Constants
        ELFCLASS64 = 2        # 64-bit ELF
        ELFDATA2LSB = 1       # Little endian
        ET_REL = 1            # Relocatable file
        EM_X86_64 = 0x3e      # x86-64 architecture
        SHT_PROGBITS = 1      # Program bits section type
        SHF_ALLOC = 0x2       # Section should be allocated
        SHF_EXECINSTR = 0x4   # Section contains executable instructions

        # Calculate offsets and sizes
        elf_header_size = 64
        section_header_size = 64
        text_section_offset = elf_header_size + section_header_size  # .text starts after headers

        # ELF Header
        elf_header = (
            b'\x7fELF' +                     # Magic number
            struct.pack('B', ELFCLASS64) +   # 64-bit
            struct.pack('B', ELFDATA2LSB) +  # Little endian
            struct.pack('B', 1) +            # ELF version (1)
            b'\x00' +                        # OS ABI (System V)
            b'\x00' +                        # ABI version
            b'\x00'*7 +                      # Padding
            struct.pack('<H', ET_REL) +      # Relocatable file type
            struct.pack('<H', EM_X86_64) +   # x86-64 architecture
            struct.pack('<I', 1) +           # ELF version
            struct.pack('<Q', 0) +           # Entry point (0 for object files)
            struct.pack('<Q', 0) +           # Program header offset (none)
            struct.pack('<Q', elf_header_size) +  # Section header offset
            struct.pack('<I', 0) +           # Flags
            struct.pack('<H', elf_header_size) +  # ELF header size
            struct.pack('<H', 0) +           # Program header size (none)
            struct.pack('<H', 0) +           # Number of program headers
            struct.pack('<H', section_header_size) +  # Section header size
            struct.pack('<H', 1) +           # Number of section headers (just .text)
            struct.pack('<H', 0)             # Section header string table index (none)
        )

        # .text Section Header
        text_section_header = (
            struct.pack('<I', 0) +           # sh_name (0 since we have no string table)
            struct.pack('<I', SHT_PROGBITS) +  # sh_type (program bits)
            struct.pack('<Q', SHF_ALLOC | SHF_EXECINSTR) +  # sh_flags
            struct.pack('<Q', 0) +           # sh_addr (0 for object files)
            struct.pack('<Q', text_section_offset) +  # sh_offset
            struct.pack('<Q', len(machine_code)) +  # sh_size
            struct.pack('<I', 0) +           # sh_link
            struct.pack('<I', 0) +           # sh_info
            struct.pack('<Q', 16) +          # sh_addralign (16-byte alignment)
            struct.pack('<Q', 0)             # sh_entsize (0 since no fixed-size entries)
        )

        with open(output_file, 'wb') as f:
            # Write ELF header
            f.write(elf_header)
            
            # Write .text section header
            f.write(text_section_header)
            
            # Write machine code
            f.seek(text_section_offset)
            f.write(machine_code)

        # Set permissions
        os.chmod(output_file, 0o644)