class Product:
    def __init__(self,name,description,price):
        self.name = name
        self.description = description
        self.price = price

    def discount(self,percent):
        discountValue = self.price * percent
        print("Requested discount equals: ",discountValue)

product = Product('Shirt','Clothes',100)
print(product.__dict__)
product.discount(0.05)