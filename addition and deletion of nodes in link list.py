class node:
    def __init__(self, data):         # initial node constructor
        self.data = data
        self.next = None
    def __str__(self):                # method overiding
        return(str(self.data))        # to return strings

class linkedlist(node):               # inherit class node
    def __init__(self):
        self.head = self.tail = None
    
    def add(self,data):
        if not self.head:
            self.head = self.tail = node(data)
        else:
            self.tail.next = node(data)
            self.tail = self.tail.next
    def delete(self, node):
        x = self.head
        if x.data == node:
            if self.head.next is None:      # setting new head
                self.head = None
                print("All nodes deleted")
            else:
                next = self.head.next       # setting new head
                self.head = None
                self.head = next
        elif self.tail.data == node:    #if data is in tail
            x = self.head               
            pre = None
            while(x):
                pre = x
                if x.next == self.tail:  # base case
                    break
                x = x.next
            pre.next = None             # removing tail node
            self.tail = pre             # setting new tail
        else:
            pre = None
            while(x):
                next = x.next
                if x.data == node:
                    break
                pre = x
                x = next
            pre.next = next
            x = None
    
    def __str__(self):
        x = self.head
        c = ""
        while(x):
            c += str(x.data) + " , "
            x = x.next
        return c[:-2]  

linklist_1 = linkedlist()
for i in range(10):
    linklist_1.add(i)

print("after addition")

print(linklist_1)

linklist_1.delete(9)

print("after deletion")

print(linklist_1)