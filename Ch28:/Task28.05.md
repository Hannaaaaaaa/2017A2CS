     LDM #0
     STO Count
     LDM #78
     STO Letter
LOOP:LDD Count
     INC ACC
     STO Count
     IN
     CMP Letter
     JPN LOOP
ENDLOOP:LDM #48
        ADD Count
        OUT
