class node:
    def __init__(self,data):
        self.data=data
        self.next=None 
    def __str__(self):
        return str(self.data)
class linked(node):
    def __init__(self):
        self.head=None 
        self.tail=None 
    def insert(self,data):
        if(self.head==None):
            self.head=self.tail=node(data)
        else:
            x=node(data)
            y=self.head
            flag=False
            while(y.next):
                if(str(y.data)==str(x)):
                    flag=True
                    break
            if(flag!=True):
                if(self.tail.next==None):
                    self.tail.next=x
                    self.tail=self.tail.next
    
    def __str__(self):
        x=self.head
        c=""
        while x.next:
            c+=str(x)
            c+="->"
            x=x.next
        c+=str(x)
        return c

a=linked()
b=list(map(str,input().split("->")))
for i in b: a.insert(i)
print(a)
