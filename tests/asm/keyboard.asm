; This program will try to get the status of the F key
; once F is pressed, the program will halt
mov ptr, 0xC02B ; 0, 2B is scancode for F 
GET_F_KEY:
mov r1, mem     ; 2
cmp r1, 1       ; 3
jz END          ; 4
jmp GET_A_KEY   ; 6
END:
jmp END         ; 8
