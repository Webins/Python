print("I am in: " + __name__)

def new_line():
    print()

def tab():
    print("\t", end='')

#this prevent code for being executed before the main called it
if __name__ == "__main__":
    new_line()