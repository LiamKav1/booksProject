# users class
class Users:

    def __init__(self, id: str, location: str, age: str):
        self.id = id
        self.location = location
        self.age = age

    def __str__(self):
        return f"{self.id}, {self.location}, {self.age}"

    def __repr__(self):
        return f"Users({self.id}, {self.location}, {self.age})"


    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
