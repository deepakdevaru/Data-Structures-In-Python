class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node= None

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
    # time comolexity O(1)
    def insertstart(self,data):
        self.size +=1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node =  self.head
            self.head = new_node

    def remove(self,data):
        if self.head is not None:
             self.size= self.size-1
             current_node = self.head
             previous_node = None
             while current_node.data != data:
                 previous_node = current_node
                 current_node= current_node.next_node

             if previous_node is None:
                 self.head = previous_node
             else: previous_node.next_node = current_node.next_node

        else: return 0

    def sizes(self):
        return  self.size

    def adding_at_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head= new_node

        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node


    def TransverseList(self):
        l=[]
        actual_node = self.head
        while actual_node is not None:
            l.append(actual_node.data)
            actual_node= actual_node.next_node
        return l





LinkedList = LinkedList()
LinkedList.insertstart(10)
LinkedList.insertstart(12)
LinkedList.insertstart(-13)
LinkedList.insertstart(9)

print ("The size of linked list is : " ,LinkedList.sizes())
print ("The elemets of linked list are: ", LinkedList.TransverseList())

LinkedList.remove(-13)

print ("The elemets of linked list after removing are: ", LinkedList.TransverseList())



LinkedList.adding_at_end(971)

print("The elemets of linked list are: ", LinkedList.TransverseList())



