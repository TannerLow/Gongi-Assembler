; pressing A on the keybaord will write an 'a' to the screen
mov ex1, 0b001

mov r4, 0x1C  ; r4 = scancode
mov r2, 97    ; r2 = ascii value
mov r3, nil   ; r3 = keystate

mov sp, nil
LOOP:
    mov ptr, r4
    or  ptr, 0xC000
    mov bp, mem
    ; bp now has current keystate
    cmp r3, bp
    jz LOOP
    mov r3, bp
    cmp bp, 1
    jnz LOOP
    mov ptr, sp
    or  ptr, 0x8000
    mov mem, r2
    add sp, 1
    jmp LOOP

END:
    jmp END