from pyfiglet import figlet_format as ff
from termcolor import colored

print(colored(ff("Webins"), color="cyan", attrs=["blink"]))
