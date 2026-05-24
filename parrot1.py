class parrot:
    speices = "Bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age

ob = parrot("Blue",10)
ob2 = parrot("Woo",9)
#Printing
print(ob.name)
print(ob2.name)
print(ob.age)
print(ob2.age)
print(ob.speices)
print(ob2.speices)