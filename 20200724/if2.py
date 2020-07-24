tier = False
rating = 4570

if (5000 < rating or 0 > rating): # Invalid filter
    tier = "invalid"
elif (rating < 1500):
    tier = "bronze"
elif (rating < 2000):
    tier = "silver"
elif (rating < 2500):
    tier = "gold"
elif (rating < 3000):
    tier = "platinum"
elif (rating < 3500):
    tier = "diamond"
elif (rating < 2000):
    tier = "master"
else:
    tier = "GM"

print(tier)




#
# if( 5000 > rating and rating > 4000 ):
#     print('GrandMaster')
# elif(3999 > rating and rating > 3500) :
#     print('master')
# elif( 3499 > rating and rating > 3000) :
#     print('dia')
# elif(2999 > rating and rating > 2500) :
#     print('plat')
# elif(2499 > rating and rating > 2000) :
#     print('gold')
# elif(1999 > rating and rating > 1500) :
#     print('silver')
# elif(0 < rating < 1500) :
#     print('bronze')
# else:
#     print('invalid')



# rating = -500
#
# if(rating > 4000 ):
#     print('GrandMaster')
# elif(rating >= 3500) :
#     print('master')
# elif(rating > 3000) :
#     print('dia')
# elif(rating > 2500) :
#     print('plat')
# elif(rating > 2000) :
#     print('gold')
# elif(rating > 1500) :
#     print('silver')
# # elif(rating < 1500) :
# else:
#     print('bronze')
