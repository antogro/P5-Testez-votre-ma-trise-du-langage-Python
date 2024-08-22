students = {
    "Alice": {"Mathematiques": 90, "Francais": 80, "Histoire": 95},
    "Bob": {"Mathematiques": 75, "Francais": 85, "Histoire": 70},
    "Charlie": {"Mathematiques": 88, "Francais": 92, "Histoire": 78},
}

student_name = str(input("Entrez le nom de l’étudiant: "))


def display_student(students: dict):
    if student_name in students:
        print("Note de: ", student_name)
        for key, value in students[student_name].items():
            print(f"{key}: {value}")

    else:
        print(f"L'étudiant {student_name} n'existe pas dans la liste")


def moyenne(students: dict) -> str | int:
    if student_name in students:
        moyenne = 0
        for value in students[student_name].values():
            moyenne += value
        moyenne /= len(students[student_name])
    print("moyenne: ", moyenne)


def main():
    display_student(students)
    moyenne(students)


if __name__ == "__main__":
    main()
