class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bintree():
    def __init__(self):
        self.root=None
    def add(self,data):
        #newnode=node(data)
        if self.root is None:
            self.root=Node(data)
            return
        self.Reccall(data,self.root)
    def Reccall(self,data,node):
        #newnode=node(data)
        if node.left is None:
            node.left=Node(data)
        elif node.right is None:
            node.right=Node(data)
        else:
            self.Reccall(data,node.left)
    def remove(self,data):
        if not self.root:
            print("00000")
            return
        if self.root.data==data:
            self.root=None
            return
        self.recdel(data,self.root)
        #if Recdel
        
    def recdel(self,data,node):
        if node.left and node.left.data==data:
            node.left=None
        elif node.right and node.right.data==data:
            node.right=None
        elif node.left:
            self.recdel(data,node.left)
        elif node.right:
            self.recdel(data,node.right)
        
    def display(self,node=None,depth=0):
        if node is None:
            node=self.root
        print(" "*depth,node.data)
        if node.left is not None:
            self.display(node.left,depth+2)
        if node.right is not None:
            self.display(node.right,depth+2)
tree=bintree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.display()
tree.remove(4)
tree.display()

