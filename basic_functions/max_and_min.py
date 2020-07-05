names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

songs = [
{"title": "After Hours", "playcount": 5555154},
{"title": "Snowchild", "playcount": 4641555},
{"title": "Repeat After Me", "playcount": 3555158},
{"title": "The Hills", "playcount": 120561132},
{"title": "King Of The Fall", "playcount": 6647050},
{"title": "Often", "playcount": 125467100}
]

print(max(names, key = lambda n: len(n)))
print(min(names, key = lambda n: len(n)))
print(max(songs, key = lambda s: s["playcount"]))
print(min(songs, key = lambda s: s["playcount"]))
