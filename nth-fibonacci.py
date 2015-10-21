# 0,1,1,2,3,5

# def fib(n):
#     # fib_array = []
#     # fib_array[i] = fib_array[i-1] + fib_array[i-2]
#     if n == 0 or n == 1:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(3))

def fib(n):
    if n < 0:
        raise Exception("Index was negative")

    elif n in [1,0]:
        return n

    prev = 0
    prev_prev = 1

    for _ in range(n):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    return current

print(fib(4))
