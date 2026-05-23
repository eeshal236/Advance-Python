#Empty Tuple
my_tuple = ()
print(my_tuple)

#Tuple having integers
my_tuple = (3,7,9)
print(my_tuple)

#Tuple with mixed datatypes
my_tuple = ("Hello", 4.5, 6)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8,6,9], (4,5,7))
print(my_tuple)

#Accessing tuple elements using indexing
my_tuple = ("p","e","r","m","i","t")
print(my_tuple[0])
print(my_tuple[5])

#nested tuple
n_tuple = ("mouse", [8,6,9], (4,5,7))

#nested index
print(n_tuple[0][3])
print(n_tuple[1][1])

#slicicing
print("Sliced : ",my_tuple[1:4])

#Iterating through tuple
for letter in (my_tuple):
    print("Hello", letter)