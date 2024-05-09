# CISW 126 Dmitrii Gusev
# Objects Lab
#
# We're going to make a shopping cart.
# First we need to make a class that describes each item
# that we will put in the cart.
# Instantiate a class called item.
class Item:
    def __init__(self, description="None", price=0.0, quantity=0):
        self.description = description
        self.price = price
        self.quantity = quantity

    def cost(self):
        return self.price * self.quantity
# In your class constructor:
# Create an attribute called description
# - Description will hold a description of a given item.
# Create an attribute called price
# - Price will have the price for one individual item.
# Create an attribute called quantity
# - Quantity is the number of this item to be purchased.
# Create a method called cost
# - When called, cost will calculate the cost of
# purchasing *quantity* items at *price* per item
# and return that value.


if __name__ == "__main__":
    cart = []
    object1 = Item("Apple", 4.54, 12)
    object2 = Item("Banana", 0.99, 37)
    object3 = Item("Orange", 2.29, 10)
    object4 = Item("Carrot", 0.34, 3)
    cart.append(object1)
    cart.append(object2)
    cart.append(object3)
    cart.append(object4)
    total_coat = 0.0

    for i in range(0, len(cart)):
        print(f"Name of an item: {cart[i].description} - Price: ${cart[i].price}")
        total_coat = total_coat + cart[i].cost()
    print(f"Total cost of the cart: ${round(total_coat,2)}")
# This is where the "main body" of your program lives.
# This is the part that will automatically run if you
# run this particular Python file.
# First: Make an empty list called 'cart'.
# Then: Create a new object from the item class you created above.
# Give it a description, quantity and price. Whatever you like.
# Add it to the list. HINT: You can use the .append() method
# to add the objects you make to a list!
# Python lists can hold anything!
# Create another new class object and repeat the steps above.
# Then create another.
# Then one more.
# At this point you should have a list with four class objects
# in it.
# Write a loop that loops over the list, print out each of the
# item descriptions and costs, and then print the total of
#all the items in the list.
