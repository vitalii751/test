
class A:
    _MUL = 10
    
    def __init__(self, n) -> None:
        self.n = n
        
    def mult(self, x=None):
        self.n = self.n * x if x else self.n * self._MUL

        
class B(A):

    def __init__(self, n) -> None:
        super().__init__(n)
        
    def suma(self, x):
        return self.n + x