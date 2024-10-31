class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class doublylinkedlist():
    def __init__(self):
        self.root=None
    def insert_at_beg(self,data):
        newnode=Node(data)
        if  self.root is None:
            self.root=newnode
        else:
            newnode.next=self.root
            self.root.prev=newnode
            self.root=newnode
    def insert_at_end(self,data):
        newnode=Node(data)
        if  self.root is None:
            self.root=newnode
        else:
            temp=self.root
            while temp.next is not None:
                temp=temp.next
            newnode.prev=temp
            temp.next=newnode
    def display(self):
        temp=self.root
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def search(self, data):
        temp=self.root
        i=True
        while temp is not None:
            if temp.data==data:
                print(data,"is found")
                i=False
            temp=temp.next
        if i is True:
            print(data,"not found")
        
    def remove(self,data):
        temp=self.root
        while temp:
            if temp.data==data:
                if temp.prev is not None:
                    temp.prev.next=temp.next
                if temp.next is not None:
                    temp.next.prev=temp.prev
                if temp==self.root:
                    self.root=temp.next
                return
            temp=temp.next
            
        
dll=doublylinkedlist()
dll.insert_at_end(2)
dll.insert_at_end(4)
dll.insert_at_end(5)
dll.insert_at_end(9)
dll.display()
dll.insert_at_beg(0)
dll.insert_at_beg(1)
dll.display()
dll.search(1)
dll.remove(1)
dll.display()
dll.remove(9)
dll.display()
dll.search(1)
dll.search(90)
dll.search(0)
