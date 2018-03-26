factorial(1,1).
factorial(N,F) :- 
   M is N-1,
   factorial(M,X),
   F is N*X.

bunnyEars(0,0).
bunnyEars(N,X):-
   M is N-1,
   bunnyEars(M,Q),
   X is Q+2.

fibonacci(0,0).
fibonacci(1,1).
fibonacci(N,X):-
   M is N-1,
   fibonacci(M,Q),
   W is M-1,
   fibonacci(W,E),
   X is Q+E.

bunnyEars2(0,0).
bunnyEars2(A,B):-
C is A-1,
bunnyEars2(C,D),
E is mod(A,2),
(E==1->
B is D+2;
B is D+3).
   

triangle(0,0).
triangle(A,B) :-
   C is A-1,
   triangle(C,D),
   B is A+D.

sumdigit(0,0).
sumdigit(A,B):-
   C is A//10,
   sumdigit(C,D),
   E is mod(A,10),
   B is E+D.

count7(0,0).
count7(A,B):-
C is A//10,
count7(C,D),
E is mod(A,10),
( E==7 ->
     B is 1+D;
B is D).




   
    



   





