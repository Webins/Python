#with open("story.txt", "a") as file:
#   file.write("\nexciting story\n")

with open("story.txt", "r+") as file:
    file.read()
    file.write("\nThis is the end...\n")
