Exercise 3.2: Russian Dolls

	Knowledge Base

	directlyIn(olga, katarina).
	directlyIn(natasha, olga).
	directlyIn(irina, natasha).

	in(X,Y):- directlyIn(X,Y).
	in(X,Y):- 
			directlyIn(X,Z),
			in(Z,Y).

Exercise 4.5: 

	Knowledge Base

	% german to english
	tran(eins, one).
	tran(zwei, two).
	tran(drei, three).
	tran(vier, four).
	tran(fuenf, five).
	tran(sechs, six).
	tran(sieben, seven).
	tran(acht, eight).
	tran(neun, nine).

	% recursively translate lists of numbers
	% between german and english or vice versa
	listtran([], []).
	listtran([Yh|Yt], [Xh|Xt]):-
		tran(Yh,Xh),
		listtran(Yt,Xt).

Modus Ponens in prolog
	
	Yes, Prolog implements a generalized modus ponens with variables and instantiation.
	As an example, here's the classic Socrates example:

	human(socrates).
	mortal(X):- human(X).
	% mortal(S). --> S=socrates
