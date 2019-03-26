% Maggie von Ebers
% 525001114
% CSCE 420
% Due: March 31, 2019
% hw5pr1
    
solve_populations() :-
    % age
    fd_domain([A1, A2, A3, A4, A5, A6, A7], 1, 125),
    A4 #= 30,
    (A1, A2, A3, A4, A5, A6, A7) / 7 #= 38,
    % gender ( 1 = female )
    fd_domain_bool([G1, G2, G3, G4, G5, G6, G7]),
    G1 + G2 + G3 + G4 + G5 + G6 + G7 #= 4,
    ((G1 * A1) + (G2 * A2) + (G3 * A3) + (G4 * A4) + (G5 * A5) + (G6 * A6) + (G7 * A7))/(G1 + G2 + G3 + G4 + G5 + G6 + G7) #= 33,   % hm this is a double tho
    % race ( 1 = black )
    fd_domain_bool([R1, R2, R3, R4, R5, R6, R7]),
    R1 + R2 + R3 + R4 + R5 + R6 + R7 #= 4,
    ((R1 * A1) + (R2 * A2) + (R3 * A3) + (R4 * A4) + (R5 * A5) + (R6 * A6) + (R7 * A7))/(R1 + R2 + R3 + R4 + R5 + R6 + R7) #= 48,   % same here
    % relationship status
    fd_domain_bool([M1, M2, M3, M4, M5, M6, M7]),
    M1 + M2 + M3 + M4 + M5 + M6 + M7 #= 4,
    ((M1 * A1) + (M2 * A2) + (M3 * A3) + (M4 * A4) + (M5 * A5) + (M6 * A6) + (M7 * A7))/(M1 + M2 + M3 + M4 + M5 + M6 + M7) #= 54,
    % black women
    (R1 * G1) + (R2 * G2) + (R3 * G3) + (R4 * G4) + (R5 * G5) + (R6 * G6) + (R7 * G7) #= 3,


