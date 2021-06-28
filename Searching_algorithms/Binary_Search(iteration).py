def binary_search(Array, Key):
    low = 0
    high = len(Array)-1
    while low <= high :
        mid = (low + high) // 2
        if Array[mid] == Key:
            return [True,mid]
        elif Array[mid] > Key:
            high = mid - 1
        else:
            low = mid + 1
    return [False,"Not_found"]

# Sort the array before using Binary Search
A = [12,21,34,49,78,92]
print(binary_search(A,21))
print(binary_search(A,50))