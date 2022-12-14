from collections import deque

class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list,heuristic):
        self.adjacency_list = adjacency_list
        self.h = heuristic

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes


    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        count_node = 0;
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h[v] < g[n] + self.h[n]:
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                print('The number of nodes to be expanted are:')
                print(count_node)
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    count_node +=1
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

adjacency_list_0 = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)],
    'D': []
}
heuristic_0 = {
    'A': 1,
    'B': 1,
    'C': 1,
    'D': 1
}
graph1 = Graph(adjacency_list_0,heuristic_0)
graph1.a_star_algorithm('A', 'D')
# ----Ph???n b??i t???p
# C??u 1: ch???y th??? A* v???i c??c ????? th???:
adjacency_list_1 = {
    'S': [('F', 3), ('A', 2), ('B', 1)],
    'F': [('G', 6)],
    'A': [('C', 2),('D',3)],
    'B': [('D',2),('E',4)],
    'C':[('G',4)],
    'D':[('G',4)],
    'E':[],
    'G':[]
        
}
heuristic_1 = {
    'S': 6,
    'A': 4,
    'B': 5,
    'C': 2,
    'D': 2,
    'E': 8,
    'F': 4,
    'G': 0,

}
print("????y l?? k???t qu??? A* ????? th??? 1:")
graph1 = Graph(adjacency_list_1,heuristic_1)
graph1.a_star_algorithm('S', 'G')
# ????? th??? 2:
adjacency_list_2 = {
    's': [('h', 7), ('f', 5)],
    'h': [('k', 6)],
    'f': [('p', 4)],
    'k': [('c', 5)],
    'p':[('q', 4)],
    'q':[('r',3)],
    'r':[('t',2)],
    't':[('g',1)],
    'c':[('a', 5)],
    'a': [('b', 4)],
    'b': [('d', 3)],
    'd': [('m', 2),('e', 4)],
    'e': [('n', 3)],
    'm': [('g', 1)],
    'n': [('m', 2)],
    'g': [],
        
}
heuristic_2 = {
     's': 4,
    'h': 3,
    'f': 5,
    'k': 2,
    'p': 4,
    'q': 3,
    'r': 2,
    't': 1,
    'c': 3,
    'a': 4,
    'b': 3,
    'd': 2,
    'e': 3,
    'm': 1,
    'n': 2,
    'g': 0,

}
print("????y l?? k???t qu??? A* ????? th??? 2:")
graph1 = Graph(adjacency_list_2,heuristic_2)
graph1.a_star_algorithm('s', 'g')

# ????? th??? 3:
adjacency_list_3 = {
    'A': [('B', 1), ('C', 4)],   
    'B': [('C',1),('D',5)],
    'C':[('D',3)],
    'D':[('F', 3), ('E', 8), ('G', 9)],
    'E':[('G',2)],
    'F':[('G',5)],
    'G':[]
}
heuristic_3_h1 = {    
    'A': 9.5,
    'B': 9,
    'C': 8,
    'D': 7,
    'E': 1.5,
    'F': 4,
    'G': 0,

}
heuristic_3_h2 = {    
    'A': 10,
    'B': 12,
    'C': 10,
    'D': 8,
    'E': 1,
    'F': 4.5,
    'G': 0,

}
print("????y l?? k???t qu??? A* ????? th??? 3:")
print("v???i h1 th??")
graph1 = Graph(adjacency_list_3,heuristic_3_h1)
graph1.a_star_algorithm('A', 'G')
print("v???i h2 th??")
graph1 = Graph(adjacency_list_3,heuristic_3_h2)
graph1.a_star_algorithm('A', 'G')
#????? th??? 4:
adjacency_list_4 = {
    'Arad': [('Zer',75),('Tim',118),('Sib',140)],
    'Zer': [('Ora',71)],
    'Tim': [('Lug',111)],
    'Sib': [('Fag',99),('Rim',80)],
    'Ora': [('Sib',151)],
    'Lug': [('Meh',70)],
    'Rim' :[('Pit',97),('Cra',146)],
    'Fag' :[('Buc',211)],
    'Meh' :[('Dob',75)],
    'Dob' :[('Cra',120)],
    'Cra' :[('Pit',138)],
    'Pit' :[('Buc',101)],
    'Buc':[]
        
}
heuristic_4 = {
    'Arad': 366,
    'Zer': 374,
    'Tim': 329,
    'Sib': 253,
    'Ora': 380,
    'Lug': 244,
    'Rim' : 193,
    'Fag' : 178,
    'Meh': 241,
    'Dob' : 242,
    'Cra' : 160,
    'Pit': 98,
    'Buc': 0

}
print("????y l?? k???t qu??? A* ????? th??? 4:")
graph1 = Graph(adjacency_list_4,heuristic_4)
graph1.a_star_algorithm('Arad', 'Buc')

