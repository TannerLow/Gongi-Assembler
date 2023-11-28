; Test for alu adder
mov r1, 0x00FF
mov r2, 0xFFF0
add r1, r2
mov r3, 0x00F0
mov r4, 0x0FFF
sub r4, r3
END:
jmp END