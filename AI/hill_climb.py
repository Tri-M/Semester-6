def hill_climbing(problem):
    current = problem.initial()
    while True:
        neighbors = problem.neighbors(current)
        if not neighbors:
            break
        next_ = max(neighbors, key=problem.value)
        if problem.value(next_) <= problem.value(current):
            break
        current = next_
    return current
 #only implementation