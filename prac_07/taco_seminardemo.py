""""""

class User:

    def __init__(self, name):
        self.name = name
        self.tacos_count = 5
        self.score = 0

    def give_taco(self, other_user):
        self.tacos_count -= 1
        other_user.tacos_count += 1

    def __str__(self):
        return (f"{self.name}, {self.score} point{'' if self.tacos_count == 1 else 's'},"
                f" {self.tacos_count} taco{'' if self.tacos_count == 1 else 's'}")


alice = User("Alice")
bob = User("Bob")

alice.give_taco(bob)
print(alice)
print(bob)
