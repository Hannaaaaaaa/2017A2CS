Label        Opcode         Operand           Explanation
             LDD            STACKBASE         
             STO            POINTER           Pointer point to the first location on stack
ADD:         IN                               Input character
             CMP            #13               check end of line character
             JPE            REMOVE            If true, go to loop2
             STI            POINTER           store the character in the memory location pointed by the pointer
             LDD            POINTER          
             INC            ACC               
             STO            POINTER           update pointer
             JMP            ADD
REMOVE:      LDD            POINTER
             CMP            STACKBASE         check stack empty?
             JPE            ENDLOOP
             LDI            POINTER           Load contents from the top of the stack
             OUT                              output the contents
             LDD            POINTER
             DEC            ACC
             STO            POINTER
             JMP            REMOVE
ENDLOOP:     END

STACKBASE:   STACK                            address of the beginning of stack
POINTER:                                      point to the next free location of stack
STACK:       ''                               start of the memory location reserved for stack

