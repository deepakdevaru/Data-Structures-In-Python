class Node():
    def __init__(self,data):
        self.datas = data
        self.right_Child = None #greater than root
        self.left_Child = None #smaller than root


class BinaryTree:
    def __init__(self):
        self.root = None

    #call this for insert node
    def insert(self,data):
        if self.root is  None:
            self.root = Node(data)

        else:
            nodes = self.root
            self.insertnode(data,nodes)


    def insertnode(self,data,nodes):
        if data < nodes.datas:
            if nodes.left_Child is not None:
                self.insertnode(data,nodes.left_Child)

            else:
                nodes.left_Child = Node(data)

        elif data > nodes.datas:
                if nodes.right_Child is not None:
                    self.insertnode(data,nodes.right_Child)
                else: nodes.right_Child = Node(data)

        if data == nodes.datas:
            pass



    #call this for traverse
    def Traverse(self):
        if self.root:
            #change her for the type of traversal u want : in , pre , post
            return self.traverseInOrder(self.root)


    def traverseInOrder(self,nodes):

        if nodes.left_Child:
            self.traverseInOrder(nodes.left_Child)
        print(" %d " % nodes.datas)
        if nodes.right_Child:
            self.traverseInOrder(nodes.right_Child)

    def traversePreOrder(self,nodes):
        print (" %d " % nodes.datas)
        if nodes.left_Child:
            self.traversePreOrder(nodes.left_Child)
        if nodes.right_Child:
            self.traversePreOrder(nodes.right_Child)

    def traversePostOrder(self,nodes):
        if nodes.left_Child:
            self.traversePostOrder(nodes.left_Child)
        if nodes.right_Child:
            self.traversePostOrder(nodes.right_Child)
        print("%d" %nodes.datas)


    #call this for min value
    def getminValue(self):
        if self.root is not None:
            return self.getmin(self.root)

    def getmin(self,nodes):
        if nodes.left_Child is not None:
            return self.getmin(nodes.left_Child)

        return nodes.datas

    #call this for max value
    def getmaxValue(self):
        if self.root is not None:
            return self.getmax(self.root)

    def getmax(self,nodes):
        if nodes.right_Child is not None:
            return self.getmax(nodes.right_Child)
        return nodes.datas

    #call this to delete a data
    def nodedelete(self,data):
        if self.root is not None:
            self.root = self.removeNode(data,self.root)

    def removeNode(self,data,node):
        if not node:
            return node
        # finding the node to be removed
        if node.datas > data:
            node.left_Child = self.removeNode(data,node.left_Child)
        elif node.datas < data:
            node.right_Child = self.removeNode(data, node.right_Child)
        else:
            if not node.left_Child and not node.right_Child: #leaf node
                del node
                return None # to tel the parent node that the underlying node is none

            elif not node.left_Child  : #removing node with single right child and no left child
                temp = node.right_Child
                del node
                return temp

            elif not node.right_Child: #removing node with single left child and no right child
                temp = node.left_Child
                del node
                return temp

            else:
                tempnode = self.predecessor_node(node.left_Child)
                node.datas = tempnode.datas
                node.left_child = self.removeNode(tempnode.datas, node.left_Child)
        return node




    def predecessor_node(self,node):
        if node.right_Child:
            self.predecessor_node(node.right_Child)
        return node

















BinartTree = BinaryTree()
BinartTree.insert(32)
BinartTree.insert(55)
BinartTree.insert(10)
BinartTree.insert(1)
BinartTree.insert(19)
BinartTree.insert(16)
BinartTree.insert(23)
BinartTree.insert(79)



print("The max value is : %d" %BinartTree.getmaxValue())
print ("The min value is : %d" %BinartTree.getminValue())
BinartTree.Traverse()
print ("**********************************************")

BinartTree.nodedelete(32)
BinartTree.Traverse()











