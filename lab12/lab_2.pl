Exercise 2.1

1. yes 

2. no

8. yes, X==bread

9. no

14. yes, but only if there exists some rule like food(bread) :- drink(beer)

Exercise 2.2

Running the queries, only magic(Hermione) appears to work, which surprises me since I would expected magic('McGonagall') to also work since she satisfies the witch(X) clause, but alas it appears not to be so...

magic(Hermione) yields Hermione=dobby

since magic(X):- house_elf(X)
and house_elf(dobby)

If we wanted to make it so that magic(Hermione) returns Hermione=hermione first and didn't crash upon trying to find a wizard, we could move the witch(X) definition above the house_elf in which case the magic(Hermione) query results in all the magic users: hermione, 'McGonagall', rita_skeeter, and dobby.

b. In propositional logic, I don't think we have this notion of unification, if for no other reason than that we don't have variables. If you accepted just the first half of the reading's definition of unification however, it would include that portion where 'a' == 'a' counts as a match.

c. I'm not certain since looking at the tracebacks of the errors prolog is trying, it appears to be looking at all possible routes that something could be true rather than symbolically simplifying complementary terms. I guess part of that might be simply that Prolog accepts more than just true/false values and likely won't always have complementary terms to work with. If it does use resolution, I suspect it would consider anything that it doesn't have information about to be false.



