# Écrivez votre code ici !
class BankAccount:
    def __init__(self, account_holder, balance) -> None:
        self.account_holder: str = account_holder
        self.balance: float = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"La somme {amount} à été ajouté")
        else:
            print("Le montant du dépot doit être positifs")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient balance you don't have enought ")
                print(f"balance {self.balance} somme a retirer {amount}")
        else:
            print("Le montant du retrait doit être positif")

    def display_balance(self):
        print(f"Mr/Mdm {self.account_holder} Propriètaire du compte.")
        print(f"Il vous reste: {self.balance} € sur votre comtpre")

def main():
    account = BankAccount("Martin Francois", 1000.0)
    account.display_balance()
    account.deposit(200.0)
    account.withdraw(150.0)

    account.display_balance()


if __name__ == "__main__":
    main()
