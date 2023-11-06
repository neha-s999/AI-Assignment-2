import heapq

def is_valid_state(state):
    ML, CL, MR, CR, B = state
    return (ML >= 0 and CL >= 0 and MR >= 0 and CR >= 0 and
            (ML == 0 or ML >= CL) and (MR == 0 or MR >= CR))

def move(state, action):
    ML, CL, MR, CR, B = state
    if B == 0:
        return (ML - action[0], CL - action[1], MR + action[0], CR + action[1], 1)
    else:
        return (ML + action[0], CL + action[1], MR - action[0], CR - action[1], 0)

def heuristic(state):
    ML, CL, MR, CR, B = state
    people_on_right = MR + CR
    trips_needed = (people_on_right + 1) // 2
    return trips_needed

def missionary_cannibal_Greedy_Best_First():
    start_state = (3, 3, 0, 0, 0)
    goal_state = (0, 0, 3, 3, 1)

    visited = set()
    priority_queue = [(heuristic(start_state), start_state, [])]

    while priority_queue:
        _, current_state, path = heapq.heappop(priority_queue)

        if current_state == goal_state:
            return path

        visited.add(current_state)

        for action in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
            next_state = move(current_state, action)
            if is_valid_state(next_state) and next_state not in visited:
                heapq.heappush(priority_queue, (heuristic(next_state), next_state, path + [next_state]))

    return None

def missionary_cannibal_A_Star():
    start_state = (3, 3, 0, 0, 0)
    goal_state = (0, 0, 3, 3, 1)

    def a_star_cost(state, path):
        return len(path) + heuristic(state)

    visited = set()
    priority_queue = [(a_star_cost(start_state, []), start_state, [])]

    while priority_queue:
        _, current_state, path = heapq.heappop(priority_queue)

        if current_state == goal_state:
            return path

        visited.add(current_state)

        for action in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
            next_state = move(current_state, action)
            if is_valid_state(next_state) and next_state not in visited:
                heapq.heappush(priority_queue, (a_star_cost(next_state, path + [next_state]), next_state, path + [next_state]))

    return None

solution_gbfs = missionary_cannibal_Greedy_Best_First()
print("Greedy Best-First Search Solution:")
print(solution_gbfs)

solution_astar = missionary_cannibal_A_Star()
print("A* Search Solution:")
print(solution_astar)
