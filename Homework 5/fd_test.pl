
solve_test(L, D) :-
    fd_domain(L, D),
    fd_all_different(L),
    fd_labeling(L).

