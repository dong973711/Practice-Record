class User:
    
    def __init__(self, id, username, birthdate, money, father, mother):
        self.id = id
        self.username = username
        self.birth_date = birth_date
        self.money = money
        self.father = father
        self.mother = mother

    def set_username(self, name):
        self.username = name

    def get_username(self):
        return self.username

    def set_money(self, money):
        self.money = money

    def get_money(self):
        return self.money

    def print(self):
        if self.father == None:
            print("id: {} father= NULL mother= NULL".format(self.id))
        else:
            print("id: {} father= {}  mother= {}".format(self.id, self.father.id, self.mother.id))
