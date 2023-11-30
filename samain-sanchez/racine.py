import sys

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def main(argv):
    print(fact(int(argv[1])))

if __name__ == "__main__":
    main(sys.argv)
