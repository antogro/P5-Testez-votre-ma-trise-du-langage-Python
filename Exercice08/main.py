def log_decorator(func):
    def wrapper():
        print("Avant")
        result = func()
        print("Après")
        return result
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

def main():
    function_test()

if __name__ == "__main__":
    main()

