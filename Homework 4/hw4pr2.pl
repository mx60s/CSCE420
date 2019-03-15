% Maggie von Ebers
% 525001114
% CSCE 420
% Due: March 21, 2019
% hw4pr2.pl

% [a,s,r,p,c,s,r,b] -> example of loop

adjacent(a,t).
adjacent(a,s).
adjacent(a,z).
adjacent(s,o).
adjacent(s,f).
adjacent(s,r).
adjacent(o,a).
adjacent(f,b).
adjacent(r,p).
adjacent(p,b).

% path(P,Start,Goal) means list P is a path from Start to Goal

path([Goal], Goal, Goal).
path([X,Y],X,Y) :- adjacent(X,Y).
path([X,Y],X,Y) :- adjacent(Y,X).
path([Start|[Head|Tail]], Start, Goal) :- 
    adjacent(Start,Head),
	path([Head|Tail],Head,Goal).


% Finds an acyclic path between two points on the graph given.
path_find(A, A).

path_find(A, B) :-
    print(B),
    walk(A, B, []).

% Checks if we have already visited this node, and recursively completes the path.
walk(A, B, V) :-
    adjacent(A, X),
    not(member(X, V)),
    (B = X; walk(X, B, [A|V])),
    print(A).