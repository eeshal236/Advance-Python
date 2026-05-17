my_dict = {}
my_dict = {1 : 'Apple',2 : 'Ball'}

my_dict = {'Name':'Eeshal',1 : [2,4,6,8,10]}

my_dict = {'Name':'Anaya', 'Age':5}

print(my_dict['Name'])
print(my_dict.get('Age'))

my_dict['Age'] = 6
print(my_dict)

my_dict['address'] = 'Downtown'
print(my_dict)

my_dict.pop('Age')
print(my_dict)

print('address : ', my_dict.get('address'))

my_dict.clear()
print(my_dict)