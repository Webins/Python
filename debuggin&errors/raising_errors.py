import time
from inspect import currentframe, getframeinfo

def colorize(text, color):
    color = color.lower()
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if color not in colors:
        fi = getframeinfo(currentframe())
        raise ValueError(f"Error encountered in file {fi.filename} line {fi.lineno} at function {colorize.__name__}\n'{color}' is not in the list. Error caused at: {time.ctime()}")
    
    if type(color) is not str:
        fi = getframeinfo(currentframe())
        raise ValueError(f"Error encountered in file {fi.filename} line {fi.lineno} at function {colorize.__name__}\n'{color}' is not a string. Error caused at: {time.ctime()}")

    if type(text) is not str:
        fi = getframeinfo(currentframe())
        raise ValueError(f"Error encountered in file {fi.filename} line {fi.lineno} at function {colorize.__name__}\n'{text}' is not a string. Error caused at: {time.ctime()}")

    
    print(f"Printed {text} in {color}")


try:
    colorize("Hello", "cyan")
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Text was printed succesfully")
finally:
    print("End...")