def fibonacci():
    n = int(input("Digite o numero de termos da sequencia Fibonacci: "))
    a, b = 0, 1

    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

class Contador:
    def __init__(self):
        self.var = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.var += 1
        if self.var > 10:
            raise StopIteration
        return self.var

def main():
    fibonacci()

    cont = Contador()
    for c in cont:
        print(c)

if __name__ == "__main__":
    main()