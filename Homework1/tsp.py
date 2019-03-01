from search import Problem, hill_climbing, simulated_annealing, exp_schedule
import random


class TSP(Problem):

    # constructor
    def __init__(self, initial, distances, n=10):
        self.initial = initial
        self.distances = distances
        self.n = n

    # some random actions from the given state
    def actions(self, state):
        actions = []
        if state is not None:

            # choose up to n-1 random positions to swap with position a
            a = random.randrange(1, len(state)-1)
            for i in range(1, self.n-1):
                b = random.randrange(1, len(state)-1)
                while a == b:
                    b = random.randrange(1, len(state)-1)
                actions.append([a, b])

            # add an additional swap which will swap the start/ending points with some other option
            actions.append(['swap', random.randrange(1, len(state)-1)])

        return actions

    # the resulting state
    def result(self, state, action):

        new_state = state[:]

        # swapping the endpoints out for a middle point
        if action[0] == 'swap':
            temp = new_state[action[1]]
            new_state[action[1]] = new_state[0]
            new_state[len(state)-1] = temp
            new_state[0] = temp
        # just swapping the two given points
        else:
            temp = new_state[action[0]]
            new_state[action[0]] = new_state[action[1]]
            new_state[action[1]] = temp

        return new_state

    # the distance of the trip
    def value(self, cities):
        cost = 0
        last_city = None
        for city in cities:
            if last_city is None:
                last_city = city
            else:
                cost += self.distances[str(last_city) + " --> " + str(city)]
                last_city = city

        return -cost


def compare_algorithms_for_this_world(world, dist_dict, attempts=30, print_solution=False):

    # using the initial as our baseline
    best_hill_climber = world
    best_annealing = world

    # initializing averages
    avg_hill_climber = 0
    avg_annealing = 0

    # our small world problem representation
    tsp = TSP(world, dist_dict)

    # try both algorithms over and over
    for i in range(0, attempts):

        hill_climber = hill_climbing(tsp)
        annealing = simulated_annealing(tsp, exp_schedule(k=20, lam=0.005, limit=1000))

        # keep track of the best solutions
        if tsp.value(hill_climber) > tsp.value(best_hill_climber):
                best_hill_climber = hill_climber
        if tsp.value(annealing) > tsp.value(best_annealing):
            best_annealing = annealing

        # maintain average values
        avg_hill_climber += tsp.value(hill_climber)
        avg_annealing += tsp.value(annealing)

    # Calculate the average
    avg_hill_climber /= attempts
    avg_annealing /= attempts

    # Ouptut: world statistics
    print("World of size " + str(len(world)) + " with " + str(attempts) + " per algorithm")

    hill_path = str(best_hill_climber)
    annealing_path = str(best_annealing)

    if not print_solution:
        hill_path = ""
        annealing_path = ""

    # Output: hill climbing results
    print("Hill Climbing:\t" + hill_path +
          "\tbest: " + str(tsp.value(best_hill_climber)) +
          "\tavg: " + str(round(avg_hill_climber, 2)))

    # Output: simulated annealing results
    print("Annealing:\t" + annealing_path +
          "\tbest: " + str(tsp.value(best_annealing)) +
          "\tavg: " + str(round(avg_annealing, 2)))


def generate_world(size=10, max_distance=10):

    # generating the world
    world = []
    for i in range(0, size):
        world.append(i)

    # generating the distance map
    distances = {}
    for city in world:
        other_cities = world[:]
        for other_city in other_cities:
            dist = random.randrange(1, max_distance)
            distances[str(city) + ' --> ' + str(other_city)] = dist
            distances[str(other_city) + ' --> ' + str(city)] = dist

    # return the generated world and distances dictionary
    return world, distances


if __name__ == '__main__':

    cities = ['D', 'A', 'C', 'B', 'D']
    distances_between_cities = {
        "A --> B": 1,
        "B --> A": 1,
        "A --> D": 5,
        "D --> A": 5,
        "A --> C": 4,
        "C --> A": 4,
        "B --> C": 6,
        "C --> B": 6,
        "B --> D": 2,
        "D --> B": 2,
        "C --> D": 3,
        "D --> C": 3
    }

    # test out the small world
    compare_algorithms_for_this_world(cities, distances_between_cities, print_solution=True)

    # generate and try out some larger worlds
    world_sizes = [4, 8, 16, 32, 64, 128]
    for world_size in world_sizes:
        cities, distances = generate_world(world_size)
        compare_algorithms_for_this_world(cities, distances)
