# ratings class
# Authors: Oleg, Liam, Henry

class Ratings:

    def __init__(self, User_id, ISBN, ratings):
        self.User_id = User_id
        self.ISBN = ISBN
        self.ratings = ratings

    def __str__(self):
        return f"{self.User_id}, {self.ISBN}, {self.ratings}"

    def __repr__(self):
        return f"Ratings({self.User_id}, {self.ISBN}, {self.ratings})"
