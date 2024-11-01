class Graph:
    def __init__(self):
        self.graph={}
    def addvertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def addedge(self,v1,v2,isdirected=False):
        self.addvertex(v1)
        self.addvertex(v2)
        self.graph[v1].append(v2)
        if isdirected is False:
            self.graph[v2].append(v1)
    def vertex(self):
        for i in self.graph:
            print(i,end=" ")
        print()
    def display(self):
        for i,j in self.graph.items():
            print(i,"=>",j,end=" ")
        print()
    def edges(self):
        for i,j in self.graph.items():
            for k in j:
                print(f"{i}=>{k}",end=" ")
        print()
    def removevertex(self,v1):
        if v1 in self.graph:
            del self.graph[v1]
        for i,j in self.graph.items():
            if v1 in j:
                self.graph[i].remove(v1)
    def removeedges(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            if v1 in self.graph[v2]:
                self.graph[v2].remove(v1)
            if v2 in self.graph[v1]:
                self.graph[v1].remove(v2)
        elif v1 in self.graph:
            if v2 in self.graph[v1]:
                self.graph[v1].remove(v2)
        elif v2 in self.graph:
            if v1 in self.graph[v2]:
                self.graph[v2].remove(v1)
        
            
            
gr=Graph()
gr.addedge('a','b')
gr.addedge('b','c',isdirected=True)
gr.vertex()
gr.edges()
print(gr.graph)
gr.removevertex('c')
print(gr.graph)
gr.removeedges('m','n')
print(gr.graph)






