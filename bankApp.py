"""
Bank app
Single flow console application

main->welcome->auth
stakeholders: admin, customer
admin menu, customer menu
CRUD Operations

loops and single flow

"""
from abc import *

class Account(ABC):
    def __init__(self, n):
        self.number = n
        self.balance = 0

    def setBalance(self, b):
        self.balance = b
    
    def getBalance(self):
        return self.balance
    
    def alterBalance(self, amount):
        if self.balance + amount >= 0:
            self.balance += amount
            return True
        else:
            return False
    
    def getNumber(self):
        return self.number
    
    @abstractmethod
    def addinterest(self):
        pass

    @abstractmethod
    def printAccount(self):
        pass

class Saving(Account):
    def addinterest(self):
        self.balance *= 1.02

    def printAccount(self):
        print("Savings Account")
        print(f"Account Number: {self.number}")
        print(f"Account Balance: {self.balance}")

class Checking(Account):
    def addinterest(self):
        self.balance *= 1

    def printAccount(self):
        print("Checkings Account")
        print(f"Account Number: {self.number}")
        print(f"Account Balance: {self.balance}")

class User(ABC):
    def __init__(self, u, p):
        self.username = u
        self.password = p

    def getPassword(self):
        return self.password
    
    @abstractmethod
    def isAdmin(self):
        pass

    @abstractmethod
    def dashboard(self, bank):
        pass

class Customer(User):
    def __init__(self, u, p, f, l, i):
        super().__init__(u, p)
        self.first = f
        self.last = l
        self.id = i
        self.accounts = []

    def isAdmin(self):
        return False

    def getName(self):
        return self.first + " " + self.last
    
    def createAccount(self, b: Bank):
        accountType = ""
        while accountType.lower() != "s" and accountType.lower() != "c":
            accountType = input("s) savings account\nc)checking account\nchoose an acount type (s or c)")
        accountNumber = b.newAccount()
        newAccount = None
        if accountType.lower() == "s":
            newAccount = Saving(accountNumber)
        else:
            newAccount = Checking(accountNumber)
        self.accounts.append(newAccount)
        print(f"Account created!\nYour account number for this account is {accountNumber}")
        print()

    def readAccounts(self):
        print(f"{self.getName()}'s accounts")
        for a in self.accounts:
            a.printAccount()
            print()
        print()

    def findAccount(self, n):
        for a in self.accounts:
            if a.getNumber() == n:
                return a
        return None
    
    def deleteAccount(self, n):
        for i in range(len(self.accounts)):
            if self.accounts[i].getNumber() == n:
                self.accounts.pop(i)
                return True
        return False

    
    def dashboard(self, b: Bank):
        option = int(input(" 1) Create Account\n2) View All Accounts\n3)Deposit\n4) Withdraw\n5) Transfer\n6) Close Account\n7) Exit\nSelect an option:"))
        print()
        match option:
            case 1:
                self.createAccount(b)
            case 2:
                self.readAccounts()
            case 3:
                accNumber = int(input("input the account number you want to deposit to: "))
                acc = self.findAccount(accNumber)
                if acc:
                    amount = int(input("how much would you like to deposit?"))
                    if amount > 0:
                        acc.alterBalance(amount)
                        print("deposit successful")
                    else:
                        print("invalid amount, must be greater than 0")
                else:
                    print("invalid account number")
                    print()
            case 4:
                accNumber = int(input("input the account number you want to withdraw from: "))
                acc = self.findAccount(accNumber)
                if acc:
                    amount = int(input("how much would you like to withdraw?"))
                    if amount > 0:
                        if acc.alterBalance(amount * -1):
                            print("withdraw successful")
                        else:
                            print(f"Not enough in account, current balance is {acc.getBalance()}")
                    else:
                        print("invalid amount, must be greater than 0")
                else:
                    print("invalid account number")
                    print()
            case 5:
                accNumber1 = int(input("input the account number you want to transfer from: "))
                accNumber2 = int(input("input the account number you want to transfer to: "))
                acc1 = self.findAccount(accNumber1)
                acc2 = self.findAccount(accNumber2)
                if acc1 and acc2:
                    amount = int(input("how much would you like to transfer?"))
                    if amount > 0:
                        if acc1.alterBalance(amount * -1):
                            acc2.alterBalance(amount)
                            print("transfer successful")
                        else:
                            print(f"Not enough in account, current balance is {acc1.getBalance()}")
                    else:
                        print("invalid amount, must be greater than 0")
                else:
                    print("one or both account numbers are invalid")
            case 6:
                accNumber = int(input("input the account number you want to close: "))
                if self.deleteAccount(accNumber):
                    print(f"account {accNumber} closed.")
                else:
                    print("invalid account number")
                print()

            case 7:
                b.logout()
            case _:
                print("invalid option")
        return 0

class Admin(User):
    def __init__(self, u, p):
        super().__init__(u, p)

    def isAdmin(self):
        return True
    
    def createUser(self, b: Bank):
        accountType = input("a) admin user\nc)checking account\nchoose an acount type (s or c)")
    
    def findUser(self, b: Bank, u: str) -> User:
        return b.users[u]

    def readUsers(self, b: Bank):
        pass
    
    def updateUserPassword(self, u:User, newPassword: str):
        u.password = newPassword

    def deleteUser(self, b: Bank, u: User) -> bool:
        b.users.pop(u.username)
    
    def dashboard(self, b: Bank):
        option = input("1) Create User\n2) Show all users\n3) Update User password\n4)DeleteUser\n5)Log out admin\n6)Exit program\nSelect Option 1-6")
        print()
        match option:
            case 1:
                self.createUser()
            case 2:
                self.readUsers()
            case 3:
                username = input("what is the username of the user?")
                user = self.findUser()
                if user:
                    passw = input(f"what is the new username for {username}?")
                    self.updateUserPassword(user, passw)
                    print(f"{username} now has password {passw}")
                else:
                    print("invalid username")
            case 4:
                username = input("what is the username of the user to delete?")
                user = self.findUser()
                if user:
                    self.deleteUser(b, user)
                    print("user deleted")
                else:
                    print("invalid username")
                
            case 5:
                b.logout()
            case 6:
                print("goodbye!")
                return -1
            case _:
                print("invalid option!")
        print()
        return 0
        
    

class Bank:
    
    def __init__ (self):
        print("Welcome to the banking app")
        self.users = {"admin": Admin("admin", "admin123"), "joe": Customer("joe", "123", "Joe", "Smith", 123)}
        self.currLogin = None
        self.nextAccount = 0
    
    def getUser(self):
        return self.currLogin
    
    def logIn(self):
        output = input("Please enter your username and password, seperated by a space: ").split(" ")
        if len(output) != 2 or output[0] not in self.users or self.users[output[0]].getPassword() != output[1]:
            print("invalid username opr password")
        else:
            self.currLogin = self.users[output[0]]
            if self.currLogin.isAdmin():
                print("welcome admin")
            else:
                print("welcome " + self.currLogin.getName())
        print()



    def logout(self):
        print("you are now logging out of this User")
        self.currLogin = None

    def newAccount(self):
        self.nextAccount += 1
        return self.nextAccount




if __name__ == "__main__":
    b = Bank()
    status = 0
    while status == 0:
        if(b.getUser()):
            status = b.getUser().dashboard(b)
        else:
            b.logIn()