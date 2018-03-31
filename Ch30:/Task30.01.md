1. 
| Type of test data |Example|Explanation|Expected output|
|---|---|---|---|
|Valid|7|7 is the secert number|Congratulation|
|Valid|56|The range is 1-100, 56 is within the range|Continue guessing|
|Abnormal|@|Not number|Wrong|
|Abnormal|-1|Not positive number|Wrong|
|Abnormal|1023|Out of the range|Wrong|
|Boundary|100|At the boundary of the range|Continue Guessing|
|Boundary|101|At the boundary out of the range|Wrong|
2. 
|Type of test data|Example|Explanation|Expected Output|
|---|---|---|---|
|Normal|6| There are 7 columns| token appears at correct position |
|Normal|1|4 same tokens in the same column| Win|
|Boundary|3|Already has 5 tokens in the same column|Fill the column|
|Boundary|4|The last free place in the board|Fill the last place, and output result(win or draw)|
|Abnormal|0|No coulmn numbered 0|Wrong|
|Abnormal|2|The column is already full|Wrong|

