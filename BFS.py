class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjancent_list = []
        self.visited = False
        self.predecessor  = None

class BFS(object):
    def bfs(self,startnode):
       queue = []
       queue.append(startnode)
       startnode.visited = True

       while queue:
           actualnode = queue.pop(0)
           print(' %s '% actualnode.name)
           for n in actualnode.adjancent_list:
               if not n.visited:
                   queue.append(n)

node1 = Node('A')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
node5 = Node('e')
node6 = Node('f')
node7 = Node('g')



node1.adjancent_list.append(node2)
node1.adjancent_list.append(node3)
node2.adjancent_list.append(node4)
node4.adjancent_list.append(node5)


bfs = BFS()
bfs.bfs(node1)










