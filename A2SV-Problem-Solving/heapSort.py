class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here

        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)    

    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
