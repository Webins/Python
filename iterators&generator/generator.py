#every generator is an iterator but not every iterator is a generator
#a quick an easy short way to create iterators

#Generator functions returns multiples values (return a generator)

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(10)


for num in counter:
    print(num)

