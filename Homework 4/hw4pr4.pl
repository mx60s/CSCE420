% Maggie von Ebers
% 525001114
% CSCE 420
% Due: March 21, 2019
% hw4pr4.pl

% flatten the list of lists into one list
flatten([], []) :- !.
flatten([L|Ls], FlatL) :-
    !,
    flatten(L, NewL),
    flatten(Ls, NewLs),
    append(NewL, NewLs, FlatL).
flatten(L, [L]).

% make sure we cannot prove that our candidate for max is lesser
% than any other number in the bunch
check_orders(Check, [[Head | Tail1] | Tail2]) :-
    not(Check = Head),
    check_orders(Check, Tail2).

my_topo_sort(Original, New) :-
    flatten(Original, X).
    my_topo(X, Original, New).

my_topo([Head | Tail], Original, New) :-
    (
        check_orders(Head, Original), 
        
        ) ;
    (not(check_orders()))