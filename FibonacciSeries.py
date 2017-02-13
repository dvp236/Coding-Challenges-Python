
# "Swaminarayan!!"

# using normal recursion
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(10)



# using dynamic approach
def fib_dynamic(n):
    result = [None] * (n+1)
    fib_helper(n,result)
    print result[n]
    # for i in result:
    #     print i


def fib_helper(n,result):
    if n <= 1:
        result[n] = n
        return result[n]
    else:
        if result[n] != None:
            return result[n]
        result[n] = fib_helper(n-1,result)+fib_helper(n-2,result)
    return result[n]


fib_dynamic(10)
