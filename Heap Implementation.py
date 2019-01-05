CAPACITY = 10
class Heap:
    def __init__(self):
        self.heap = [0]*CAPACITY
        self.size = 0

    #use this method to insert a data
    def insert(self,data):
        if self.size == CAPACITY:
            return
        self.heap[self.size] = data
        self.size =self.size+1
        self.fix_heap(self.size-1)


    # arrange heap acc to property
    def fix_heap(self,index):
        parent_index = (index - 1)//2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index,parent_index)
            self.fix_heap(parent_index)

    def swap(self,index1,index2):
        self.heap[index2],self.heap[index1] = self.heap[index1],self.heap[index2]


    def getmax(self):
        return self.heap[0]

    def poll(self):
        max = self.getmax()
        self.swap(0,self.size-1)
        #del self.heap[self.size -1]
        self.size = self.size-1
        self.fix_down(0)
        return max
    # to remove violations in downward direction
    def fix_down(self,index):
        left_index = 2*index + 1
        right_index = 2*index + 2

        large_value_index = index
        if left_index < self.size and self.heap[large_value_index] < self.heap[left_index]:
            large_value_index = left_index
        if right_index < self.size and self.heap[large_value_index] < self.heap[right_index]:
            large_value_index = right_index
        if index != large_value_index:
            self.swap(index,large_value_index)
            self.fix_down(large_value_index)


    def heap_sort(self):
        size = self.size
        for i in range(0,size):
            max =self.poll()
            print (max)
















if __name__ == "__main__":
    Heap = Heap()
    Heap.insert(10)
    Heap.insert(12)
    Heap.insert(1)
    Heap.insert(19)
    Heap.insert(0)

    Heap.heap_sort()


