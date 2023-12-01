; Displays ASCII 32(Space) through 50(2) to the monitor
mov r1, 0x8000  ; address 0 in video memory
mov ex1, 0b001  ; setup ex1 to write char only
mov r2, 0
LOOP:
cmp r1, 0x8100  ; loop 256 times, 0 to 255
jz  END
mov ptr, r1
mov mem, r2     ; write char value in r2 to video memory
add r2, 1
add r1, 1
jmp LOOP
END:
jmp END
