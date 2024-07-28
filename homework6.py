my_dict = {'Polina': 2001, 'Sveta' :1961, 'Marina' :1978}
print(my_dict)
print(my_dict['Sveta'])
print(my_dict.get('Lena'))
my_dict.update({'Lena' : 1984, 'Arina': 1998})
print(my_dict)
k = my_dict.pop('Marina')
print(k)
print(my_dict)
my_set = {True, 1, 7, 19, 7, True, 'Home', ('a', 'b')}
print(my_set)
my_set.add(18)
my_set.add('a')
print(my_set.discard(True))
print(my_set)



