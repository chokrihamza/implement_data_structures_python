# implement circular linked list python
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
    
class CircularLinkedList:
    def __init__(self):
        self.head=None 
    
    def prepend(self,data)  :
        new_node=Node(data)
        cur=self.head
        new_node.next=self.head
        if not self.head:
            new_node.next=new_node
        else:
            while cur.next !=self.head:
                cur=cur.next
            cur.next=new_node 
        self.head=new_node # !!!!!!!!
    
    def append(self,data):
        if not self.head:
            self.head=Node(data)
            self.head.next=self.head
        else:
            new_node=Node(data)
            cur=self.head
            while cur.next != self.head:
                cur=cur.next
            cur.next=new_node
            new_node.next=self.head
    
    def remove(self,key):
        # if the removed is the head 
        if self.head.data==key:
            cur=self.head
            while cur.next != self.head:
                cur=cur.next
            cur.next=self.head.next
            self.head=self.head.next
        else:
            cur=self.head
            prev=None 
            while cur.next != self.head:
                prev=cur
                cur=cur.next
                if cur.data==key:
                    prev.next=cur.next
                    cur=cur.next
                    
    def print_list(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
            if cur==self.head:
                break
        
    def __len__(self):
        cur=self.head 
        count=0
        while cur:
            count+=1
            cur=cur.next
            if cur == self.head:
                break
        return count 
            
        
    def split_list(self):
        size=len(self)
        if size ==0:
            return None 
        if size ==1 :
            return self.head 
        mid=size//2
        count=0
        prev=None 
        cur=self.head 
        while cur and count <mid :
            count+=1
            prev=cur
            cur=cur.next
        prev.next=self.head 
        split_clinkedlist=CircularLinkedList()
        while cur.next != self.head:
            split_clinkedlist.append(cur.data)
            cur=cur.next 
        split_clinkedlist.append(cur.data)
        self.print_list()
        print("...")
        split_clinkedlist.print_list()
        
    def remove_node(self,node):
        # if the removed is the head 
        if self.head==node:
            cur=self.head
            while cur.next != self.head:
                cur=cur.next
            cur.next=self.head.next
            self.head=self.head.next
        else:
            cur=self.head
            prev=None 
            while cur.next != self.head:
                prev=cur
                cur=cur.next
                if cur==node:
                    prev.next=cur.next
                    cur=cur.next    
        
        
    def josephus_circle(self,step):
        cur=self.head 
        
        while len(self)>1:
            count=1
            while count != step:
                 cur=cur.next
                 count+=1
            print("Removed :"+str(cur.data))
            self.remove_node(cur)
            cur=cur.next
            
    def is_circular_linked_list(self,list):
        cur=list.head
        while cur.next:
            cur=cur.next
            if cur.next == list.head:
                return True
        return False 
    
    
    
    
    
        
clist=CircularLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.append(4)
#clist.remove_node(clist.head)
#clist.josephus_circle(2)
list=CircularLinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
#clist.prepend("e")
#clist.prepend("f")
#clist.remove("c")
#clist.remove("a")
#clist.split_list()
clist.print_list()
print(clist.is_circular_linked_list(list))
    
