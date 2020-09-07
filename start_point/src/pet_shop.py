# # WRITE YOUR FUNCTIONS HERE
# def get_pet_shop_name(pets):
#         if(pets["name"]):
#             return pets["name"]

# def get_total_cash(pets):
#     return pets["admin"]["total_cash"]


# def add_or_remove_cash(pets, number):
#     pets["admin"]["total_cash"] += number
#     return pets["admin"]["total_cash"]

# def get_pets_sold(pets):
#     return pets["admin"]["pets_sold"]

# def increase_pets_sold(pets, number):
#     pets["admin"]["pets_sold"] += number
#     return pets["admin"]["pets_sold"]

# def get_stock_count(pets):
#     lists = len(pets["pets"])
#     return lists

# def get_pets_by_breed(pets, name):
#     lists = []
#     for pet in pets["pets"]:
#         if(pet["breed"] == name):
#             lists.append(pet)
#     return lists

# def find_pet_by_name(pets, name):
#     for pet in pets["pets"]:
#         if(pet["name"]== name):
#             return pet
#     return None

# def remove_pet_by_name(pets, name):
#     for pet in pets["pets"]:
#         if(pet["name"] == name):
#             pet["name"] = None
#     return pet

# def  add_pet_to_stock(pets, new_pet):
#     new_pet = {"name": "Skippy", "pet_type": "dog", "breed": "Alsatian", "price": 900,}
#     pets["pets"].append(new_pet)
#     get_stock_count(pets)

# def get_customer_cash(customer_cash):
#     return customer_cash["cash"]

# def remove_customer_cash(customer_cash, number):
#     customer_cash["cash"] -= number
#     return customer_cash["cash"]


# def get_customer_pet_count(customer_count):
#     lists = customer_count["pets"]
#     return len(lists)

# def add_pet_to_customer(customer, pet):
#     pet = {
#             "name": "Bors the Younger",
#             "pet_type": "cat",
#             "breed": "Cornish Rex",
#             "price": 100
#         }
#     lists = customer["pets"]
#     lists.append(pet)
#     return len(lists)

# def customer_can_afford_pet(customers, new_pet):
#     if customers["cash"] >= new_pet["price"]:
#         return True
#     else:
#         return False


# def sell_pet_to_customer(pet_shop, pets, customers):
#     if(pets != None) and (customer_can_afford_pet(customers, pets) == True):
#         print("Pet cannot be found! ")
#         pet_shop["admin"]["pets_sold"] = 1
#         add_pet_to_customer(customers, pets)
#         get_customer_pet_count(customers)
#         get_pets_sold(pet_shop)
#         customers["cash"] -= pets["price"]
#         get_customer_cash(customers)
#         pet_shop["admin"]["total_cash"] += pets["price"]
#         get_total_cash(pet_shop)



def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]

def get_total_cash(shop_cash):
    return shop_cash["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    new_cash = get_total_cash(pet_shop)
    return new_cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]
        
def increase_pets_sold(pet_shop, number):
    pet_shop["admin"]["pets_sold"] += number
    pet_sold = get_pets_sold(pet_shop)
    return pet_sold

def get_stock_count(pet_shop):
    list_pets = []
    for pet in pet_shop["pets"]:
        list_pets.append(pet)
    
    return len(list_pets)

def get_pets_by_breed(pet_shop, pet_breed):
    pet_found = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pet_found.append(pet)
    
    return pet_found

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet["name"] = None
    pet_found = find_pet_by_name(pet_shop, pet_name)
    return pet_found

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    get_stock_count(pet_shop)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount
    return customer["cash"]

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    pet_count = get_customer_pet_count(customer)
    return pet_count

def customer_can_afford_pet(customer, new_pet):
    if(customer["cash"] >= new_pet["price"]):
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    if((pet != None) and (customer_can_afford_pet(customer, pet) == True)):
        add_pet_to_customer(customer, pet)
        get_customer_pet_count(customer)
        increase_pets_sold(pet_shop, 1)
        get_pets_sold(pet_shop)
        remove_customer_cash(customer, pet["price"])
        get_customer_cash(customer)
        add_or_remove_cash(pet_shop, pet["price"])
        get_total_cash(pet_shop)