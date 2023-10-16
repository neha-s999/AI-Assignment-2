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

def missionary_cannibal_DFS():
    start_state = (3, 3, 0, 0, 0)
    goal_state = (0, 0, 3, 3, 1)

    def dfs(state, path):
        if state == goal_state:
            return path

        visited.add(state)

        for action in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
            next_state = move(state, action)
            if is_valid_state(next_state) and next_state not in visited:
                result = dfs(next_state, path + [next_state])
                if result is not None:
                    return result

    visited = set()
    return dfs(start_state, [start_state])

solution_dfs = missionary_cannibal_DFS()
print(solution_dfs)
