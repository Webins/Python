import sys

square_lambda = lambda num: num * num

print(square_lambda(2))

nums = (878.8,7878,787,5565,6121,222)

doubles = tuple(map(lambda x: x*2, nums))

print(doubles)

names = [
{"first": "pedro", "last":"gonzales", "age":22},
{"first": "juan", "last":"torres", "age":27},
{"first": "leo", "last":"martinez", "age":18},
{"first": "maria", "last":"santana", "age":19},
{"first": "jay", "last":"rodriguez", "age":25}
]

#map
print(tuple(map(lambda x: x['first'].upper(), names)))

#filter
print(tuple(filter(lambda x: x['age'] >= 20, names)))

#combinin filter and map
print(tuple(map(lambda x: x['first'].upper(), filter(lambda x: x['age'] >= 20, names))))

#list comprehension
print(tuple([f"{name['first'].upper()}" for name in names if name['age'] >= 20]))


#list comprehension vs generator expression
list_comp = [num % 2 == 0 for num in [5,6,0,12,11,44,56,878,87,11,44,4,466,6,54,7,8,412,21,2,4,45,87]]
gen_exp = (num % 2 == 0 for num in [5,6,0,12,11,44,56,878,87,11,44,4,466,6,54,7,8,412,21,2,4,45,87])

#calculate the size
print(f"List compresion size : {sys.getsizeof(list_comp)} bytes")
print(f"Generator expression size : {sys.getsizeof(gen_exp)} bytes")

#all return true if all elements on a list are true

print(all(list_comp)) #False


#any return true if at least one element is true

print(any(gen_exp)) #True
