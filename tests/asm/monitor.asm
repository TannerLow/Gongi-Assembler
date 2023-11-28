; Displays ASCII 32(Space) through 50(2) to the monitor
mov r1, 0xC000  ; address 0 in video memory
mov ex1, 0b001  ; setup ex1 to write char only
mov r2, 32
LOOP:
cmp r1, 0xC013  ; loop 19 times, 32 to 50
jz  END
mov ptr, r1
mov mem, r2     ; write char value 32 to video memory
add r2, 1
add r1, 1
jmp LOOP
END:
jmp END
