% Maggie von Ebers
% 525001114
% CSCE 420
% Due: March 21, 2019
% hw4pr1.pl

my_sorted([]).
my_sorted([_]).
my_sorted([X,Y|Z]) :- 
    X =< Y, 
    my_sorted([Y|Z]).


my_quicksort([],[]).
my_quicksort([H|T],Sorted):-
	my_pivot(H,T,L1,L2),my_quicksort(L1,Sorted1),my_quicksort(L2,Sorted2),
	append(Sorted1,[H|Sorted2]).
   
my_pivot(H,[],[],[]).
my_pivot(H,[X|T],[X|L],G):-X=<H,my_pivot(H,T,L,G).
my_pivot(H,[X|T],L,[X|G]):-X>H,my_pivot(H,T,L,G).

my_perm_rec([H1|T1], [H2|T2]) :-
    H1 = H2,
    my_perm_rec(T1, T2).

my_perm(A, B) :-
    my_quicksort(A, Sorted1),
    my_quicksort(B, Sorted2),
    my_perm_rec(Sorted1, Sorted2).
