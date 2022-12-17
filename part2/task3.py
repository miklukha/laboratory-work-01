class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


class Customer:
    def __init__(self, name, surname, mobile_phone):
        self.name = name
        self.surname = surname
        self.mobile_phone = mobile_phone


class Order:
    order = {"owner": None, "products": [], "price": 0}

    def __init__(self, order_id):
        self.order_id = order_id

    def get_owner(self):
        if self.order["owner"]:
            return self.order["owner"].name
        else:
            return None

    def set_owner(self, owner):
        self.order["owner"] = owner

    def get_products(self):
        if len(self.order["products"]) != 0:
            return self.order["products"]
        else:
            return "You already haven't any products"

    def set_product(self, product):
        self.order["products"].append({"product_name": product.name,
                                       "product_price": product.price,
                                       "product_description": product.description})

    def calc_price(self):
        for i in self.order["products"]:
            self.order["price"] += i["product_price"]

    def get_order(self):
        products = []
        for product in self.order['products']:
            products.append(product['product_name'])

        return f"Customer name: {self.order['owner'].name}\n" \
               f"Products: {', '.join(products)}\n" \
               f"Final price: {self.order['price']}"


Anna = Customer(name="Anna",
                surname="Miklukha",
                mobile_phone="+380950714248")

Book = Product(name="Book: 'To Kill a Mockingbird'",
               price=130,
               description="To Kill a Mockingbird is a novel by the American author Harper Lee. "
                           "It was published in 1960 and was instantly successful.")

Socks = Product(name="Christmas socks",
                price=220,
                description="Mens and Ladies 1 Pair Lazy Panda Bamboo Fun & Novelty Socks")

Cup = Product(name="Cup",
              price=220,
              description="Personalised Christmas Cup Santa with straw")

order = Order("12241242")
order.set_owner(Anna)
order.set_product(Book)
order.set_product(Socks)
order.set_product(Cup)
order.calc_price()

print(order.get_order())

