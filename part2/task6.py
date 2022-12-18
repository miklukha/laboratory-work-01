# Create a class BINARY TREE that contains background information of product prices (product code, price of 1 product).
# The tree is sorted by product codes.
# From the keyboard enter data on the number of products in the format: product code, number of products.
# Using a tree, find the cost of products (cost = quantity * price of one product).
class BinaryTree:
    products = []
    def __init__(self):
        pass

    def add_product(self, product_code, product_price):
        self.products.append({"code": product_code,
                              "price": product_price})

    def get_products(self):
        for product in self.products:
            print(f"Product with code: {product['code']} has price: {product['price']}")

    def find_product_price(self, product_code, number_of_products):
        for product in self.products:
            if product["code"] == product_code:
                total_price = product['price'] * number_of_products
                return f"The total price of product is {total_price:.2f}"
        return f"The product with code {product_code} not found"


tree = BinaryTree()
tree.add_product('342', 10.50)
tree.add_product('343', 132)
tree.add_product('344', 213.99)
tree.add_product('345', 255.6)
tree.add_product('346', 300)
print(tree.find_product_price('342', 3))
