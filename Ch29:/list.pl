mymember(I,[I|_]).
mymember(I,[_|T]):-
    mymember(I,T).

myappend([],X,X).
myappend([H|T],L,[H|R]):-
   myappend(T,L,R).

lastone([X],X).
lastone([_|T],R):-
   lastone(T,R).

lastbutone([X,_],X).
lastbutone([_|T],R):-
   lastbutone(T,R).

elementat([X|_],1,X).
elementat([_|T],N,R):-
   A is N-1,
   elementat(T,A,R).

len([],0).
len([_|T],L):-
  len(T,X),
  L is X+1.


