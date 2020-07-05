#zip combine two or more collection base on the index
#if the two collections are not equally in size, then it will discard the most greatest values in terms of lenght

nums1 = [1,2,3,4,5,6]
nums2 = [7,8,9,10,11, 12]

zip_nums = list(zip(nums1, nums2))
print(zip_nums) #[(1, 7), (2, 8), (3, 9), (4, 10), (5, 11), (6, 12)]

print(*zip_nums) # unpacking1 (1, 7) (2, 8) (3, 9) (4, 10) (5, 11) (6, 12)

names = ['James', 'Pedro', 'Carolina', 'Andrea', 'John']

print(list(zip(names, nums1, nums2))) # [('James', 1, 7), ('Pedro', 2, 8), ('Carolina', 3, 9), ('Andrea', 4, 10), ('John', 5, 11)]


midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

#dict comprehension
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades)


