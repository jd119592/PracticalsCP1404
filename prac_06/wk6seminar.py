
# list comprehension for new list
# containing only products that are on sale
"""Lecture 6 - Do This Now"""

products = [["Phone", 340, False],
            ["PC", 1420.95, True], ["Plant", 24.5, True]]

# on_sale_product = [product for product in products if product[2]]
# print(on_sale_product)

"Exam Hint-----------------------------------------------"
"Be able to write a simple, "
"complete class from scratch. Learn how the basic standard "
"template methods work and practise writing classes with these. "
"Lets look at these methods now."

"""Sample Exam Question-------------------
How confident are you feeling about the final exam? Here's a sample exam question 
with details about marking, tips for doing well, and a worked solution. Your exam 
might be online rather than written on paper. It's still a good idea to practise 
hand-writing code as it will help you learn more. Get pen and paper 
(proper, A4 paper) ready now"""

class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        """to tell you what the class has"""
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):

        if self.is_on_sale:
            on_sale_string = "(on_sale)"
        else:
            on_sale_string = ""
        return f"{self.name}, ${self.price:.2f} {on_sale_string}"

    def __repr__(self):
        return str(self)

    def put_on_sale(self, discount_percentage):
        """this will put product on sale by discount percentage as decimal (e.g. 0.2 is 20%)"""
        self.price *= (1 - discount_percentage)
        self.is_on_sale = True

print(__name__)

if __name__ == '__main__':
    p = Product("Phone", 340, False)
    print(p.name, "...")
    print(p)
    p.put_on_sale(0.1)
    print(p)
    print(type(p))

# products = [Product("Phone", 340, False),
#             Product("PC", 1420.95, True), Product("Plant", 24.5, True)]
#
# on_sale_products = [product for product in products if product.is_on_sale]
# print(on_sale_products)


"""Self refers to this specific object that the method is involked on
self is for instance variables not local variables"""

"""Define all a class's fields in __init__
youre warned not to define a new field outside __init__ bad practice"""

"""Define __str__ for printing objects
when opject is printed python runs the __str__ method which must return str see above"""

# standard class methods Template
# from kivy.app import App
# from kivy.app import Widget
# """Class (New Type)"""
# Class HelloWorld(App):
# """Method (function)"""
#   def build(self):
#       """Reference to instance"""
#       self.root Widget()
#       return self.root
# "create new object of type HelloWorld"
# HelloWorld().run()
# "call method run of new object (Kivy defines this method)"

"Class's responsibilities are:"
"responsible for knowing = data attributes,"
" responsible for doing = methods"
"to find responsibilities look at problem "
"domain and deduce required information and actions"
"-----------------------------------------------------------------------"

"""Classes should be store in modules, 
The module filename should be class_name_in_lowercase.py

# person.py
class Person:
   def __init__(self):"""

""" Client Code (other file)
from person import Person
me = Person()
..."""



