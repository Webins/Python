from random import choice as ch, shuffle as shuf
from custom_module import tab, new_line as nl

print("I am in: " + __name__)
nl()
print(ch(["apple", "banana", "cherry", "durian"]))
nl(); nl()
tab();tab();
print(shuf(["apple", "banana", "cherry", "durian"]))

