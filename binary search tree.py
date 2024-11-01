class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst():
    def __init__(self):
        self.root=None
    def insert(self,data):
        if not self.root:
            self.root=Node(data)
            return
        self.insertionrecurive(data,self.root)
    def insertionrecurive(self,data,node):
        if node.data>data:
            if not node.left:
                node.left=Node(data)
            else:
                self.insertionrecurive(data,node.left)    
        elif node.data<data:
            if not node.right:
                node.right=Node(data)
            else:
                self.insertionrecurive(data,node.right)
    def inorderdisplay(self):
        result=[]
        self.inorder(self.root,result)
        for i in result:
            print(i,end=" ")
    def inorder(self,node,result):
        if not node:
            return 
        self.inorder(node.left,result)
        result.append(node.data)
        self.inorder(node.right,result)
        
    def preorderdisplay(self):
        result=[]
        self.preorder(self.root,result)
        for i in result:
            print(i,end=" ")
    def preorder(self,node,result):
        if not node:
            return
        result.append(node.data)
        self.preorder(node.left,result)
        self.preorder(node.right,result)
    def search(self,data):
        Search=self.Searchrec(data,self.root)
        if Search:
            print("TRUE")
        else:
            print("False")
    def Searchrec(self,data,node):
        if not  node:
            return node
        if node and node.data==data:
            return node
        elif node.data>data:
            return self.Searchrec(data,node.left) 
        elif node.data<data:
            return self.Searchrec(data,node.right) 
    def remove(self,data):
        if self.root.data==data:
            self.root=None
            return
        self.delrec(data,self.root)
    def delrec(self,data,node):
        
        if node.left and node.left.data==data:
            node.left=None
            return
        if node.right and node.right.data==data:
            node.right=None
            return
        if node.data>data:
            self.delrec(data,node.left) 
        else:
            self.delrec(data,node.right) 
bstree=bst()
bstree.insert(23)
bstree.insert(45)
bstree.insert(12)
bstree.insert(5)
bstree.insert(67)
bstree.insert(44)
bstree.insert(45)
bstree.search(5)
bstree.inorderdisplay()
print()
bstree.preorderdisplay()
print()
bstree.remove(12)
bstree.preorderdisplay()
print()
bstree.search(44)
bstree.search(23)
bstree.search(5)






