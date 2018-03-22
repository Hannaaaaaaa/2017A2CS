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
parent(brandon,ed).



ancestor(A,B):-parent(A,B).
ancestor(A,B):-parent(A,X),ancestor(X,B).

