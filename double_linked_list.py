class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node = None
        self.previous_node = None

class Double_LinkedList():

    def __init__(self):
        self.head = None


    def insert_first(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_last(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head= new_node
        else:
            new_node.previous_node = self.head
            self.head = new_node

    def remove(self,data):
        current_node  = self.head
        previous_node = None

        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node
        if previous_node is None:
            self.head =  previous_node
        else:
            previous_node.next_node = current_node.next_node
            current_node.next_node.previous_node = current_node.previous_node

    def TransverseList(self):
        l= []
        actual_node = self.head
        while actual_node is not None:
            l.append(actual_node.data)
            actual_node = actual_node.next_node
        return l



Double_LinkedList = Double_LinkedList()
Double_LinkedList.insert_first(10)
Double_LinkedList.insert_first(20)
Double_LinkedList.insert_first(30)
Double_LinkedList.insert_first(40)
Double_LinkedList.insert_first(50)


print(Double_LinkedList.TransverseList())
Double_LinkedList.remove(30)
print(Double_LinkedList.TransverseList())






