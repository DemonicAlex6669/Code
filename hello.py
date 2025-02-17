import sys

def main():
    try:
        name = sys.argv[1]
    except IndexError:
        name = input("name: ").title()

    print(f"Hello, {name}")

if __name__ == "__main__":
    main()
