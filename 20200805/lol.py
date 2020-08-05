class Champion():
    # name = "someChamp"
    # APcoeefficent = 0
    # isAlive = True
    def __init__(self, a, b):
        self.name = a
        self.APcoeefficent = b
        self.isAlive = True


    def APItem(self, AP):
        return ("This Item grants me +" + str(self.APcoeefficent * AP)  + "AP Damage")

    def teamfight (self):
        if self.isAlive :
            print(self.name + "survived!" )
        else :
            print(self.name + "is dead.")

a = Champion ('ahri', 0.5)
b = Champion ('Kayle', 0.2)
c = Champion ('Teemo', 1)

# ahri = Champion()
# Kayle = Champion()
# Teemo = Champion()
#
# ahri.name = "ahri"
# Kayle.name  ="Kayle"
# Teemo.name = "Teemo"
#
# ahri.APcoeefficent = 0.5
# Kayle.APcoeefficent = 0.2
# Teemo.APcoeefficent = 1

print (a.APItem(240))
c.isAlive = False
c.teamfight()


#property 3 method 2
# class Champion () :
#     name = 'aatrox'
#
#     def sayHi(self, attack ):
#         print (self.name, attack , 'teemo')
#
# a = Champion ()
# b = Champion ()
#
# b.name = "ahri"
#
# a.sayHi ('kill')
# b.sayHi ('damage')
#
# print (a.name)
# print (b.name)
