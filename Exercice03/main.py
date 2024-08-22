words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

mots_voyelles = []


def nombre_voyelles(mots):
    voyelles = ["a", "e", "i", "o", "u", "y"]
    compteur = 0

    for word in mots:
        if word in voyelles:
            compteur += 1
    return mots, compteur


def comprehension(mots, compteur):
    mots_voyelles.append((mots, compteur))


def main():
    for word in words:
        mots, compteur = nombre_voyelles(word)
        comprehension(mots, compteur)
    print("mots_voyelles: ", mots_voyelles)


if __name__ == "__main__":
    main()
