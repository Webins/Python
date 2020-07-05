nums = (88,89,94,112,333,44,112,1,20,223,4,5,6)

#sorted return a new collection without affecting the original one

print(sorted(nums))

#specify the order

print(sorted(nums, reverse=True))

#custom sorted

users =[ 
{"name": "Angel", "age": 22},
{"name": "Diana", "age": 17},
{"name": "Dayton", "age": 32},
{"name": "Clay", "age": 42},
{"name": "Rodrigo", "age": 24},
]

print(sorted(users, key=lambda x : x["age"]))


