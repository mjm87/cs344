from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])


# a1.
print("P(Raise | sunny) => " +
      enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())

# a2.
print("P(Raise | happy ^ sunny) => " +
      enumeration_ask('Raise', dict(Sunny=T, Happy=T), happiness).show_approx())

# b1.
print("P(Raise | happy) => " +
      enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())

# b2.
print("P(Raise | happy ^ !sunny) => " +
      enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())


# given how small the probability of having a raise in this domain is, I suppose
# it's not surprisingly though it's doubtlessly disappointing how low the probability
# of a raise is given happiness. Thankfully, knowing that it's not sunny out does
# increase our chances since we're removing a potential explanatory factor of happiness
# however, even given the 5-6x increase in probability of a raise, it's still under 10%
# presumably thanks to the abominably low percentage of getting a raise.
# Is it not sad to anyone else that in these worlds you are about as likely to get
# cancer as you are to have a burglary as you are to have a raise?
