import sys

try:
    name = sys.argv[1]
except IndexError:
    name = input("name: ").title()

print(f"Hello, {name}")
