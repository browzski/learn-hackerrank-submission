def factorial(n):
    if(n==1):
        return 1
    prod = n*factorial(n-1)
    return prod

if __name__ == "__main__":
    n = int(input().strip())
    print(factorial(n))
