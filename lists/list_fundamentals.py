#create a list
my_list = [1, "one", 1.00, "1"]
number_list = list(range(1, 4))
slicing_list = [10,20,30,40,50,60,70,80,90,100]


#calculate the lenght
print(f"My list length: {len(my_list)}") 

#methods
number_list.append(4) #single item to the end of the list
number_list.extend([5,6,7,8,9,10]) #multiples items to the end of the list
number_list.insert(0, 0) #insert a item at a given position

number_list.index(6) #returns the index of a specified item
number_list.index(6, 4) #start from index 4
number_list.index(6, 4, 8) #start from index 4 and end on index 8
number_list.count(1) #return the number of times that and value appears on the list
number_list.reverse() #reverse the lists
number_list.sort() # sort the list in asc

item_removed = number_list.pop(0) #return and delete the item at pos 0
item_remove2 = number_list.pop() #return and delete the last item
number_list.remove(8) # remove the first item from the list whose value is x and thrown a value error is the item is not found
number_list.clear() #remove all items

#slicing
print(slicing_list[1:]) #from index 1
print(slicing_list[-3:]) #from the end -2
print(slicing_list[:3]) # from the end
print(slicing_list[1:4]) #from 1 to 4
print(slicing_list[1:8:2]) #step of 2
print(slicing_list[4::2]) #without end point

#swapping values
names = ['James', 'Michelle']
names[0] , names[1] = names[1], names[0]

#accessing values
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])

#check for a value
print(1 in number_list)
print("one" in my_list)
