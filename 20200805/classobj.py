class Person () :
    # name = 'steve' #property
    def __init__(self, a,b,c,d):
        self.name = a
        self.race = b
        self.height = c
        self.age = d

    def sayHi(self, greeting): #method
        print (greeting + ", " + self.name)

class Professor(Person):
    def __init__(self, a,b,c,d, p1, p2):
        self.name = a
        self.race = b
        self.height = c
        self.age = d
        self.salary = p1
        self.phD = p2

    def introduce(self):
        print("I got my phD at " + self.phD)

class Student(Person):

    def __init__(self, s1, s2, s3, s4, s5, s6):
        Person.__init__(self, s1, s2, s3, s4)
        self.age = s4 + 1
        self.dorm = s5
        self.studentId = s6

# a = Person()
# b = Person()
# b.name = 'tom'

a = Person("John", "Asian", 135, 87)
a.height = 152
b = Person("Sam", "White", 234, 122)
c = Professor("Daniel", "Black", 185, 77, 10000, "Stanford" )
d = Student("Karen", "Mexican", 160, 63, "West", "assd232141")

d.sayHi("Hey ")
c.sayHi("Hello Class")

a.sayHi ("Hello")
b.sayHi ("Howdy")

print(a.age)
print(a.height)
print(b.race)
