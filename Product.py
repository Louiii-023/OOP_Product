class Product: # Represents a product in the inventory
    inventory = []
    product_counter = 1

 # Initializes a new product with given attributes     
    def __init__(self, name, category, quantity, price, supplier): 
        self.product_id = Product.product_counter
        Product.product_counter += 1 # Increment product ID for the next product

        self.name = name
        self.category = category
        self.categoryquantity = quantity
        self.price = price  
        self.supplier = supplier

        Product.inventory.append(self) # Add the new product to the inventory list


# Class method to add a new product to the inventory
    @classmethod 
    def add_product(cls, name, category, quantity, price, supplier): 
      new_product = cls(name, category,quantity, price, supplier)
      print("Product added successfully")
      return new_product
    
# Update product details based on provided parameters
    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
       for product in cls.inventory: # Iterate through the inventory to find the product
          if product.product_id  == product_id: 
            if quantity is not None:
               product.quantity = quantity
            if price is not None:
               product.price = price
            if supplier is not None:
               product.supplier = supplier
            return "Product information updated successfully"
       return "Product not found"
    
# Delete a product from the inventory based on product ID    
    @classmethod
    def delete_product(cls, product_id): 
       for product in cls.inventory:
          if product.product_id == product_id:
             cls.inventory.remove(product)
          return "Product deleted successfully"
       return "Product not found"
    
class Order: # Represents a customer order(new class created)
   def __init__(self, order_id, product_id, quantity, customer_info = None):
      self.order_id = order_id
      self.product_id = product_id
      self.quantity = quantity
      self.customer_info = customer_info

   # Method to place an order
   def place_order(self): 
      for product in Product.inventory:
         if product.product_id == self.product_id:
            if product.quantity >= self.quantity:
                  return f"Order placed successfully. Order ID: {self.order_id}"
            else:
                  return "Insufficient stock to place the order"
      return "Product not found"
   
# Example usage
Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
Product.add_product("Chair", "Furniture", 20, 150, "Supplier B")
Product.add_product("Notebook", "Stationery", 100, 5, "Supplier C")
print(Product.update_product(1, quantity=45, price=950))
print(Product.delete_product(2))
order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")
print(order1.place_order())
