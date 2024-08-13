def chaicoder(num):
    def actual(x):
        return x ** num
    return actual
f = chaicoder(2)
print(f(3))
g = chaicoder(3)
print(g(3))