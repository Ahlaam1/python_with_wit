def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))


odd_nums = filter(lambda num : num % 2 != 0, numbers)

from functools import reduce


numbers = [1,2,3,4,5,1]
total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)

def sum_total(a, b): return a + b
print(sum_total(10, 8))

