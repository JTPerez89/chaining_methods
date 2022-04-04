class user:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.accountBalance = 0

    def makeDeposit(self, amount):
        self.accountBalance += amount
        return self

    def makeWithdrawal(self, amount):
        self.accountBalance -= amount
        return self

    def displayUserBalance(self):
        print(f'User: {self.firstName} {self.lastName} - Balance {self.accountBalance}.')

    def transfer(self, amount, targetAcc):
        self.accountBalance -= amount
        targetAcc.accountBalance += amount
        print(self.accountBalance)
        print(targetAcc.accountBalance)


bob = user('Bob', 'Smith')
tommy = user('Tommy', 'Timber')
jimmy = user('Jimmy', 'Johnson')

bob.makeDeposit(100).makeDeposit(100).makeDeposit(100).makeWithdrawal(25).displayUserBalance()

tommy.makeDeposit(100).makeDeposit(100).makeWithdrawal(25).makeWithdrawal(25).displayUserBalance()

jimmy.makeDeposit(100).makeWithdrawal(25).makeWithdrawal(25).makeWithdrawal(25).displayUserBalance()

bob.transfer(100, jimmy)