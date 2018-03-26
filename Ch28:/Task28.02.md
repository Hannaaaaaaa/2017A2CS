      LDD A
      CMP #0
      JPN ELSE
THEN: STO B
      JMP ENDIF
ELSE: LDD B
      DEC ACC
      STO B
ENDIF:.....
