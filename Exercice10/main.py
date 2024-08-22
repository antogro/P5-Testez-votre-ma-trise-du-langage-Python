## Écrivez votre code ici !
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def afficher_details(self):
        return f"Nom : {self.name}, Age : {self.age}"


class Employee(Person):
    def __init__(self, name, age, salaire):
        self.salaire = salaire
        super().__init__(name, age)

    def afficher_details(self):
        return (f"{super().afficher_details()}, Salaire: {self.salaire}")



def main():
    person = Person("Alice", 30)
    employee = Employee("Bob", 25, 50000)

    print(person.afficher_details())
    print(employee.afficher_details())
    

if __name__ == "__main__":
    main()
