from copy import deepcopy

INIT_STATE = [[1, 2, 3], [5, 0, 4], [6, 7, 8]]
GOAL_STATE = [[0, 1, 2], [5, 4, 3], [6, 7, 8]]
DIM = 3

node_created = 1


def is_equal(first_state, second_state):
    if first_state is None or second_state is None:
        return False

    for i in range(DIM):
        for j in range(DIM):
            if(first_state[i][j] != second_state[i][j]):
                return False
    return True


def operator(state, node):
    global node_created
    states = []

    zero_i = None
    zero_j = None

    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 0:
                zero_i = i
                zero_j = j
                break

    def add_swap(i, j):
        new_state = deepcopy(state)
        new_state[i][j], new_state[zero_i][zero_j] = new_state[zero_i][zero_j], new_state[i][j]
        states.append(new_state)

    # kiri
    if zero_j != 0:
        add_swap(zero_i, zero_j - 1)

    # kanan
    if zero_j != len(state) - 1:
        add_swap(zero_i, zero_j + 1)

    # atas
    if zero_i != 0:
        add_swap(zero_i - 1, zero_j)

    # bawah
    if zero_i != len(state) - 1:
        add_swap(zero_i + 1, zero_j)

    return states


class Tree:
    def __init__(self, state=None, parent=None, depth=0, node_number=1, children=[]):
        self.state = state
        self.parent = parent
        self.cost = self.manhattan()
        self.depth = depth
        self.node_number = node_number
        self.children = children

    def __str__(self):
        return str(self.state) + " fn " + str(self.depth + self.cost)

    def manhattan(self):
        # manhattan
        result = 0
        for i in range(DIM):
            for j in range(DIM):
                if (GOAL_STATE[i][j] == 0):
                    continue
                for l in range(DIM):
                    for m in range(DIM):
                        if (GOAL_STATE[i][j] == self.state[l][m]):
                            result += (abs(m - j) + abs(l - i))
                            break
        return result

    def get_parent_state(self):
        if self.parent is None:
            return None
        return self.parent.state

    def add_children(self):
        global node_created
        new_states = operator(self.state, self)
        for state in new_states:
            node_created = node_created + 1
            self.children.append(
                Tree(state, self, self.depth + 1, node_created, []))


tree = None


def a_star_search():
    global node_created
    priority_queue = []

    tree = Tree(INIT_STATE)

    while not is_equal(tree.state, GOAL_STATE):
        tree.add_children()

        for child in tree.children:
            priority_queue.append(
                [child, child.cost + child.depth, child.node_number])

        priority_queue.sort(key=lambda x: (-x[1], -x[2]))
        tree = priority_queue.pop()[0]

    output = []
    output.append(tree.state)
    while tree.parent is not None:
        tree = tree.parent
        output.append(tree.state)

    for out in output[::-1]:
        print(out)


a_star_search()
