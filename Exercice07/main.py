# Écrivez votre code ici !
def square(a):
    try:
        return a * a
    except TypeError:
        return None

def main():
    print(square(5))  # Output: 25
    print(square("n"))  # Output: None


if __name__ == "__main__":
    main()
