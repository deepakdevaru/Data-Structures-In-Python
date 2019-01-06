class Nodes(object):
    def __init__(self,character):
        self.character = character
        self.rightNode = None
        self.leftNode = None
        self.middleNode = None
        self.value = 0


class TernaryTree:
    def __init__(self):
        self.rootNode = None

    def insert(self,key,value):
        self.rootNode =  self.putItem(self.rootNode, key,value, charIndex=0)


    def putItem(self, node ,key, value, charIndex):
        char = key[charIndex]
        if node == None:
            node = Nodes(char)
        if char < node.character:
            node.leftNode = self.putItem(node.leftNode,key,value,charIndex)
        elif char > node.character:
            node.rightNode = self.putItem(node.rightNode,key,value,charIndex)
        elif charIndex < len(key) -1:
            node.middleNode = self.putItem(node.middleNode,key,value,charIndex+1)
        else:
            node.value = value
        return node

    def get(self,key):
        node = self.getItem(self.rootNode,key, charIndex=0)
        if node == None:
            return -1
        return node.value


    def getItem(self,node,key,charIndex):
        char = key[charIndex]
        if node == None:
            return None
        if char < node.character:
            return self.getItem(node.leftNode,key,charIndex)
        elif char > node.character:
            return self.getItem(node.rightNode,key,charIndex)
        elif charIndex < len(key)-1:
            return self.getItem(node.middleNode,key,charIndex+1)
        else:
            return node


if __name__ == "__main__":
    ternaryTrees = TernaryTree()
    ternaryTrees.insert("cat",64)
    ternaryTrees.insert("camel", 46)
    ternaryTrees.insert("rat", 8)
    ternaryTrees.insert("tom", 6)
    ternaryTrees.insert("abstract",90)

    print(ternaryTrees.get("tom"))












