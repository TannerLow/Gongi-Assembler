comment = ";"

# any - any register or immediate
# reg - any register but no immediate
# dst - same as reg but also no nil or ip
# any|label - any or a label

operators = {
    "nop": [],
    "mov": ["dst", "any"],
    "add": ["dst", "any"],
    "sub": ["dst", "any"],
    "shl": ["dst", "any"],
    "shr": ["dst", "any"],
    "and": ["dst", "any"],
    "or" : ["dst", "any"],
    "xor": ["dst", "any"],
    "not": ["dst"],
    "cmp": ["reg", "any"],
    "jmp": ["any|label"],
    "jz" : ["any|label"],
    "jnz": ["any|label"],
    "lpd": ["any"],
}

operands = {
    "any": [
        "r1",
        "r2",
        "r3",
        "r4",
        "sp",
        "bp",
        "ptr",
        "nil",
        "ip",
        "mem",
        "pma",
        "ex1"
    ],
    "dst": [
        "r1",
        "r2",
        "r3",
        "r4",
        "sp",
        "bp",
        "ptr",
        "mem",
        "pma",
        "ex1"
    ]
}

opcodes = {
    "nop": "00000",
    "mov": "00001",
    "add": "00010",
    "sub": "00011",
    "shl": "00100",
    "shr": "00101",
    "and": "00110",
    "or" : "00111",
    "xor": "01000",
    "not": "01001",
    "cmp": "01010",
    "jmp": "01011",
    "jz" : "01100",
    "jnz": "01101",
    "lpd": "01110",
}



registerCodes = {
    "r1" : "0000",
    "r2" : "0001",
    "r3" : "0010",
    "r4" : "0011",
    "sp" : "0100", 
    "bp" : "0101",
    "ptr": "0110",
    "nil": "0111", 
    "ip" : "1000",
    "mem": "1001",
    "immediate": "1010",
    "pma": "1011",
    "ex1": "1100",
}