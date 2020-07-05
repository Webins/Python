#existing dict
numbers = {
"first" : 1,
"second": 2,
"third": 3
}

squared = {key:value ** 2 for key, value in numbers.items()}
print(squared)

#creating a new dict
new = {num: num ** 2 for num in [1,2,3,4,5]}
print(new)

num_list = list(range(1, 50))
odd_even = {num: ("even" if num %2 == 0 else "odd") for num in num_list}
print(odd_even)
