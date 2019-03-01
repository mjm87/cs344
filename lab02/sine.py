"""
This module implements local search on a simple sine function variant.
The function has multiple local maximums and ever increasing as x -> infinity
(see the abs function variant in graphs.py).
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class SineVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """
    
    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta
        
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        return abs(x * math.sin(x))


if __name__ == '__main__':

    maximum = 30
    iterations = 1000

    overall_hill_solution = 0
    overall_sim_annealing_solution = 0

    avg_hill_soln = 0
    avg_anneal_soln = 0

    # random restarts
    for i in range(1,iterations):

        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=1.0)
        # print('Initial                      x: ' + str(p.initial)
        #      + '\t\tvalue: ' + str(p.value(initial))
        #     )

        # Solve the problem using hill-climbing.
        hill_solution = hill_climbing(p)

        # Solve the problem using simulated annealing.
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )

        # Save off best solutions : hill-climbing
        if(hill_solution > overall_hill_solution):
            overall_hill_solution = hill_solution

        # Save off best solutions : simulated annealing
        if(annealing_solution > overall_sim_annealing_solution):
            overall_sim_annealing_solution = annealing_solution

        # keep track of averages
        avg_hill_soln += hill_solution
        avg_anneal_soln += annealing_solution

    # iteration display
    print('Iterations: ' + str(iterations));

    # printing off the results - hill-climbing
    print('Hill-climbing solution       x: ' + str(overall_hill_solution)
          + '\tvalue: ' + str(p.value(overall_hill_solution))
          + '\tavg: ' + str(avg_hill_soln / iterations)
          )

    # printing off the results - simulated annealing
    print('Simulated annealing solution x: ' + str(overall_sim_annealing_solution)
          + '\tvalue: ' + str(p.value(overall_sim_annealing_solution))
          + '\tavg: ' + str(avg_anneal_soln / iterations)
          )
