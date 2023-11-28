mov sp, nil  ; 0
mov bp, 1    ; 1
mov r1, 5    ; 3
mov r2, 6    ; 5
mov r3, 7    ; 7
mov r4, 8    ; 9
LOOP:
cmp sp, 0x0F ; 11
jz END       ; 13
add r1, bp   ; 15
add r2, bp
add r3, bp
add r4, bp
add sp, 1
jmp LOOP
END:
jmp END
