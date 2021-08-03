class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def get_balance(self):
        funds = 0
        for i in range(len(self.ledger)):
            funds += self.ledger[i]['amount']
        return funds

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, description=f"Transfer to {category.name}")
            category.deposit(amount, description=f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        details = ""
        details += self.name.center(30, '*') + '\n'
        for i in range(len(self.ledger)):
            details += self.ledger[i]['description'][:23].ljust(23) +\
                       "{:.2f}".format(self.ledger[i]['amount']).rjust(7) + '\n'
        details += "Total: " + str(self.get_balance())
        return details


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spent_percent = list()
    total_withdraw = 0
    for category in categories:
        category_withdraw = 0
        for each in category.ledger:
            if each['amount'] < 0:
                category_withdraw += each['amount']
        total_withdraw += category_withdraw
    for category in categories:
        category_withdraw = 0
        for each in category.ledger:
            if each['amount'] < 0:
                category_withdraw += each['amount']
        category_withdraw_percent = category_withdraw / total_withdraw * 100
        spent_percent.append(round(category_withdraw_percent, 0))
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for each in spent_percent:
            if each >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += '\n'
    chart += "    -" + "---" * len(spent_percent) + '\n'
    names = []
    for category in categories:
        names.append(category.name)
    max_len = max(names, key=len)
    for i in range(len(max_len)):
        chart += "     "
        for name in names:
            try:
                chart += name[i] + "  "
            except IndexError:
                chart += "   "
        chart += '\n'
    chart = chart.rstrip('\n')
    return chart
