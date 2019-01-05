SIZE= 10
class Heaps:
    def __init__(self):
        self.heap = [0]*SIZE
        self.size = 0

    def insert(self,data):
        if self.size == SIZE:
            return
        self.heap[self.size]=data
        self.size+=1
        self.check(self.size-1)


    def check(self,index):
        parent_index = (index-1)//2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.swap(index,parent_index)
            self.check(parent_index)

    def getmin(self):
        return self.heap[0]

    def getmax(self):
        return self.heap[self.size-1]

    def poll(self):
        min = self.getmin()
        self.swap(0,self.size-1)
        self.size -= 1 #decrement and remove the last item
        self.check_down(0)

        return min

    def check_down(self,index):
        left_index = 2*index +1
        right_index = 2*index +2

        smallest_val_index = index
        if left_index < self.size and self.heap[left_index] < self.heap[smallest_val_index]:
            smallest_val_index= left_index
        if right_index < self.size  and self.heap[right_index] < self.heap[smallest_val_index]:
            smallest_val_index= right_index
        if index != smallest_val_index:
            self.swap(index,smallest_val_index)
            self.check_down(smallest_val_index)

    def heap_sort(self):
        if self.heap:
            for i in range(0,self.size):
                print (self.poll())



    def swap(self,index1,index2):
        self.heap[index1], self.heap[index2] = self.heap[index2],self.heap[index1]



if __name__ == "__main__":
    Heap = Heaps()
    Heap.insert(10)
    Heap.insert(12)
    Heap.insert(-1)
    Heap.insert(19)
    Heap.insert(80)


    print ("min: ",Heap.getmin())
    print ("max :", Heap.getmax())
    Heap.heap_sort()
