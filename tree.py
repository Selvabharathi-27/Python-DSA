class node():
    def __init__(self,data):
        self.data=data
        self.child=[]
class new():
    def __init__(self):
        self.root=None
    
    def insert(self,data,parentnode=None):
        fun=node(data)
        if not self.root:
            self.root=fun
            return
        findparent=self.findpn(parentnode,self.root)
        if not findparent:
            print("parent is not")
            return
        findparent.child.append(fun)
    
    def findpn(self,data,nodee):
        if nodee.data==data:
            return nodee
        for children in nodee.child:
            newnode=self.findpn(data,children)
            if newnode:
                return newnode
        return None
    def remove(self,data):
        if self.root.data==data:
            self.root=None
            return
        parent=self.findrevpn(data,self.root)
        if parent:
            for children in parent.child:
                if children.data==data:
                    parent.child.remove(children)
                    return
        print("node not identified")
    def findrevpn(self,data,node):
        for children in node.child:
            if children.data==data:
                return node
            newnode1=self.findrevpn(data,children)
            if newnode1:
                return newnode1
        return None
    def prin(self,node,level=0):
        if node:
            print(" "*level+str(node.data))
        for i in node.child:
            self.prin(i,level+1)
New=new()
New.insert(3)
print("parent")
New.insert(8,3)
print("child")
New.insert(9,3)
print("child")
New.insert(6,3)
print("child")
New.insert(3,8)
print("child")
New.insert(6,1)
print("child")
New.insert(3,3)
New.prin(New.root)







