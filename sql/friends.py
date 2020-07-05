import sqlite3

conn = sqlite3.connect('friends.db')

# create cursor object
c = conn.cursor()

# execute some sql

# create table
c.execute('CREATE TABLE friends(name TEXT, closeness INTEGER)')

# insert 
peoples = [
    ("John", 5),
    ("Maria", 4),
    ("Jesus", 8),
    ("Alexa", 6),
    ("Pedro", 3),
    ("Jhonathan", 8),
    ("Bob", 9),
    ("Lewis", 2),
    ("Efrain", 3)
]

c.executemany("INSERT INTO friends VALUES (?,?)", peoples)

# c.execute('INSERT INTO friends VALUES("John", 5)')
# c.execute('INSERT INTO friends VALUES("Maria", 4)')
# c.execute('INSERT INTO friends VALUES("Jesus", 8)')
# c.execute('INSERT INTO friends VALUES("Alexa", 6)')
# c.execute('INSERT INTO friends VALUES("Pedro", 3)')
# c.execute('INSERT INTO friends VALUES("Jhonathan", 8)')
# c.execute('INSERT INTO friends VALUES("Bob", 9)')
# c.execute('INSERT INTO friends VALUES("Lewis", 2)')
# c.execute('INSERT INTO friends VALUES("Efrain", 3)')

# select
friends = c.execute('SELECT * FROM friends WHERE friends.closeness > 5 ORDER BY closeness')
for friend in friends:
    print(friend)
# commit changes
conn.commit()

# close the connection
conn.close()