class man:
    def __init__(self, name='dammy', age=20):
        self.name=name
        self.age=age
    
    def adress(self):
        print(f"your name is {self.name} and you are {self.age} years old")

    def change_age(self, new_age):
        self.age=new_age
        print(f"you are now {self.age} years old")

per1=man()

per1.adress()

per1.change_age(23)