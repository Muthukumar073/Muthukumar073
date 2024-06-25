class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    
class doublelinkedlist:
    def __init__(self):
        self.head=node(8)
        self.tail=self.head
        

    def prepend(self,value):
        new_node=node(value)
        self.head.prev=new_node
        new_node.next=self.head
        self.head=new_node
        
    def append(self,value):
        new_node=node(value)
        self.tail.next=new_node
        new_node=self.tail
        self.tail=new_node.next
    
    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next  # fcurrent is the head
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  # current is the tail

                # If the node to be deleted is both head and tail (only node in the list)
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None

                return True  # Node found and deleted
            current = current.next

        return False  #Node not found

    def traversal(self):
        root=self.head
        while root:
            print(root.value,'-->',end=" ")
            root=root.next
        print("Null")

dll=doublelinkedlist()
dll.prepend(4)
dll.prepend(1)
dll.append(6)
dll.append(19)
dll.delete(1)
dll.traversal()
print(dll.head.value)


   
 


    

    
