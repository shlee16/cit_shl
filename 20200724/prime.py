# Prime



n = 2
print ("Prime Numbers are:")
while n < 1000:
    i = 2
    isPrime = True

    while i <= n and isPrime:
        if i == n:
            print (n)
        elif n % i == 0:
            isPrime = False
        i += 1

    n += 1

# #
# n = 2
# print ("Prime Numbers are:")
# while n < 1000:
#     i = 1
#
#     while i <= n:
#         if i == n:
#             print (n)
#             break
#         elif n % i == 0 and i != 1:
#             break
#         i = i + 1
#
#     n = n + 1
