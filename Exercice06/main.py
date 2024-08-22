# Fonction calculate_average
def calculate_average(number):
    average = 0
    divided = 0
    for value in number:
        average += value
        divided += 1
    average /= divided
    return average




def main():
    # Exemple d'utilisation de la fonction
    numbers = [10, 20, 30, 40, 50]
    average = calculate_average(numbers)
    print("La moyenne est :", average)


if __name__ == "__main__":
    main()
