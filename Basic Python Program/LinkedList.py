class node:
    def __init__(self,value):
        self.value=value
        self.next=None


head=node(10)
tail=head

#print(head.value)
#print(tail.value)

def insert_front(head,value):
    if head==None:
        head=node(value)
        return head
    else:
        ne=node(value)
        ne.next=head
        head=ne
        return head
head=insert_front(head,20)
def insert_last(tail,value):
    if tail==None:
        tail=node(value)
        return tail
    else:
        ne=node(value)
        tail.next=ne
        return ne

tail=insert_last(tail,5)
tail=insert_last(tail,14)
def remove(head,tail,value):
    if head == None:
        return head,tail
    
    if head.value==value:
        new_head=head.next

        if head==tail:
            return new_head,tail
        return new_head,tail
    root=head
    while root.next:
        if root.next.value==value:
            root.next=root.next.next
            if root.next is None:
                return head,root
            return head,tail
        root=root.next
    return head,tail
head,tail=remove(head,tail,10)
def traversal(head):
    root=head
    while root:
        print(root.value,'-->',end="")
        root=root.next
    print("")
traversal(head)
