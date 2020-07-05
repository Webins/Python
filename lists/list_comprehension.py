nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums_multiplied = [x*10 for x in nums] #for every x(value) in the list nums, multiply by 10
nums_divided = [num * 2 if num %2 == 0 else num/2 for num in nums]

evens = [num for num in nums if num % 2 == 0]
odds = [num for num in nums if num % 2 != 0 ]
print(nums_multiplied)
print(nums_divided)
print(evens)
print(odds)


#nested list comprehension
# doesnt work board = [[for num in range(1,4) if num %2 == 0 "X" else "O"] for val in range(1,4)]
board = [["X" if num %2 == 0 else "O" for num in range(1,4)] for val in range(1,4)]
print(board)
