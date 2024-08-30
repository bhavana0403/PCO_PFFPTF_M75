# list of items and number of items available
# price of each item
# add the item to cart
# remove the item from cart
# summary of the cart

class ShoppingCart:
    items = {'mobile': 5, 'laptop': 15, 'watch': 7, 'tablet': 10}
    prices = {'mobile': 1000, 'laptop': 5000, 'watch': 500, 'tablet': 1500}

    def __init__(self):
        self.cart = {}

    def add_item(self, item, quantity):
        if item not in ShoppingCart.items or quantity > ShoppingCart.items[item]:
            raise ValueError ("Item out of stock")
        self.cart[item] = quantity
        ShoppingCart.items[item] -= quantity

    def remove_item(self, item, quantity):
        if quantity <= self.cart[item]:
            self.cart[item] -= quantity
            ShoppingCart.items[item] += quantity
        else:
            raise ValueError

    def total_cost(self):
        total_cost = 0
        for item in self.cart:
            price = ShoppingCart.prices[item]
            no_of_items = self.cart[item]
            total_cost += price * no_of_items
        print(f"The total price of the cart is {total_cost}")

    def summary(self):
        print('*' * 100)
        for item, quantity in self.cart.items():
            price = ShoppingCart.prices[item]
            print(f"{item}  {quantity}  {price} {price*quantity}")
        self.total_cost()
        print('*' * 100)


cust1 = ShoppingCart()
cust2 = ShoppingCart()

# cust1.add_item("mobile", 8)
cust1.add_item("mobile", 1)
cust1.add_item("laptop", 2)

cust2.add_item("mobile", 3)
cust2.remove_item("mobile", 1)

cust1.total_cost()
cust2.total_cost()

print(cust1.cart)
print(cust2.cart)
print(ShoppingCart.items)

cust1.summary()
cust2.summary()

# create a class of your own choice with 4 object members
