; Known bugs:
;   Backspacing from beginning of line doesn't reset col

; Typing letters and numbers will display them to the screen
; backspace removes the last character
; enter moves cursor to the next line

; constants
mov ex1, 0b001 ; only write character data to screen, don't change colors
mov bp, 32636  ; main memory contains scancode to ascii DAT starting at this address

; initial setup
mov sp, nil    ; sp will hold the screen cursor position
mov r3, nil    ; cursor row
mov r4, nil    ; cursor col

MAIN_LOOP:
    ; poll for keyboard input
    mov ptr, 0xC000 ; location of keyboard keycode to read
    mov r1, mem     ; store keycode in r1, keycode is FF if invalid
    cmp r1, 0xFF    ; repoll if keycode is invalid
    jz MAIN_LOOP

    ; skip release events and extended scancodes
    mov r2, r1
    and r2, 0x0300  ; extract release and extended scan bits
    cmp r2, nil     ; if event is a release or extended code then ignore
    jnz MAIN_LOOP

    ; Handle Enter key as a newline
    cmp r1, 0x5A         ; if key is Enter then treat as newline char
    jnz HANDLE_BACKSPACE
    add r3, 1            ; increment row
    mov r4, r3           ; recalculate cursor position, temporarily clobber col register
    shl r4, 6            ; r4 = row * 64
    mov sp, r3
    shl sp, 4            ; sp = row * 16
    add sp, r4           ; sp = r4 + sp, (in other words sp = row * 80)
    mov r4, nil          ; reset col
    jmp MAIN_LOOP
    
    HANDLE_BACKSPACE:
    cmp r1, 0x66            ; if key is backspace then delete last character
    jnz DRAW_CHAR_TO_SCREEN
    sub sp, 1               ; adjust cursor
    cmp r4, nil             ; handle edge case where col is 0
    jnz NO_EDGE_CASE
    mov r4, 80              ; later it will subtract 1 to become 79
    cmp r3, nil             ; handle edge case where row is 0
    jz NO_EDGE_CASE
    sub r3, 1
    NO_EDGE_CASE:
    sub r4, 1
    ; draw whitespace at cursor to override whatever is currently there
    mov ptr, 0x8000         ; memory address of video memory
    add ptr, sp             ; offset to cursor position
    mov mem, 0x20           ; write character to video memory
    jmp MAIN_LOOP

    DRAW_CHAR_TO_SCREEN:
    mov ptr, bp     ; go to scancode to ascii DAT 
    add ptr, r1     ; offset index based on current scancode
    mov r2, mem     ; get ascii value
    mov ptr, 0x8000 ; memory address of video memory
    add ptr, sp     ; offset to cursor position
    mov mem, r2     ; write character to video memory
    
    add sp, 1       ; progress cursor
    add r4, 1       ; increment col

    cmp r4, 80      ; if col reaches 80 then update row and reset
    jnz MAIN_LOOP
    add r3, 1       ; increment row
    mov r4, nil     ; reset col

    jmp MAIN_LOOP

END:
    jmp END