1.3 Exercises

	1.1

	vINCENT -- atom
	Footmassage -- variable
	variable23 -- atom
	Variable2000 -- variable
	big_kahuna_burger -- atom
	'big kahuna burger' -- atom
	big kahuna burger -- neither
	'Jules' -- atom
	_Jules -- variable
	'_Jules' -- atom

	1.2

	loves(Vincent,mia) -- complex term
	'loves(Vincent,mia)' -- atom
	Butch(boxer) -- neither
	boxer(Butch) -- complex term
	and(big(burger),kahuna(burger)) -- complex term
	and(big(X),kahuna(X)) -- complex term
	_and(big(X),kahuna(X)) -- neither
	(Butch  kills  Vincent) -- neither
	kills(Butch  Vincent) -- neither
	kills(Butch,Vincent -- neither

	1.3

	facts: 3
	rules: 4
	clauses: 0
	predicates: 0

	if X is a man or X  is a woman, X is a person
	if X and Y have a father relationship, X and Y have a love relationship
	if Y is a man and Z and Y have a son relationship, there is a father relationship between Y and Z
	if Y is a man and Z and Y have a daughter relationship, thie is a father relationship between Y and Z

	1.4

	killer(butch)    // butch is a killer
	married(mia, marsellus)  // mia and marsellus are married
	dead(zed)    // zed is dead
	kill(marsellus, X):- footmassage(mia, X)  // marsellus will kill anyone who gives mia a footmassage
	love(mia, X):- goodDancer(X)  // mia will love anyone who is a good dancer
	eats(jules, X):- nutritious(X) ; tasty(X)  // jules will eat anything that is either nutriious or tasty



	1.5

	1. yes: it's in the knowledge base
	2. no: there is no definition for witch to work with
	3. no: there is no definiton for hermione
	4. no: ditto
	5. yes: harry is a quidditchPlayer and thus has a broom, he also has a wand which qualifies him as a wizard
	6. ron: Prolog returns a valid wizard, since ron is explicitly mentioned I suspect he would come first before harry who would need to have been queried with another ;
	7. no: still no definition for what a witch is...


b. No, it can do modus ponens from rules that we provide it using the :- operator, but doesn't explicitly appear to do so through propositional logic. However, if you wanted to create it, I would attempt to build a query out of the AND operator , and the implication operator :- to replicate the propositional approach.

c. It appears that Prolog's horn-clauses are powerful enough to express most of propositional logic sort of things, however, Prolog comes with support for variables which is lacking in propositional logic.

d. From my understanding of the syntax, TELL and ASK are the same in Prolog. I suppose so that you don't have to learn multiple different syntaxes when one would do. 
	
	happy(julie)
	dances(X) :- happy(X)
