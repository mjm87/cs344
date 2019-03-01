from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])

# a.
print("P(Cancer | Test1 ^ Test2) => " +
      enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# b.
print("P(Cancer | Test1 ^ !Test2) => " +
      enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

# While the results don't necessarily make intuitive sense until you consider how low the probability of cancer
# is, I've seen these sorts of problems since high-school so I'm more concerned about how large 0.17 is rather
# than how low it is.)

# One failed test drastically reduces the chance that you have cancer.
