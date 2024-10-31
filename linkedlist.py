class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class ll:
    def __init__(self):
        self.head=None
    def insert(self,data):
        run=node(data)
        if self.head is None:
            self.head=run
        else:
            temp=self.head
            while temp.ref is not None:
                temp=temp.ref
            temp.ref=run
    def printt(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.ref
        print()
    def delete(self,data):
        if self.head.data ==data:
            self.head=self.head.ref
        #else:
        temp=self.head
        while temp.ref is not None:
            if temp.ref.data!=data:                    
                temp=temp.ref
            else:
                temp.ref=temp.ref.ref
def reverse(self):
        pre=None
        temp=self.head
        while temp is not None:
            point=temp.ref
            temp.ref=pre
            pre=temp
            temp=point
        self.head=pre        
        
link=ll()
a=(4,2,3,4,5,4,5)
for i in a:
    link.insert(i)
link.printt()
link.delete(4)
link.printt()
