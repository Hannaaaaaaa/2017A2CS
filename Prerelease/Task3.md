# Task3
3.1
character(habib)
character_type(habib,explorer).
pet(habib,fish).
skill(timetravel).
has_skill(habib,timetravel).

3.2
pet(X,Y):-character(X),animal(Y).

3.3
character(noah).
character_type(noah,king).
animal(lion).
skill(seer).
pet(noah,lion).

3.4
true
X=princess
X=jim
X=invisibility
X=jim

3.5
pet(jim,X).
skill(X,fly).
skill(X).
petofprincess(X):-pet(A,B),character_type(A,princess),X is B.
 






