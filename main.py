
class A:
    _MUL = 10
    
    def __init__(self, n) -> None:
        self.n = n
        
    def mult(self, x=None):
        self.n = self.n * x if x else self.n * self._MUL

        
class B(A):
    _SUM = 0
    
    def __init__(self, n) -> None:
        super().__init__(n)
        
    def suma(self, x=None):
        return self.n + x if x else self.n + self._SUM