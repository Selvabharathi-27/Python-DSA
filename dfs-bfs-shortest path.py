def dfs(graph, vertex, unique=set()):
    result = []
    if vertex not in unique:
        unique.add(vertex)
        result.append(vertex)
        for i in graph.get(vertex, []):
            result.extend(dfs(graph, i, unique))
    return result

def bfs(graph,vertex):
    unique=set(vertex)
    result=[]
    queue=[vertex]
    while queue:
        i=queue.pop(0)
        result.append(i)
        for j in graph.get(i,[]):
            if j not in unique:
                queue.append(j)
                unique.add(j)
               
    return result
def shortpath(graph,vertex,endvertex):
    unique=set(vertex)
    result=[]
    queue=[(vertex,[vertex])]
    while queue:
        i,path=queue.pop(0)
        result.append(i)
        if i==endvertex:
            return path
        for j in graph.get(i,[]):
            if j not in unique:
                queue.append((j,path+[j]))
                unique.add(j)
    return None
    
graph={'A':['B','F'],'B':['C','I','A'],'C':['B','E'],'F':['A','E','I'],'E':['F','C','I'],'I':['A','B','C','E','F']}
print(graph)
v=dfs(graph,'A')
print(v)
print(bfs(graph,'A'))
print(shortpath(graph,'A','E'))





