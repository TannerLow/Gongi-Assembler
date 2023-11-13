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
        "pma"
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
        "pma"
    ]
}