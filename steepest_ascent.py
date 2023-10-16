import random

def initial_state(n):
    return [random.randint(0, n-1) for _ in range(n)]

def calculate_cost(state):
    n = len(state)
    cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                cost += 1
    return cost

def steepest_ascent_hill_climbing(n):
    best_state = initial_state(n)
    best_cost = calculate_cost(best_state)

    while True:
        neighbors = []
        for col in range(n):
            for row in range(n):
                if best_state[col] != row:
                    neighbor = list(best_state)
                    neighbor[col] = row
                    neighbors.append(neighbor)

        if not neighbors:
            break

        current_best_cost = best_cost
        for neighbor in neighbors:
            cost = calculate_cost(neighbor)
            if cost < current_best_cost:
                best_state = neighbor
                best_cost = cost

        if best_cost == current_best_cost:
            break

    return best_state, best_cost

def main():
    success_count = 0
    success_steps = 0
    failure_count = 0
    failure_steps = 0
    num_runs = 1000

    for _ in range(num_runs):
        result, cost = steepest_ascent_hill_climbing(8)
        if cost == 0:
            success_count += 1
            success_steps += 1
        else:
            failure_count += 1
            failure_steps += 1

    avg_success_steps = success_steps / success_count if success_count > 0 else 0
    avg_failure_steps = failure_steps / failure_count if failure_count > 0 else 0

    print(f"Success Count: {success_count}")
    print(f"Average Steps for Success: {avg_success_steps}")
    print(f"Failure Count: {failure_count}")
    print(f"Average Steps for Failure: {avg_failure_steps}")

if __name__ == "__main__":
    main()
