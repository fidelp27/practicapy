def fizzBuzz(n):
    for i in range(1, int(n)+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        elif i % 3 != 0 and i % 5 != 0:
            print(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)


def getMinimumOperations(executionTime, x, y):
    n = len(executionTime)
    operations = 0
    while len(executionTime) > 0:
        max_time = max(executionTime)
        executionTime = [time - y if time !=
                         max_time else time - x for time in executionTime]
        executionTime = [time for time in executionTime if time > 0]
        operations += 1
    return operations
