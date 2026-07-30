"""Class variables are shared by all objects of that class

Sometimes we want all objects of a class to share a CONSTANT or
variable
• This is modelled using class variables
• Class variables go between the class header and the first method
• Example: all Taxi objects will share the same price_per_km. If this ever
changes (e.g., Taxi.price_per_km *= 1.1), then all taxis will share this
new value."""

"""E.g.------------------------"""
# class Taxi(Car):
#     Price_per_km = 1.23
#     def __init__(self, name, fuel):
"-------------------------------------"

"""Remember itemgetter for sorting different list elements"""
from operator import itemgetter
data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
data.sort(key=itemgetter(1))
# Gives [['Bob', 6], ['Derek', 7], ['Carrie', 8], ['Aaron', 9]]

"For classes/objects, use attrgetter, like"
from operator import attrgetter
# Sort objects by their last_name attribute
data = [Person(name="Bob", age=18), ...]
data.sort(key=attrgetter("name"))

"""TERMINOLOGY
• Class - a blueprint (template) for creating objects
• Object - a specific instance of a particular class
• Method - a function defined within a class
• Field / Attribute / Instance variable - a variable that belongs to
(inside) an object (e.g., self.x)"""
