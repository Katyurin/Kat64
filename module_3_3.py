
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(10)
print_params(10, 'text')
print_params(10, 'text', False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [3.14, 'hello', False]
values_dict = {'a': 42, 'b': 'world', 'c': None}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
