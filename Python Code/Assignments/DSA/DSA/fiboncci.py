class Fiboncci:

    def __init__(self):
        self.mydict = {}

    def fiboncci(self, n):
        if n == 1 or n == 2:
            return 1
        return self.fiboncci(n-1) + self.fiboncci(n-2)

    def fiboncci_dynamic(self, n):
        if n == 1 or n == 2:
            return 1
        if n in self.mydict:
            return self.mydict[n]
        self.mydict[n] = self.fiboncci_dynamic(n-1) + self.fiboncci_dynamic(n-2)
        return self.mydict[n]