# class Shoe
class Shoe:
    def __init__(self,country,code,product,cost,quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
 # method that return cost of the shoe
    def get_cost(self):
        return self.cost


 # method that return the quantity of the shoes
    def get_quantity(self):
        return self.quantity

# method that returns product
    def get_product(self):
        self.product

 # method that returns a string representation of a class
    def __repr__(self):
        return  self.country + "," + self.code + "," + self.product + "," + str( self.cost) + "," + str( self.quantity) + "\n"

 
# function that read from file then create a shoe object
# shoe objects are appended to shoes list
def read_shoes_data():
    try:
        with open('inventory.txt','r') as f:
            # reading line by line
            lines = f.readlines()
         
            # pointer for position
            ptr = 1
     
        # opening in writing mode
        with open('inventory.txt','w') as fw:
            for item in lines:
               
                # we want to remove 1st line
                if ptr != 1:
                    fw.write(item)
                ptr += 1
        with open("inventory.txt","r") as file:
            for line in file:
                line_list = line.strip("\n").split(",")
                shoe_object = Shoe(line_list[0],line_list[1],line_list[2],int(line_list[3]),int(line_list[4]))
                shoes_objects.append(shoe_object)
            print(shoes_objects)
            
            
    except FileNotFoundError as e:
        print("File does not exist")


# function that allows a user to capture data about a shoe
# a shoe object is created and appended to shoe list
def capture_shoes():
    with open("inventory.txt","a") as f:
        country=input("Enter the country: ")
        code=input("Enter the code: ")
        product=input("Enter the product: ")
        cost=float(input("Enter the cost: "))
        quantity=int(input("Enter the quantity: "))
    new_shoe=Shoe(country,code,product,cost,quantity)
    shoes_objects.append(new_shoe)
    
    
# prints  the shoes details 
def view_all():
    # iterate through the list
    for i in shoes_objects:
        print(i)


def restock():
        position = 0
        # finding shoe with the lowest quantity
        for index in range(1, len(shoes_objects)):
            if shoes_objects[index].quantity < shoes_objects[position].quantity:
                position = index
        shoe = shoes_objects[position]
        print("Lowest quantity product:\n", shoe)
        # asking the user to enter restock value
        new_quantity=int(input("Enter the restock value"))
        shoe.quantity = new_quantity


# searches for a shoes using a code entered by user
def search_shoes():
    shoe_code=input("Enter the code")
    with open("inventory.txt","r") as f:
        for line in f:
            data=line.strip("\n").split(",")
            if shoe_code in data:
                print(data)
           

# calculates total value for each item  
def value_per_item():
    for item in shoes_objects:
        value=item.get_cost() * item.get_quantity()
        print(f"The value for {item} is {value}")
     

# determines highest quantity
# product is on sale
def highest_quantity():
    position = 0
        # finding shoe with the lowest quantity
    for index in range(1, len(shoes_objects)):
        if shoes_objects[index].quantity > shoes_objects[position].quantity:
            position = index
    shoe = shoes_objects[position]
    print(f"{shoe} is on sale.")
    

# list of shoes objects
shoes_objects=[]
choice=""
while choice != "8":
    choice=input("""Select one of the options:
    1-read_shoes_data
    2_capture_shoes
    3-view_all
    4-restock
    5_search_shoes
    6-value_per_item
    7-highest_quantity
    8-exit
    """)
    if choice == "1":
        read_shoes_data()
        pass
    elif choice == "2":
        capture_shoes()
        pass
    elif choice == "3":
        view_all()
        pass
    elif choice == "4":
        restock()
        
        pass
    elif choice == "5":
        search_shoes()
        pass
    elif choice == "6":
        value_per_item()
        pass
    elif choice == "7":
        highest_quantity()
        pass
    elif choice == "8":
        print ("Goodbye")
    else:
        print("Invalid choice")
    
    

    
    
