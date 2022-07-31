from collections import deque

class Graph:
  

    def __init__(self,adjacency_list,heuristic):
        self.adjacency_list = adjacency_list
        self.h = heuristic

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def a_star_algorithm(self, start_node, stop_node):
        count_node = 0;
        open_list = set([start_node])
        closed_list = set([])

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or self.h[v] < self.h[n]:
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

            
            for (m) in self.get_neighbors(n):
                
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    count_node +=1
                    parents[m] = n
                    

               
                else:
                    if self.h[m] > self.h[n]:
                        self.g[m] = self.g[n]
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

adjacency_list_0 = {
    'A': [('B'), ('C'), ('D')],
    'B': [('D')],
    'C': [('D')],
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
# ----Phần bài tập
# Câu 1: chạy thử Greedy với các đồ thị:
adjacency_list_1 = {
    'S': [('F'), ('A'), ('B')],
    'F': [('G')],
    'A': [('C'),('D')],
    'B': [('D'),('E')],
    'C':[('G')],
    'D':[('G')],
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
print("đây là kết quả Greedy đồ thị 1:")
graph1 = Graph(adjacency_list_1,heuristic_1)
graph1.a_star_algorithm('S', 'G')
# Đồ thị 2:
adjacency_list_2 = {
    's': [('h' ), ('f' )],
    'h': [('k' )],
    'f': [('p' )],
    'k': [('c' )],
    'p':[('q' )],
    'q':[('r')],
    'r':[('t')],
    't':[('g')],
    'c':[('a' )],
    'a': [('b' )],
    'b': [('d' )],
    'd': [('m' ),('e' )],
    'e': [('n' )],
    'm': [('g' )],
    'n': [('m' )],
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
print("đây là kết quả Greedy đồ thị 2:")
graph1 = Graph(adjacency_list_2,heuristic_2)
graph1.a_star_algorithm('s', 'g')

# Đồ thị 3:
adjacency_list_3 = {
    'A': [('B'), ('C')],   
    'B': [('C'),('D')],
    'C':[('D')],
    'D':[('F'), ('E'), ('G')],
    'E':[('G')],
    'F':[('G')],
    'G':[],
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
print("đây là kết quả Greedy đồ thị 3:")
print("với h1 thì")
graph1 = Graph(adjacency_list_3,heuristic_3_h1)
graph1.a_star_algorithm('A', 'G')
print("với h2 thì")
graph1 = Graph(adjacency_list_3,heuristic_3_h2)
graph1.a_star_algorithm('A', 'G')
#Đồ thị 4:
adjacency_list_4 = {
    'Arad': [('Zer'),('Tim'),('Sib')],
    'Zer': [('Ora')],
    'Tim': [('Lug')],
    'Sib': [('Fag'),('Rim')],
    'Ora': [('Sib')],
    'Lug': [('Meh')],
    'Rim' :[('Pit'),('Cra')],
    'Fag' :[('Buc')],
    'Meh' :[('Dob')],
    'Dob' :[('Cra')],
    'Cra' :[('Pit')],
    'Pit' :[('Buc')],
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
print("đây là kết quả Greedy đồ thị 4:")
graph1 = Graph(adjacency_list_4,heuristic_4)
graph1.a_star_algorithm('Arad', 'Buc')

