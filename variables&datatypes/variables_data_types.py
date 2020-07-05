#Variable declaration in python is 'naming'
#naming or assigment 

#data types : bool, int, string, list, dict

a = 15 #integer
b = 12
c = b + a
one, two, three = 1, 2, 3
string = 'This is a string' #string
float_var = 45.67 #floating point variable
complex_var = 3.14J #complex 
boolean_var = True #boolean
my_list= [1,2,3] #list
first_str = 'first'
second_str = "second"
third_str = '"third"'
all_str = first_str + '\n' + second_str  +  '\n' + third_str
print(all_str)

#casting
floating = float(a)
string = str(a)
list_to_str = str(my_list)
print(f"{floating}\t {string}\t {list_to_str}")


#python is a no typed language. is dynamic

is_string = 'Another string'
print(boolean_var)
print(type(boolean_var))
boolean_var = is_string
print(boolean_var) 
print(type(boolean_var))
#change the type

boolean_var = None
print(boolean_var)
print(type(boolean_var))


#formatted string
boolean_var = False

#python 3
print(f'What i\'ve said is {boolean_var}')

#python 2
print('What i\'ve said is {}'.format(boolean_var))

#old
print('What i\'ve said is %r' % (boolean_var))

print(f'Accessing the first letter of is_string: {is_string[0]}')
print(f'Accessing the Last letter of is_string: {is_string[-1]}')
