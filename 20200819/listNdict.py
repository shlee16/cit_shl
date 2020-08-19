a = [1, 5, "jerry", True, 9]

print(a[0] + a[1])

a[1] = "Tom"
a[0] = a[0] + 9

print(a)
print(len(a))
a.append(False)
print(a)


b = {"name" : "Tom", "age" : 19, "isMarried" : True}
c = {"name" : "Jane", "age" : 29, "isMarried" : False}
print(c["age"] + 10)
# c["isMarried"] = True
c["isMarried"] = not (c["isMarried"])

print(c)
