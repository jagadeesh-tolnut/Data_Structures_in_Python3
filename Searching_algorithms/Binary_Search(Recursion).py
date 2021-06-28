def binary_search(Array, Key , low, high):
    if low > high:
        return [False,"Not_found"]
    else:
        mid = (low+high) // 2
        if Array[mid] == Key:
            return [True,mid]
        elif Array[mid] > Key:
            return binary_search(Array, Key , low, mid-1)
        else:
            return binary_search(Array, Key , mid+1, high)

A = [12,21,34,49,78,92]
print(binary_search(A,21,0,len(A)-1))
print(binary_search(A,50,0,len(A)-1))