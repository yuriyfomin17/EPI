import bisect
import copy


def create_2d_array():
    array_2d = [[0 for _ in range(3)] for _ in range(3)]
    print(array_2d)
    array_2d = [[0] * 3 for _ in range(3)]
    print(array_2d)


def copying_array():
    B = [0, 1, 2, 3]
    A = B
    B[0] = -1
    # [-1, 1, 2, 3]
    print(B)
    # [-1, 1, 2, 3]
    print(A)

    A = list(B)
    A[0] = 0

    # [-1, 1, 2, 3]
    print(B)
    # [0, 1, 2, 3]
    print(A)

    B = [[0, 1], [2, 3]]
    A = copy.copy(B)
    B[0][0] = -1

    # [[-1, 1], [2, 3]]
    print(B)
    # [[-1, 1], [2, 3]]
    print(A)

    B = [[0, 1], [2, 3]]
    A = copy.deepcopy(B)

    B[0][0] = -1
    # [[-1, 1], [2, 3]]
    print(B)
    # [[0, 1], [2, 3]]
    print(A)

    B = [[0, 1], [2, 3]]
    A = B[:]
    B[0][0] = -1
    # [[-1, 1], [2, 3]]
    print(B)
    [[-1, 1], [2, 3]]
    print(A)

    B = [[0, 1], [2, 3]]
    A = [el[:] for el in B]

    B[0][0] = -1
    # [[-1, 1], [2, 3]]
    print(B)
    # [[0, 1], [2, 3]]
    print(A)



def sort_dependant_python_functions():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    neededElement = 5
    indexOfElementToInsertToKeepListSorted = bisect.bisect(arr1, neededElement)
    print(indexOfElementToInsertToKeepListSorted)

    bisect.insort(arr1, neededElement)
    print(arr1)

    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    indexOfElementBefore = bisect.bisect_left(arr2, neededElement)
    print(indexOfElementBefore)

    indexOfElementAfter = bisect.bisect_right(arr2, neededElement)
    print(indexOfElementAfter)


def perform_sorting_reversing_of_arr():
    arr = [1, 2, 3, 4, 5, 6]
    arr.reverse()
    print(arr)

    arr2 = [1, 2, 3, 4, 5, 6]
    arr3 = list(reversed(arr2))
    print(arr3)

    arr4 = [7, 2, 1, 2, 10, 9]

    arr4.sort()
    print(arr4)

    arr5 = [7, 2, 1, 2, 10, 9, 8]
    print(sorted(arr5))

def deletion_of_arr():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    del arr[5]
    print(arr)

    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(arr2[3:7])

def reversing_arr():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 9, 8, 7, 6, 5
    print(arr[-2: -7: -1])
    # [2, 3, 4, 5, 6]
    print(arr[2: 7: 1])
    # [2, 4, 6]
    print(arr[2: 7: 2])
    # 7, 6, 5, 4, 3
    print(arr[7: 2: -1])
    # [7, 5, 3]
    print(arr[7: 2: -2])
    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(arr[::-1])

    # rotate array by 4 items
    print(arr[4:] + arr[:4])

def array_manipulation():
    A = [1, 3, 5]
    B = ['a', 'b']
    product_set = [(x, y) for x in A for y in B]
    print(product_set)

    M = [['a', 'b', 'c'], ['d', 'e', 'f']]
    # flattening of array
    print([x for row in M for x in row])

    M = [[1, 2, 3], [4, 5, 6]]
    # squaring array
    print([[x**2 for x in row] for row in M])

array_manipulation()
