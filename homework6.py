my_dict = {'Nadia': '2008', 'Dasha': '2010', 'Marina': '2007'}
print(my_dict)
print(my_dict['Nadia'])
print(my_dict.get('Dima'))
my_dict.update({'Vitia': '1889',
                'Vadim': '1884'})
x = my_dict.pop('Marina')
print(x)
print(my_dict)

my_set = {1, 2, 3, 2, 1, 'cat', 'a', 'a', True, False, False}
print(my_set)
my_set.add(5)
my_set.add('dog')
my_set.remove('a')
print(my_set)
