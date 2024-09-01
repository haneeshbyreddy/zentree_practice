class Helper:
    def __init__(self):
        pass
    def transpose(self, A):
        m, n = len(A), len(A[0])
        ans = []
        for i in range(n):
            arr = []
            for j in range(m):
                arr.append(A[j][i])
            ans.append(arr)
        return ans
    def matrixMult(self, A, B):
        m, n = len(A), len(A[0])
        if len(B) != n:
            B = self.transpose(B)
            print("B is transposed now", "A :", [len(A), len(A[0])], "B :", [len(B), len(B[0])])
        ans = []
        for i in range(m):
            arr = []
            for j in range(n):
                var = 0
                for k in range(n):
                    var += A[i][k] * B[k][j]
                arr.append(var)
            ans.append(arr)
        return ans

h1 = Helper()
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
# A = [[1,2,3],[4,5,6]]
# B = [[7,8],[9,10],[11,12]]

# A transpose
print("A transpose of", A)
A_T = h1.transpose(A)
print(A_T)

# A * B
print("matrix multiplication of", A, "and", B)
A_mult_B = h1.matrixMult(A, B)
print(A_mult_B)
