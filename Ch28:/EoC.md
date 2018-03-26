# Chapter 28
## End OF Chapter
### Hanna Gao

1. a. 
If the bit in the register and the bit in operand with same position as register are both 1, then puts 1 in that position, otherwise is 0.
b.
AND #B00001111
c.

|        label        |Opcode                          |Operand                         
|----------------|-------------------------------|-----------------------------|
||IN||
||AND|Mask|
||LSL|#4|
||STO|Result|
||IN||
||AND|Mask|
||OR|Result|
||STO|Result|
||END
|Mask:| &0F|

3. 
| Label | Opcode | Operand |
|--|--|--|
|| LDR| #0|
|LOOP:|IN||
||STI|STRING|
||INC|IX|
||CMP|#33|
||JPN|LOOP
||END||