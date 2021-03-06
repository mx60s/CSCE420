% Maggie von Ebers
% 525001114
% CSCE 420
% Due: March 21, 2019
% hw4pr3.pl

% It was just easier to define both parents...sorry!!

parent(king_george, elizabeth).
parent(king_george, margaret).
parent(elizabeth, diana).
parent(elizabeth, anne).
parent(elizabeth, andrew).
parent(elizabeth, edward).
parent(diana, william).
parent(diana, harry).
parent(anne, peter).
parent(anne, zara).
parent(andrew, beatrice).
parent(andrew, eugenie).
parent(edward, louise).
parent(edward, james).
parent(william, prince_george).
parent(william, charlotte).
parent(william, louis).
parent(harry, meghans_baby).
parent(zara, mia).
parent(peter, savannah).
parent(peter, isla).

parent(mum, elizabeth).
parent(mum, margaret).
parent(philip, diana).
parent(philip, anne).
parent(philip, andrew).
parent(philip, edward).
parent(charles, william).
parent(charles, harry).
parent(mark, peter).
parent(mark, zara).
parent(sarah, beatrice).
parent(sarah, eugenie).
parent(sophie, louise).
parent(sophie, james).
parent(catherine, prince_george).
parent(catherine, charlotte).
parent(catherine, louis).
parent(meghan, meghans_baby).
parent(mike, mia).
parent(autumn, savannah).
parent(isla, savannah).


female(mum).
female(elizabeth).
female(margaret).
female(diana).
female(anne).
female(sarah).
female(sophie).
female(zara).
female(beatrice).
female(eugenie).
female(louise).
female(meghan).
female(catherine).

child(A, B) :-
    parent(B, A).

grandchild(A, B) :-
    parent(B, X),
    parent(X, Y),
    A = Y.

greatgrandchild(A, B) :-
    grandchild(X, B),
    parent(X, Y),
    A = Y.

grandparent(A, B) :-
    grandchild(B,A).

greatgrandparent(A, B) :-
    greatgrandchild(B, A).

ancestor(A, B) :- 
    (parent(C, B), A = C) ;
    (grandparent(D, B), A = D) ;
    (greatgrandparent(E, B), A = E).

mother(A, B) :-
    parent(X, B),
    A = X,
    female(X).

father(A, B) :-
    parent(X, B),
    A = X,
    not(female(X)).

sister(A, B) :-
    parent(X, B),
    parent(X, Y),
    female(X),
    female(Y),
    not(Y = B),
    A = Y.

brother(A, B) :-
    parent(X, B),
    parent(X, Y),
    female(X),
    not(female(Y)),
    not(Y = B),
    A = Y.

sibling(A, B) :-
    (brother(X, B), A = X) ;
    (sister(Y, B), A = Y).

aunt(A, B) :-
    parent(X, B),
    sister(Y, X),
    A = Y.

uncle(A, B) :-
    parent(X, B),
    brother(Y, X),
    A = Y.

firstcousin(A, B) :-
    parent(X, B),
    (sister(Y, X) ; brother(Y, X)),
    parent(Y, Z),
    A = Z.

brotherinlaw(A, B) :-
    (sister(X, B) ; brother(X, B)),
    parent(X, Y),
    parent(Z, Y),
    not(female(Z)),
    A = Z.

secondcousin(A, B) :-
    firstcousin(X, B),
    parent(X, Y),
    A = Y.

