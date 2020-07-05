#create dictionaries
book = {
"title": "Cronicas de una muerte anunciada",
"author": "Gabriel Garcia Marquez",
"year": "1999",
"ISBN": "2244E40"
}

book2 = dict(
title = "Cronicas de una muerte anunciada",
author = "Gabriel Garcia Marquez",
year = "1999",
ISBN = "2244E40")

print(book)
print(book2)

#accessing individual values

print(book["title"])
try:
	print(book["edition"])
except KeyError:
	print("That key doesnt exist")

print(book.get('title'))
print(book.get('edition')) #None instead of KeyError


#accessing all values and keys
for key in book.keys():
	print(key)
	
for value in book.values():
	print(value)
	
for key,value in book.items():
	print(key,value)
	

#check for a key
print("title" in book)
print("edition" in book)

#check for a value
print ("1999" in book.values())


#methods
book2.clear() #clear the dict
book2 = book.copy() #make a copy

#default dictionaries
book2 = dict.fromkeys(['title', 'author', 'year', 'edition', 'ISBN'], 'Unknown')
print(book2)

book2.pop('edition') #remove edition
print(book2)
book2.popitem() #remove a random key(last key)
print(book2)
book2.update(book) 
print(book2)







