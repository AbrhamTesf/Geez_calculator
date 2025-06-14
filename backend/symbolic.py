class Expr:
    def __add__(self, other):
        return Add(self, other)
    
    def __mul__(self, other):
        return Mul(self, other)
    
    def __pow__(self, other):
        return Pow(self, other)

class Const(Expr):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Symbol(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Add(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} + {self.right})"

class Mul(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} * {self.right})"

class Pow(Expr):
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def __str__(self):
        return f"({self.base}^{self.exponent})"
