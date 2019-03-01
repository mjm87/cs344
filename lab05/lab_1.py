from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])


# Exercise 5.1


# a. The answer makes sense given that it can be taken straight off the chart
print("P(Alarm | burglary ^ !earthquake) => " +
      enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# b. This also matches the intuitive notion that P(J|B^!e) = P(J|A) * P(A|B^!e)
print("P(John | burglary ^ !earthquake) => " +
      enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# c. This makes sense given that this is the answer we got in class.
#    It also makes sense that it's pretty low thanks to the potential of the earthquake being about twice as likely
#    as a burglary.
print("P(Burglary | alarm) => " +
      enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

# d. This matches with the answer you showed in hand up top. It also makes sense that it is lower than the P(B | a),
#    because neither John or Mary have a reliable chance of reporting the alarm (90 and 70 respectively)
print("P(Burglary | john ^ mary) => " +
      enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())


