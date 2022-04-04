class ArraySort:
    @staticmethod
    def __swap(arr, a, b):
        t = arr[a]
        arr[a] = arr[b]
        arr[b] = t

    @staticmethod
    def __partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i+=1
                ArraySort.__swap(arr, i, j)
        
        ArraySort.__swap(arr, i + 1, high)
        return (i+1)

    @staticmethod
    def sort(arr, low, high):
        if low < high:
            pi = ArraySort.__partition(arr, low, high)
            ArraySort.sort(arr, low, pi - 1)
            ArraySort.sort(arr, pi + 1, high)


class BusTerminal:
    def __init__(self, seats, size):
        self.seats = seats
        self.size = size
        
    def __canPlace(self, p, sep):
      placed = 1
      last = self.seats[0]

      for i in range(1, self.size):
        seat = self.seats[i]; 
        if (seat - last >= sep):
          placed+=1
          last = seat
          if (placed == p):
            return True 

      return False 

    def __maxDistance(self, p):
        ArraySort.sort(self.seats, 0, self.size-1)
        res = 0
        start = 0
        end = self.seats[self.size - 1] - self.seats[0]

        while start <= end:
            mid = start + ((end - start) / 2)

            # Can passengers be placed in a way that min distance
            # between any two passengers is at least mid?
            if self.__canPlace(p, mid):
                res = mid
                start = mid + 1
            else:
                end = mid - 1

        return res
    
    def canTransport(self, q, d):
        p = q
        while True:
            m = self.__maxDistance(p)
            if (m<d):
                p -= 1
            if m<d and p>0:
                break
            
        return p


class App:
    def __printArray(self, arr, size):
        for i in range(0, size):
            print(str(arr[i]) + " ", end="")
        print("\n")

    def processQueue(self, seats, n, q=10, dist=2):
        term = BusTerminal(seats, n)
        print("Bus Terminal:"); print(q, end="")
        print(" passengers queueing for ", end="")
        print(n, end=""); print(" seats...")
        
        p = term.canTransport(q, dist)
        print("Free Seats: ", end="")
        self.__printArray(seats, n)
        
        print("Transporting ", end=""); print(p, end="")
        print(" passengers (required distance ", end="")
        print(dist, end=""); print(")")


if __name__ == "__main__":
    seats = [3, 2, 8, 1, 9, 6, 12, 10, 13, 15, 16, 4, 21]
    app = App()
    app.processQueue(seats, len(seats))
