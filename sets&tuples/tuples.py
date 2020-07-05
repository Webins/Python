#creating a tuple
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

#month2 = tuple('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

#accessing a tuple
for month in months:
	print(month)
	
print(month[0])


#methods
print(months.count('February')) #return the number of times a value appears in a tuple
print(months.index('June')) #return the index at wich a value is found in a tuple

#tuples in dictionaries

locations = {
(35.8887,874,5545): "Tokyo Office",
(74.588,56.778): "Paris office"
}


#nested tuples
tuples = ((1,2,3,4), (5,6,7,8), (9,10,11,12))

