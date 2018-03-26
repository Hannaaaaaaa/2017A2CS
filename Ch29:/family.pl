male(jon).
male(bran).
male(ed).
male(robb).

female(sansa).
female(arya).
female(cat).
female(lyanna).

parent(lyanna,jon).
parent(ed,bran).
parent(ed,robb).
parent(ed,sansa).
parent(ed,arya).

parent(cat,sansa).
parent(cat,arya).
parent(cat,bran).
parent(cat,robb).



sibling(X,Y) :- parent(D,X), parent(D,Y),not(X=Y).
brother(X,Y) :- parent(D,X), parent(D,Y),male(X),not(X=Y).
sister(X,Y) :- parent(D,X), parent(D,Y),female(X),not(X=Y).
daughter(X,Y) :- parent(Y,X),female(X).
son(X,Y) :- parent(Y,X), male(X).
married(X,Y) :- parent(X,S),parent(Y,S),not(X=Y)
ancestor(X,Y) :- parent(A,B).
ancestor(X,Y) :- parent(X,A),ancestor(Y,A)



    


