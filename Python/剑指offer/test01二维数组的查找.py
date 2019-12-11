def Find(target, array):
    # write code here
    row = len(array)
    col = len(array[0])
    i = 0
    j = col - 1
    while i < row and j >= 0:
        if target < array[i][j]:
            j = j - 1
        elif target > array[i][j]:
            i = i + 1
        else:
            return True
    return False


array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
target = 7
# row = len(array)
# col = len(array[0])
# print(row, "  ", col)
print(Find(target, array))
