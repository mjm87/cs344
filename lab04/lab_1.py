'''
Exercise 4.1


'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())


# Exercise 4.1b
# P(Cavity|catch) = P(Cavity^catch) / P(catch) = (0.108 + 0.072) / (0.108 + 0.072 + 0.016 + 0.144) = 0.529...
p_cavity_given_catch = (0.108 + 0.072) / (0.108 + 0.072 + 0.016 + 0.144)
print(p_cavity_given_catch)
PCC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PCC.show_approx())

# Exercise 4.1c
# coins
P = JointProbDist(['coin_1', 'coin_2'])
H, T = True, False
P[H, H] = 0.25
P[H, T] = 0.25
P[T, H] = 0.25
P[T, T] = 0.25

PHH = enumerate_joint_ask('coin_2', {'coin_1': H}, P)
print(PHH.show_approx())
# yes. If I hadn't found a 50-50 shot for the second coin to be heads, I would have had to conclude
# that either I had created the wrong distribution or that separate coin tosses weren't independent.


# It's not a terrible approach I suppose for these trivial examples, but I can definitely see it growing in
# pain as we scale up with more and more variables and when we're interested in more interesting questions
