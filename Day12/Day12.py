import copy

class cave:

    def __init__(self):
        self.path = []
        self.is_big = False
        self.num_visited = 0

    def add_conn(self, str):
        self.path.append(str)

def explore_cave(current, curr_graph, curr_path):
    global total_paths
    curr_path.append(current)
    if current == 'end':
        total_paths.append([curr_path])
        return

    if curr_graph[current].is_big == False and curr_graph[current].num_visited > 0:
        return

    curr_graph[current].num_visited += 1

    for i in curr_graph[current].path:
        explore_cave(i, copy.deepcopy(curr_graph), copy.deepcopy(curr_path))

def slow_explore_cave(current, curr_graph, has_visited_twice):
    global valid_paths
    if current == 'end':
        valid_paths += 1
        return
    
    curr_graph[current].num_visited += 1

    if curr_graph[current].is_big == False:
       n_visit = curr_graph[current].num_visited
       if(has_visited_twice == True and n_visit >= 2):
           return
       if(has_visited_twice == False and n_visit == 3):
           return
       if(has_visited_twice == False and n_visit == 2):
           has_visited_twice = True

    for i in curr_graph[current].path:
        if i != 'start':
            slow_explore_cave(i, copy.deepcopy(curr_graph), has_visited_twice)


total_paths = []

with open('input.txt') as file:
    graph = {};
    for line in file:
        conns = line.strip().split('-')
        for conn in conns:
            if not graph.__contains__(conn):
                graph[conn] = cave()
                graph[conn].is_big = conn.isupper()
        graph[conns[0]].add_conn(conns[1])
        graph[conns[1]].add_conn(conns[0])
    explore_cave('start', copy.deepcopy(graph), [])
    print('Part 1: ' + str(len(total_paths)))

valid_paths = 0

with open('input.txt') as file:

    graph = {};

    for line in file:
        conns = line.strip().split('-')
        for conn in conns:
            if not graph.__contains__(conn):
                graph[conn] = cave()
                graph[conn].is_big = conn.isupper()
        graph[conns[0]].add_conn(conns[1])
        graph[conns[1]].add_conn(conns[0])

    slow_explore_cave('start', copy.deepcopy(graph), False)

    print('Part 2: ' + str(valid_paths))


