class parrot:
    speices = "Bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sing(self):
        print("I am a parrot I can sing")
    def dance(self):
        print("I am a parrot I can Dance")
ob = parrot("Coco",8)
ob2 = parrot("Kiwi",11)
print("My species is ",ob.speices)
print("My name is ",ob.name,"and my age is ",ob.age)
print("My species is ",ob.speices)
print("My name is ",ob2.name,"and my age is ",ob2.age)
