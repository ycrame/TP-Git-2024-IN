import sys

def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = fibonnaci(n-1) + fibonnaci(n-2)
        return fib

def main(argv):
    print(fibonnaci(int(argv[1])))

if __name__ == "__main__":
    main(sys.argv)
