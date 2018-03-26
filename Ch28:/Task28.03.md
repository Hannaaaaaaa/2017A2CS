     LDM #1
     STO Number
     LDM #0
     STO Total
     LDM #5
     STO Max
LOOP:LDD Total
     ADD Number
     STO Total
     LDD Number
     INC ACC
     STO Number 
UNTIL:CMP Max
      JPN LOOP
ENDLOOP:......