% Maggie von Ebers
% 525001114
% CSCE 420
% Due: March 21, 2019
% hw4pr4.pl

flatten([], []) :- !.
flatten([L|Ls], FlatL) :-
    !,
    flatten(L, NewL),
    flatten(Ls, NewLs),
    append(NewL, NewLs, FlatL).
flatten(L, [L]).

check_orders(Check, [[Head | Tail1] | Tail2]) :-
    not(Check = Head),
    check_orders(Check, Tail2).

my_topo_sort(Original, New) :-
    flatten(Original, X).
    my_topo(X, Original, New).

my_topo([Head | Tail], Original, New) :-
    