% Maggie von Ebers
% 525001114
% CSCE 420
% Due: March 31, 2019
% hw5pr1
    
solve_populations(_) :-
    % age
    fd_domain([A1, A2, A3, A4, A5, A6, A7], 1, 125),
    A4 #= 30,
    (A1 + A2 + A3 + A4 + A5 + A6 + A7) / 7 #= 38,
    median([A1, A2, A3, A4, A5, A6, A7], X),
    X #= 30,
    fd_atmost(2, [A1, A2, A3, A4, A5, A6, A7], 5),  % need it to be "at most 2 people are less than 5"
    % gender ( 1 = female )
    fd_domain_bool([G1, G2, G3, G4, G5, G6, G7]),
    fd_cardinality([G1, G2, G3, G4, G5, G6, G7], 4),
    ((G1 * A1) + (G2 * A2) + (G3 * A3) + (G4 * A4) + (G5 * A5) + (G6 * A6) + (G7 * A7)) #= 134,
    % median([(G1 * A1), (G2 * A2), (G3 * A3), (G4 * A4), (G5 * A5), (G6 * A6), (G7 * A7)], FMedian),
    % FMedian #= 30,
    % race ( 1 = black )
    fd_domain_bool([R1, R2, R3, R4, R5, R6, R7]),
    fd_cardinality([R1, R2, R3, R4, R5, R6, R7], 4),
    ((R1 * A1) + (R2 * A2) + (R3 * A3) + (R4 * A4) + (R5 * A5) + (R6 * A6) + (R7 * A7)) #= 194,
    ((R1 * G1 * A1) + (R2 * G2 * A2) + (R3 * G3 * A3) + (R4 * G4 * A4) + (R5 * G5 * A5) + (R6 * G6 * A6) + (R7 * G7 * A7)) #= 110,
    %median([(R1 * A1), (R2 * A2), (R3 * A3), (R4 * A4), (R5 * A5), (R6 * A6), (R7 * A7)], BMedian),
    %BMedian #= 51,
    % relationship status ( 1 = married )
    fd_domain_bool([M1, M2, M3, M4, M5, M6, M7]),
    fd_cardinality([M1, M2, M3, M4, M5, M6, M7], 4),
    ((M1 * A1) + (M2 * A2) + (M3 * A3) + (M4 * A4) + (M5 * A5) + (M6 * A6) + (M7 * A7))/(M1 + M2 + M3 + M4 + M5 + M6 + M7) #= 54,
    % black women
    (R1 * G1) + (R2 * G2) + (R3 * G3) + (R4 * G4) + (R5 * G5) + (R6 * G6) + (R7 * G7) #= 3,
    (A1 #< 15) #==> (M1 #= 0),
    fd_labeling([A1, A2, A3, A4, A5, A6, A7]),
    fd_labeling([G1, G2, G3, G4, G5, G6, G7]),
    fd_labeling([R1, R2, R3, R4, R5, R6, R7]),
    fd_labeling([M1, M2, M3, M4, M5, M6, M7]),
    marriage(M1, CM1),
    write(CM1),
    write([A1, G1, R1, M1]),
    write([A2, G2, R2, M2]),
    write([A3, G3, R3, M3]),
    write([A4, G4, R4, M4]),
    write([A5, G5, R5, M5]),
    write([A6, G6, R6, M6]),
    write([A7, G7, R7, M7]).


median(List, Median) :-
    msort(List, SortedList),
    middle_element(SortedList, SortedList, Median).

middle_element([], [M|_], M).
middle_element([_], [M|_], M).
middle_element([_,_|Xs], [_|Ys], M) :-
    middle_element(Xs, Ys, M).

marriage("M", X) :-
    X = 1.
marriage("S", X) :-
    X = 0.
