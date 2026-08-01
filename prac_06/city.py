"""City Class"""

class City:
    """City class"""


    def __init__(self, name="", population=0, percent=0.0):

        """Initialise a City object."""
        self.name = name
        self.population = population
        self.percent = percent


    def __repr__(self):
        """Returns string representation of data in a City"""
        return f"{self.name}, {self.population:,}, {self.percent}%"

    def __lt__(self, other):
        return self.population <= other.population

    def __eq__(self, other):
        return self.population == other.population

    def __add__(self, other):
        return City(self.name + other.name, self.population + other.population, 100)


def run_tests(self):
    c1 = City("Tokyo", 13921000, 11.20)
    c2 = City("Rome", 2761632, 4.70)
    # print(c1)
    print(c1 > c2)
    print(c1 == c2)
    print(c1 + c2)



if __name__ == '__main__':
    run_tests(City)

