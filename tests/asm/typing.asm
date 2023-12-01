; Anything the user types will appear on screen

; initialize a keymap in memory to all 0's (not pressed)
mov ptr, nil
mov r1, 131
INITIAL_1:
    cmp ptr, r1
    jz INITIAL_2
    mov mem, nil
    add ptr, 1
    jmp INITIAL_1

; store all the keys scancodes for polling them later
; [0-130] key states
; [131+]  scan codes
; [331+]  ASCII values
; r2 stores max scan code address + 1
; key codes (some are overriden to be lower values) 
; https://docs.google.com/document/d/1w--ouGvSSf93tFltmBcSRGMN8Rte7ayalQZRDPG0ezk/edit
INITIAL_2:
    mov r4, 1
    mov r2, 131
    mov r3, 200
    mov ptr, r2
    ; r2 will store max address
    mov mem, 0x16 ; 1
    add ptr, r3
    mov mem, 49 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x1E ; 2
    add ptr, r3
    mov mem, 50 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x26 ; 3
    add ptr, r3
    mov mem, 51 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x25 ; 4
    add ptr, r3
    mov mem, 52 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x2E ; 5
    add ptr, r3
    mov mem, 53 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x36 ; 6
    add ptr, r3
    mov mem, 54 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x3D ; 7
    add ptr, r3
    mov mem, 55 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x3E ; 8
    add ptr, r3
    mov mem, 56 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x46 ; 9
    add ptr, r3
    mov mem, 57 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x45 ; 0
    add ptr, r3
    mov mem, 48 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x66 ; Backspace
    add ptr, r4
    mov r2, ptr
    mov mem, 0x15 ; Q
    add ptr, r3
    mov mem, 113 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x1D ; W
    add ptr, r3
    mov mem, 119 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x24 ; E
    add ptr, r3
    mov mem, 101 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x2D ; R
    add ptr, r3
    mov mem, 114 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x2C ; T
    add ptr, r3
    mov mem, 116 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x35 ; Y
    add ptr, r3
    mov mem, 121 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x3C ; U
    add ptr, r3
    mov mem, 117 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x43 ; I
    add ptr, r3
    mov mem, 105 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x44 ; O
    add ptr, r3
    mov mem, 111 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x4D ; P
    add ptr, r3
    mov mem, 112 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x1C ; A
    add ptr, r3
    mov mem, 97 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x1B ; S
    add ptr, r3
    mov mem, 115 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x23 ; D
    add ptr, r3
    mov mem, 100 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x2B ; F
    add ptr, r3
    mov mem, 102 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x34 ; G
    add ptr, r3
    mov mem, 103 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x33 ; H
    add ptr, r3
    mov mem, 104 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x3B ; J
    add ptr, r3
    mov mem, 106 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x42 ; K
    add ptr, r3
    mov mem, 107 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x4B ; L
    add ptr, r3
    mov mem, 108 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x1A ; Z
    add ptr, r3
    mov mem, 122 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x22 ; X
    add ptr, r3
    mov mem, 120 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x21 ; C
    add ptr, r3
    mov mem, 99 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x2A ; V
    add ptr, r3
    mov mem, 118 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x32 ; B
    add ptr, r3
    mov mem, 98 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x31 ; N
    add ptr, r3
    mov mem, 110 ; ASCII value
    sub ptr, r3
    add ptr, r4
    mov r2, ptr
    mov mem, 0x3A ; M
    add ptr, r3
    mov mem, 109 ; ASCII value
    sub ptr, r3
    mov r2, ptr
    add r2, r4

mov bp, r1
mov ptr, bp
mov ex1, 0b001
mov sp, nil
; register allocations
; bp - start of scan codes index, constant
; r1 - current scan code
; r2 - end of scan code indexes, constant
; r3 - temporary ptr storage
; r4 - key state of current scan code
; sp - screen cursor location
; ex1 - constant
MAIN_LOOP:
    cmp ptr, r2 ; has ptr reached end of scan codes
    jz RESET_PTR
    mov r1, mem ; get scan code

    ; save scan code index ptr for later
    mov r3, ptr
    mov ptr, 0x0FFF
    mov mem, r3 ; we can now clobber r3
    mov ptr, mem

    or  ptr, 0xC000 ; setup ptr to poll key state of current scan code
    mov r4, mem ; get key state of current scan code
    and ptr, 0x00FF ; change back to just scan code
    mov ptr, mem
;    mov r3, ptr ; save scan code for later
    cmp mem, r4 ; check if key state has changed
    jz BREAK
    ; else

    ; key state has changed, if its now pressed then write key to screen
    cmp r4, 1
    jnz UPDATE_KEYSTATE ; key state shows key was released
    ; else

    ; key state shows key is now being pressed so write char to screen
    ; if key is Backspace then remove last key instead
    cmp ptr, 0x66
    jz HANDLE_BACKSPACE
    ; else

    ; write char to screen
    ; get scan code index and add 200 to get ASCII value
    mov ptr, 0x0FFF
    mov ptr, mem
    add ptr, 200
    mov r3, mem ; r3 now has ASCII value
    mov ptr, sp
    or  ptr, 0x8000 ; translate address to video memory address
    mov mem, r3 ; write char to video memory at cursor location

    jmp UPDATE_KEYSTATE
    HANDLE_BACKSPACE:
    ; if cursor at pos 0, do nothing
    cmp sp, nil
    jz UPDATE_KEYSTATE
    ; else

    ; go back a space and write a space char
    sub sp, 1
    mov ptr, sp
    or  ptr, 0x8000
    mov mem, 0x32

    UPDATE_KEYSTATE:
    ; retrieve scan code and write key state to mem[scan code]
    mov ptr, 0x0FFF
    mov ptr, mem
    mov mem, r4
    BREAK:
    ; retrieve previously stored scan code index
    mov ptr, 0x0FFF
    mov ptr, mem

    add ptr, 1
    jmp MAIN_LOOP

RESET_PTR:
    mov ptr, bp
    jmp MAIN_LOOP

END:
    jmp END