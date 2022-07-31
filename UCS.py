from collections import deque
from lib2to3.pytree import convert

class Graph:
   
    def __init__(self, adjacency_list):
       
        self.adjacency_list = adjacency_list
        

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    

    def a_star_algorithm(self, start_node, stop_node):
        count_node = 0;
        open_list = set([start_node])
        closed_list = set([])

        g = {}

        g[start_node] = 0

        
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

           
            for v in open_list:
                if n == None or g[v]  < g[n] :
                    
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

           
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

            
            for (m, weight) in self.get_neighbors(n):
                
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    count_node +=1
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)],
    'D': []
}

graph1 = Graph(adjacency_list)

graph1.a_star_algorithm('A', 'D')

# ----Phần bài tập
# Câu 1: chạy thử UCS với các đồ thị:
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

print("đây là kết quả UCS đồ thị 1:")
graph1 = Graph(adjacency_list_1)
graph1.a_star_algorithm('S', 'G')
# Đồ thị 2:
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

print("đây là kết quả UCS đồ thị 2:")
graph1 = Graph(adjacency_list_2)
graph1.a_star_algorithm('s', 'g')

# Đồ thị 3:
adjacency_list_3 = {
    'A': [('B', 1), ('C', 4)],   
    'B': [('C',1),('D',5)],
    'C':[('D',3)],
    'D':[('F', 3), ('E', 8), ('G', 9)],
    'E':[('G',2)],
    'F':[('G',5)],
    'G':[]
}

print("đây là kết quả UCS đồ thị 3:")
graph1 = Graph(adjacency_list_3)
graph1.a_star_algorithm('A', 'G')

#Đồ thị 4:
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

print("đây là kết quả UCS đồ thị 4:")
graph1 = Graph(adjacency_list_4)
graph1.a_star_algorithm('Arad', 'Buc')

