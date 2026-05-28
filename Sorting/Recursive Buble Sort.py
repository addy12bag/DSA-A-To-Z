class Bubblesort:
    def __init__ (self,arr):
        self.arr = arr
        self.length = len(arr)
    def __str__(self):
        return " ".join([str(x) for x in self.arr])
    
    def recusive_bubble_sort(self,n =None):
        if n == None:
            n = self.length
        if n ==1:
            return
        count = 0
        for i in range(n-1):
            if self.arr[i]>self.arr[i+1]:
                self.arr[i],self.arr[i+1] = self.arr[i+1],self.arr[i]
                count +=1
        if count == 0:
            return
        
        self.recusive_bubble_sort(n-1)


def main():
    arr = [64,34,25,12,22,11,90]
    bs = Bubblesort(arr)
    bs.recusive_bubble_sort()
    
    print("Sorted array is ;",bs)

if __name__ == "__main__":
    main()
