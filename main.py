import time
import random
from greedy_bfs import greedy_bfs
from a_star import a_star_search

PROBLEMS = [
    {"init": [[1, 2, 3], [5, 0, 4], [6, 7, 8]],
        "goal": [[0, 1, 2], [5, 4, 3], [6, 7, 8]]},
    {"init": [[7, 2, 4], [5, 0, 6], [8, 3, 1]],
        "goal": [[0, 1, 2], [3, 4, 5], [6, 7, 8]]},
    {"init": [[0, 2, 3], [1, 4, 5], [8, 7, 6]],
        "goal": [[1, 2, 3], [8, 0, 4], [7, 6, 5]]}
]

# PROBLEM_STATE = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# MAX = 5

# RANDOM_PROBLEMS = [
#     {"init": random.shuffle(PROBLEM_STATE), "goal": random.shuffle(PROBLEM_STATE)} for i in range(MAX)
# ]


def timer(problem, func):
    start = time.time()
    func(problem["init"], problem["goal"])
    end = time.time()
    print(f"{end - start}")


for i, problem in enumerate(PROBLEMS):
    print(f"Problem {i}:")
    print(f"Init State:")
    print(problem["init"])
    print(f"Goal State:")
    print(problem["goal"])

    print("")
    print("Greedy Best First Search")
    timer(problem, greedy_bfs)

    print("A Star Search")
    timer(problem, a_star_search)

    print("")
