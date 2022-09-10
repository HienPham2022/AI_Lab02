#cài đặt DFS
from importlib.resources import path
from inspect import stack


 # Set to keep track of visited nodes of graph.

def dfs(graph, root_node,end_node):
    traversed = [root_node]
    stack = [root_node]
    while stack:
        vertex = stack[-1]
        if vertex == end_node:
            traversed.extend(vertex)
            return traversed
        if vertex not in traversed:
            traversed.extend(vertex)
        pop = True
        for adjacent in graph[vertex]:
            if adjacent not in traversed:
                stack.extend(adjacent)
                pop = False
                break
        if pop:
            stack.pop()
    return traversed
#Đồ thị thứ 1:

graph = {
    'S':['D','E','P'],
    'D':['B','C','E'],
    'P':['Q'],
    'E':['R','H'],
    'B':['A'],
    'C':['A'],
    'A':[],    
    'H':['P','Q'],
    'R':['F'],
    'F':['C','G'],    
    'Q':[],
    'G':[]
}
print("Đây là kết quả đồ thị thứ 1-DFS: ")
print (dfs(graph, 'S','G'))
print("===================================")

#Đồ thị thứ 2:
graph = {
    's':['f','h'],
    'f':['p'],
    'h':['k'],
    'k':['c'],
    'c':['a'],
    'p':['q'],
    'q':['r'],    
    'r':['t'],
    't':['g'],
    'a':['b'],    
    'b':['d'],
    'd':['e','m'],
    'e':['n'],
    'm':['g','n'],
    'n':[],
    'g':[]
}
print("Đây là kết quả đồ thị thứ 2-DFS: ")
print (dfs(graph, 's','g'))
print("===================================")

#Đây là kết quả đồ thị thứ 3
graph = {
    'A':['B','C'],
    'D':['E','G','F'],
    'E':['G'],
    'B':['D','C'],
    'C':['D'],    
    'F':['G'],
    'G':[]
}
print("Đây là kết quả đồ thị thứ 3-DFS: ")
print (dfs(graph, 'A','G'))
print("===================================")