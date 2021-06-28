def linear_search(Array,Key):
    pointer = 0
    while pointer < len(Array):
        if Key == Array[pointer]:
            return [True,pointer]
        else:
            pointer += 1
    return [False,"Not_Found"]

A = [45,78,35,97,6,18]
print(linear_search(A,6))
print(linear_search(A,100))