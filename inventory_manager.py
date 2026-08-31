import json
print("This is version 2")
class Product:

    def __init__(self,id,name,price,quantity,category):
        self.id = id 
        self.name = name 
        self.price = price 
        self.quantity = quantity
        self.category = category

class Inventory:


    def __init__(self,store_name):
        self.store_name = store_name
        self.inventory = []



    def unique_id_generator(self):
        highest = 0 
        for i in self.inventory:
            if i.id > highest:
                highest = i.id
        return highest +1 


    def add_product(self):
        product_name = input("Enter product name = ").strip()
        product_name = self.product_name_validator(product_name)
        price = input("Enter product pirce = ")
        price = self.price_validator(price)
        quantity = input("Enter quantity = ")
        quantity = self.quantity_validaotr(quantity)
        category = input("Enter category = ").capitalize().strip()
        category = self.category_validator(category)
        id = self.unique_id_generator()
        one_product = Product(id,product_name,price,quantity,category)
        self.inventory.append(one_product)

    
    

    def remove_product(self,quantity):
        product_to_remove = input("Enter name of product to remove = ")
        quantity_of_product_to_remove = int(input("Enter the quantity of product to remove = "))
        print("====================================")
        for product in self.inventory:
            if product.name == product_to_remove and quantity_of_product_to_remove <= product.quantity :
                product.quantity = product.quantity - quantity_of_product_to_remove
                print(f"After removing we have {product.quantity} in stok  remaining of {product_to_remove}")
            if product.quantity == 0:
                print("No stock left all products has been sucesfully removed!")
            print(f"{product_to_remove} remaining in stock {product.quantity}")
            self.inventory.remove(product)
        print("=======================================")        
                
        

    def sell_product(self):
        product_to_sell = input("Enter name of product to sell = ")
        quantity_of_product_to_sell = int(input("Enter the quantity of product to sell = "))
        print("====================================")
        for product in self.inventory:
            if product.name == product_to_sell and quantity_of_product_to_sell <= product.quantity :
                product.quantity = product.quantity - quantity_of_product_to_sell
                print(f"After removing we have {product.quantity} in stok  remaining of {product_to_sell}")
            if product.quantity == 0:
                print("No stock left all products has been sucesfully sold !")
                self.inventory.remove(product)
        print(f"{product_to_sell} remaining in stock {product.quantity}")
        print("=======================================")        
                        


    def restock_product(self,quantity):
        product_to_restock = input("Enter name of product to restock = ")
        quantity_of_product_to_restock = int(input("Enter the quantity of product to restock = "))
        print("====================================")
        print(f"{product_to_restock} remaining in stock {quantity}")
        for product in self.inventory:
            if product.name == product_to_restock  :
                product.quantity = product.quantity + quantity_of_product_to_restock
                print(f"After restocking we have {product.quantity} in stock  remaining of {product_to_restock}")
        print("=======================================")  
        


    def display_inventory(self):
        for product in self.inventory:
            print("===============================")
            print(f"Product id : {product.id} ")
            print(f"Product name: {product.name}")
            print(f"Quantity left : {product.quantity}")
            print(f"Category: {product.category}")
            print("==================================")

    #-------------------------Validatorr --------------------------------------------#

    def product_name_validator(self,product_name):
        while True :
            if  3 <= len(product_name) <= 100:
                return product_name
            print("Invalid Input ")
            product_name = input("Enter product name again = ")
        

    def price_validator(self,price):
        while True :
            if len(price) > 0  and price.isdigit() and  0 < int(price):
                return price 
            print("Invalid price ")
            price = input("Enter the price again = ")


    def quantity_validaotr(self,quantity):
        while True : 
            if len(quantity) > 0 and quantity.isdigit() and 0 < int(quantity)< 10000 : 
                return quantity 
            print("Invalid quantity ")
            quantity = input("Enter quantity again = ")




    def category_validator(self,category):
        categoties_in_store = ["Food","Beverages","Tech","Furniture","Clothing"]
        for items in categoties_in_store:
            print("=============================================")
            print (items)
            print("=============================================")
        while True : 
            if category in categoties_in_store:
                return category
            print("Not in our expertise ")
            category = input("Enter the category name again = ").capitalize().strip()


    #------------------------ Connecting OOP and Json ---------------------#
  
    def writing_in_json(self):
        pass


    def load_in_json(self):
        with open ("inventory.json","r") as f:
            data = json.load(f)
        self.inventory.clear()
        for product_data in data:
            product = Product(
            product_data["id"],
            product_data["name"],
            product_data["price"],
            product_data["quantity"],
            product_data["category"]
        )
            self.inventory.append(product)
        
        

#---------------------- MENU -------------------------#

print("Welcome to Inventory manager  ")

def menu():
    menu_list = ["1) Add product ", "2) Remove product ", "3) Sell product ", "4) Restock product ", "5) Display inventory " , "6) Exit "]
    for i in menu_list:
        print(i)


name_of_shop = input("Enter name of shop = ")
one_shop = Inventory(name_of_shop)

def task_identifer(task,one_shop,quantity):
    if task in ["1" , "Add product "]:
        one_shop.add_product()
    if task in ["2" , "Remove product"]:
        one_shop.remove_product()
    if task in ["3" , "Sell prdouct"]:
        one_shop.sell_product()
    if task in ["4" , "Restock product"]:
        one_shop.restock_product()
    if task in ["5","Display inventory "]:
        one_shop.display_inventory()

    

def menu_validator(task):
    while True:
        if task in ["1", "2","3","4","5","6","Add product","Remove product","Sell product","Restock product","Display inventory","Exit"]:
            return task 
        print("Choose the correct menu option ")
        task = input("Enter task again = ")


while True :
    menu()
    task = input("Enter your task = ").capitalize()
    menu_validator(task)
    task_identifer(task,one_shop)
    if task in ["6","Exit"]:
            break
    print("Thnakyou for visiting ! ")


    


    








