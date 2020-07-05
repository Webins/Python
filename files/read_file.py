file_name = "story.txt"
try:
    file = open(f"./{file_name}")
except OSError:
    print(f"Error opening the file {file_name}")

print(file.read())

# move to the beginning
file.seek(0)

print(file.read())

file.seek(0)

# read line by line
print(file.readline())

file.seek(0)

# read all the lines an put in a list
print(file.readlines())

# close a file
file.close()

#check if the file is close
print(f"{file_name} is closed: {file.closed}")