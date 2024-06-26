class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class stack:
    def __init__(self):
        self.top=node(8)

    def push(self,value):
        new_node=node(value)
        new_node.next=self.top
        self.top=new_node

    def isempty(self):
        if self.top is None:
            return

    def pop(self):
        if self.top is not None:
            popped=self.top.value
            self.top=self.top.next
            return popped
    
class text_editor:
    def __init__(self):
        self.content=""
        self.undo_stack=stack()

    def add_stack(self,text):
        self.content+=text
        self.undo_stack.push(len(text))
            
    def undo(self):
        if not self.undo_stack.isempty():
            length=self.undo_stack.pop()
            self.content=self.content[:-length]
            
    def display(self):
        print("current content: ")
        print(self.content)

editor=text_editor()
editor.add_stack("Hello ")
editor.add_stack("World")
editor.undo()
editor.display()




    
'''def traversal(self):
        root=self.top
        while root:
            print(root.value,'-->',end="")
            root=root.next
        print("null")'''


sta=stack()
'''sta.push(4)
sta.push(16)
sta.push(44)
sta.push(11)
sta.pop()
sta.traversal()
print(sta.top.value)'''