class MyClass:
    def __init__(self, L):
        self.L = L

    def odds(self):
        t = []
        try:
            for i in range(1,len(self.L),2):
                t.append(self.L[i])
        except:
            pass
        return t

    def oddsPlusC(self, c):
        return [i+c for i in self.odds()]
