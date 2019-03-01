from csp import backtracking_search, mrv, forward_checking, parse_neighbors, CSP, min_conflicts

# options for the classes
classes = 'CS-108 CS-112 CS-212 CS-214 CS-344 CS-384 CS-398'.split()
rooms = 'NH253 SB382'.split()
time_slots = 'MWF800 MWF900 MWF1030 TTh1030 TTh12:05'.split()
professors = 'Adams Plantinga Schuurman Vanderlinden'.split()

# all the domain possibilities
domain_possibilities = []
for room in rooms:
    for time_slot in time_slots:
        for prof in professors:
            domain_possibilities.append(prof + " " + room + " " + time_slot)

# variables : courses
# domains : everything else
variables = classes
domains = {}
for var in variables:
    domains[var] = domain_possibilities

# neighbors : everybody is a neighbor
neighbors = parse_neighbors("""CS-344: NH158 8MWF""", variables)
for type in [classes, domain_possibilities]:
    for A in type:
        for B in type:
            if A != B:
                if B not in neighbors[A]:
                    neighbors[A].append(B)
                if A not in neighbors[B]:
                    neighbors[B].append(A)


# constraint function
# ensuring that a room is acceptable
# and that no schedule conflicts occur 
# (i.e. kvlinden can't be in two rooms at once)
def scheduler_constraint(A, a, B, b, recurse=0):
    prof_a = a.split()[0]
    room_a = a.split()[1]
    time_a = a.split()[2]

    prof_b = b.split()[0]
    room_b = b.split()[1]
    time_b = b.split()[2]

    # Schuurman must teach 108
    if (A == "CS-108" and prof_a != "Schuurman") or (B == "CS-108" and prof_b != "Schuurman"):
        return False

    # Adams must teach 112
    if (A == "CS-112" and prof_a != "Adams") or (B == "CS-112" and prof_b != "Adams"):
        return False

    # Plantinga must teach 212
    if (A == "CS-212" and prof_a != "Plantinga") or (B == "CS-212" and prof_b != "Plantinga"):
        return False

    # Adams must teach 214
    if (A == "CS-214" and prof_a != "Adams") or (B == "CS-214" and prof_b != "Adams"):
        return False

    # Vanderlinden must teach 344
    if (A == "CS-344" and prof_a != "Vanderlinden") or (B == "CS-344" and prof_b != "Vanderlinden"):
        return False

    # Schuurman must teach 384
    if (A == "CS-384" and prof_a != "Schuurman") or (B == "CS-384" and prof_b != "Schuurman"):
        return False

    # Vanderlinden must teach 398
    if (A == "CS-398" and prof_a != "Vanderlinden") or (B == "CS-398" and prof_b != "Vanderlinden"):
        return False

    # professor can only teach one course at a time
    if(prof_a == prof_b) and (time_a == time_b):
        return False

    # we can't have two courses in the same room at the same time
    if(room_a == room_b) and (time_a == time_b):
        return False

    return True


problem = CSP(variables, domains, neighbors, scheduler_constraint)
solution = backtracking_search(problem)
print(solution)
solution = min_conflicts(problem)
print(solution)
