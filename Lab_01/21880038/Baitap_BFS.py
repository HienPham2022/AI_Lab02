#cài đặt lại code mẫu BFS
from importlib.resources import path

print("Đây là kết quả chạy 2 source code mẫu: ")
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
visited = []
queue = []
def bfs_1(visited,graph,start,end):
    visited.append(start)
    queue.append(start)

    while queue:
        s= queue.pop()
        print(s,end =" ")
        if s == end:
            return
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs_1(visited,graph,'A','F') 
print("")
#======BFS có xuất ra dường đi======
graph = {
    '1':['2','3','4'],
    '2':['5','6'],
    '5':['9','10'],
    '4':['7','8'],
    '7':['11','12']
}
def bfs(graph,start,end):
    visited = []
    queue = []

    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
print("BFS có xuất ra đường đi:")
print(bfs(graph,'1','11'))
print("================================================")
#thực thi kết quả với 3 đồ thị
# đồ thị thứ 1:
print("Kết quả của đồ thị thứ 1: ")
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

print("Xuất ra đường đi:")
print(bfs(graph,'S','G')) 
print("")
print("================================================")
#Đồ thị thứ 2:
print("Kết quả của đồ thị thứ 2: ")
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

print("Xuất ra đường đi:")
print(bfs(graph,'s','g')) 
print("")
print("================================================")
#Đồ thị thứ 3
print("Kết quả của đồ thị thứ 3: ")
graph = {
    'A':['B','C'],
    'D':['E','G','F'],
    'E':['G'],
    'B':['D','C'],
    'C':['D'],    
    'F':['G'],
    'G':[]
}

print("Xuất ra đường đi:")
print(bfs(graph,'A','G')) 
print("")
print("================================================")