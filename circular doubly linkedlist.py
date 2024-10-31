class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class cdll():
    def __init__(self):
        self.head=None
    def insert_beg(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.prev=newnode
            newnode.next=newnode
        else:
            tail=self.head.prev
            newnode.prev=tail
            newnode.next=self.head
            self.head.prev=newnode
            tail.next=newnode
            self.head=newnode
    def insert_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.prev=newnode
            newnode.next=newnode
        else:
            tail=self.head.prev
            tail.next=newnode
            newnode.prev=tail
            newnode.next=self.head
            self.head.prev=newnode
            tail=newnode
    def insert_mid(self,data,postdata):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.prev=newnode
            newnode.next=newnode
            return
        if self.head.data==postdata:
            tail=self.head.prev
            newnode.prev=tail
            newnode.next=self.head
            self.head.prev=newnode
            tail.next=newnode
            self.head=newnode
            return
        else:
            temp=self.head
            while True:
                if temp.data==postdata:
                    newnode.prev=temp.prev
                    newnode.next=temp
                    temp.prev.next=newnode
                    temp.prev=newnode
                    return
                temp=temp.next
                if temp==self.head:
                    print(f"data not {postdata} found")
                    break
    def insert_mid_pre(self,data,predata):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.prev=newnode
            newnode.next=newnode
            return
        else:
            temp=self.head
            while True:
                if temp.data==predata:
                    newnode.prev=temp
                    newnode.next=temp.next
                    temp.next.prev=newnode
                    temp.next=newnode
                    return
                temp=temp.next
                if temp==self.head:
                    print(f"data not {predata} found")
                    break
    def search(self,data):
        temp=self.head
        i=0
        while True:
            if temp.data==data:
                print("%d is there"%(data))
                i=1
            temp=temp.next
            if temp.next==self.head:
                break
        if i==0:print("data not found",data)
    def display(self):
        k=[]
        temp=self.head
        while True:
            print(temp.data,end=" ")
            k.append(temp.data)
            temp=temp.next
            if temp==self.head:
                break
        print()
        j=len(k)
        print(k[j//2],"mid val")
    def delete(self,data):
        temp=self.head
        i=0
        while True:
            if temp.data==data:
                i=1
                if temp==temp.next:
                    self.head=None
                    return 
                if temp==self.head:
                    tail=self.head.prev
                    self.head=temp.next
                    self.head.prev=tail
                    tail.next=self.head
                else:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
            temp=temp.next
            if temp==self.head:
                break
        if i==0:
            print("data is not there",data)
cirdll=cdll()
cirdll.insert_beg(5)
cirdll.insert_beg(4)
cirdll.insert_beg(3)
cirdll.insert_beg(2)
cirdll.insert_beg(1)
cirdll.insert_end(7)
cirdll.insert_end(77)
cirdll.insert_end(777)
cirdll.insert_end(1)
cirdll.insert_end(7777)
cirdll.insert_mid(23,1)
cirdll.insert_mid(78,7)
cirdll.insert_mid_pre(90,23)
cirdll.insert_mid_pre(91,7777)
cirdll.insert_mid_pre(92,89)
cirdll.display()
cirdll.search(1)
cirdll.search(45)
cirdll.delete(1)
cirdll.delete(23)
cirdll.delete(91)
cirdll.delete(69)
cirdll.display()
