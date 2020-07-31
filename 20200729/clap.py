# # 3 6 9 13 16 19 23 26 29 30 31 32 33 333

n = 1

while n < 3000 :
    digit = 1
    clap = 0

    while  n > 10 ** (digit-1) :
        digitNumber = ( n % (10 ** digit) - n % (10 ** (digit - 1))  )/ 10 ** (digit - 1)
        if ( digitNumber % 3 == 0 and digitNumber != 0):
            clap += 1
        digit += 1


    if clap == 0 :
        print(n)
    else :
        claps = ""
        while (clap > 0 ):
            claps += "clap "
            clap -= 1
        print(claps)

    n += 1

#
# count = 1
# #
# # r = 0
# # n = 10 * r
# #
# # i = count + n
#
# a = count * (1 / 10)
# n = 10 * a
#
# count < n
#
# while count < 100 :
#     if count == 3 :
#         print ('clap' )
#     elif count == 6 :
#         print ('clap')
#     elif count == 9 :
#         print ('clap')
#     elif count % n == 3 :
#         print ('clap')
#     elif count % n == 6 :
#         print ('clap')
#     elif count % n == 9 :
#         print ('clap')
#     elif count  == 3 :
#         print ('clap' * b )
#
#     # if count + n == n + 3:
#     #     print ('clap')
#     # elif count + n == n + 6:
#     #     print ('clap')
#     # elif count + n == n + 9:
#     #     print ('clap')
#
#
#
#     count = count + 1
#     # r = r + 1
