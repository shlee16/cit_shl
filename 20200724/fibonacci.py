# Fibonacci Sequence 1 1 2 3 5 8 13 21

first = 1
second = 1
limit = 1000000

print(first)
print(second)

while limit > second :
    steve = first
    first = second
    second = steve + second
    print(second)
