class User:
    id = 0
    username = ""
    birth_data = ""
    money = 0
    father = ""
    mother = ""

    def __init__(self, id, username, birthdata, money, father, mother):
        self.id = id
        self.username = username
        self.birth_data = birthdata
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

    def dayin(self):
        if self.father == None:
            print("id:", self.id, " father= NULL mother=NULL")
        else:
            print("id:", self.id, " father=", self.father.username, "  mother=", self.mother.username)
