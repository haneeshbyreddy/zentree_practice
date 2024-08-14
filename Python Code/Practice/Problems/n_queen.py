import copy

n = 8
matrix = [[0]*n for _ in range(n)]
ans_arr = [0]*n

def mark(row, col, input_matrix):
    for i in range(n):
        input_matrix[row][i] = 1
        input_matrix[i][col] = 1

    for i in range(n):
        if 0 <= row + i < n and 0 <= col + i < n:
            input_matrix[row + i][col + i] = 1
        if 0 <= row - i < n and 0 <= col - i < n:
            input_matrix[row - i][col - i] = 1
        if 0 <= row + i < n and 0 <= col - i < n:
            input_matrix[row + i][col - i] = 1
        if 0 <= row - i < n and 0 <= col + i < n:
            input_matrix[row - i][col + i] = 1

def n_queen(row, matrix):
    if row>=len(matrix):
        return True
    for i in range(len(matrix[0])):
        if matrix[row][i] == 0:
            temp = copy.deepcopy(matrix)
            mark(row, i, temp)
            if n_queen(row+1, temp):
                return True
    return False 

print(n_queen(0, matrix))