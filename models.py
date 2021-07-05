import json


class Expenses:
    def __init__(self):
        try:
            with open("expenses.json", "r") as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            self.expenses = []
            '''
        self.sum = 0
        for i in self.expenses:
            self.sum += self.expenses[i]["amount"]
            '''

    def all(self):
        return self.expenses

    def get(self, id):
        return self.expenses[id]

    def create(self, data):
        data.pop('csrf_token')
        self.expenses.append(data)

    def save_all(self):
        with open("expenses.json", "w") as f:
            json.dump(self.expenses, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.expenses[id] = data
        self.save_all()

    def suma(self):
        summa = 0
        for i in self.expenses:
            summa += i["amount"]
        return summa


expenses = Expenses()
