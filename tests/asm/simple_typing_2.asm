; pressing A on the keybaord will write an 'a' to the screen
mov ex1, 0b001  ; write char to video mem, not colors 
mov r2, 0xFF    ; invalid key data
mov bp, 97      ; ascii value for 'a'

mov ptr, 0xC000 ; keyboard mem location
mov sp, nil     ; cursor position

LOOP:
    mov r1, mem ; get key data

    cmp r1, r2  ; check if key data is valid
    jz  LOOP

    mov r4, r1
    and r4, 0x0200 ; extract the release bit from key data
    cmp r4, nil    ; if release bit then skip drawing and update r3
    jz  DRAW_TO_SCREEN
    jmp LOOP

    DRAW_TO_SCREEN:
    cmp r1, 0x1C    ; if not A then skip
    jnz LOOP
    mov r1, bp      ; convert scan code to ascii value
    mov ptr, 0x8000 ; video mem location
    or  ptr, sp     ; offset with cursor location
    mov mem, r1     ; draw char to screen
    add sp, 1
    mov ptr, 0xC000 ; reset ptr back to keyboard mem location
    jmp LOOP

END:
    jmp END