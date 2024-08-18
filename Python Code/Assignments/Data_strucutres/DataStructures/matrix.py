class Matrix:
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