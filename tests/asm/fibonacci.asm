; Calculates the first 15 fibonacci numbers
MOv ptr, nil ; 0 : ptr = 0
mov mem, 1   ; 1 : mem[ptr] = 1
add ptr, 1   ; 3 : ptr = ptr + 1
mov mem, 1   ; 5 : mem[ptr] = 1
mov r1, 2    ; 7 : r1 = 2
LOOP:
cmp r1, 0xF  ; 9 : if(r2 == 9)
jz  27       ; 11: goto instruction 27
mov ptr, r1  ; 13: ptr = r1
sub ptr, 1   ; 14: ptr = ptr - 1
mov r2, mem  ; 16: r2 = mem[ptr]
sub ptr, 1   ; 17: ptr = ptr - 1
mov r3, mem  ; 19: r3 = mem[ptr]
mov ptr, r1  ; 20: ptr = r1
add r2, r3   ; 21: r2 = r2 + r3
mov mem, r2  ; 22: mem[ptr] = r2
add r1, 1    ; 23: r1 = r1 + 1
jmp LOOP     ; 25: goto instruction 9
jmp 27       ; 27: halt