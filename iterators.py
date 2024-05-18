def give_fibonacci(previous, current):

    while True:
        next = previous+current
        yield next
        previous = current
        current = next

fib = give_fibonacci(0,1)
print('0')
print('1')
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

