% the woman weighs the same as a duck
% ducks float just like wood floats
% wood burns just like witches burn
% the woman must be a witch

weighLikeADuck(woman).
floats(X):-weighLikeADuck(X).
burn(X):-floats(X).
witch(X):-burn(X).

% to test, query witch(woman). or witch(Y).
