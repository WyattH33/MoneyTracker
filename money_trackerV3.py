'''
program ideas: 
add a deposit description
'''

place_holder_var = 0

# class for creating each budget and user
class Budget():
    def __init__(self, monthtly_income,  perc_lis):
        self.category_value_list = []
        self.category_name_list = name_list
        self.category_obj_list = [Category(name) for name in self.category_name_list]


# actual transaction logic, displays transaction details, adds the data from each transaction to category_value_list
    def transaction(self):
        self.deposit_location = deposit_location
        self.deposit_amt = deposit_amt
        self.category_value_list = self.deposit_location

        for index, obj in enumerate(self.category_obj_list):
            if username_var in user_dict:
                try:
                    obj.max = user_dict[username_var][deposit_location][0]
                    obj.amt = user_dict[username_var][deposit_location][1]
                except UnboundLocalError:
                    pass
            else:
                obj.max = (obj.perc_list[index] / 100) * obj.monthly_income 
            if self.deposit_location == self.category_name_list[index]:
                self.deposit_amt = deposit_amt
                pass
            else:
                self.deposit_amt = 0
                pass 
            obj.amt += self.deposit_amt
            obj.left = obj.max - obj.amt
            self.max = obj.max
            self.amt = obj.amt
            self.left = obj.left
            self.category_value_list = [obj.max, obj.amt, obj.left, obj.perc_list[index]]
            self.category_value_list.extend([obj.max, obj.amt, obj.left, obj.perc_list[index]])
            if len(self.category_value_list) > 4:
                del self.category_value_list[:4]

            if name_list[index] == deposit_location:
                self.category_dict =  get_category_data(name_list[index], self.category_value_list)
            elif place_holder_var == 0:
                list = [obj.max, 0, obj.max, obj.perc_list[index]]
                self.category_dict =  get_category_data(name_list[index], list)
            if self.deposit_amt != 0:
                print(f"Amount spent on {obj.name}: ${obj.amt} \nAmount left to spend: ${round(obj.left,2)}")


# Class that defines a category object

class Category():
    def __init__(self, name):
        self.name = name
        self.perc = 0
        self.amt = 0
        self.left = 0
        self.max = 0
        self.perc_list = perc_list
        self.monthly_income = inc

# gets monthly income
def get_inc():
    while True:
        try:
            inc = float(input("Enter your monthly income after taxes: "))
            return inc
        except ValueError:
            print("Invalid Input : Must be a number")
            continue
            
# gets number of categories
def get_cat_num():
    while True:
        try:
            cat_num = int(input("Enter total number of desired categories: "))
            return cat_num
        except ValueError:
            print("Invalid Input : Please enter a number")
            continue

# gets each category name and adds it to name_lis
name_list = []
def get_cat(cat_num):
    num = 0
    while num < cat_num:
        num += 1
        cat = input(f"Catetgory {num}: ")
        name_list.append(cat)
    return name_list

# retrieves and adds each categories percentages to a list
perc_list = []
def gather_perc():
    print("Enter desired percentage of income spent for each category (do not include %): ")
    x = 0
    y = 0
    while x < len(name_list):
        y = 0
        for i in name_list:
            try:
                if y == 0:
                    perc = float(input(f"{i}: "))
            except ValueError:
                    print("Invalid Input : Please enter a number")
                    y = 1
                    continue
            if y == 0:
                perc_list.append(perc)
        # makes sure the percentages sum from 95-105  
            if len(perc_list) == cat_num:
                if sum(perc_list) not in range(95, 105):
                    print("Invalid Input : Must add to 100%")
                    perc_list.clear()
                    x = 0
                    continue
                else:
                    return perc_list


# gets the deposit location
def get_location():

    while True:
        try:
            deposit_location = ""
            deposit_location = input("Where would you like to deposit? ")
            if deposit_location not in name_lis:
                print("Invalid Input : Must be valid category")
                continue
            else:
                return deposit_location
        except ValueError:
            print("Invalid Input : Must be valid category")
            continue

# gets the deposit amount
def get_amt():
    while True:
        try:
            deposit_amt = 0
            deposit_amt = float(input("Deposit amount: "))
            return deposit_amt
        except ValueError:
            print("Invalid Input : Must be a number")
            continue

# assigns each category its percentage 
def get_perc():
    for name in name_lis():
        perc = float(input(f"{name}: "))
        perc_lis.append(perc)
    return perc_lis

# makes a dictionary with each category (the data for each category is added later)
category_dict = {}
def make_dict():
    for index, name in enumerate(name_lis):
        category_dict[name] = ["NO DATA"]

# adds each categories data to category_dict
value_count = 0
def get_category_data(deposit_location_var, category_value_list_var):
    category_dict[deposit_location_var] = category_value_list_var
    return category_dict

# stores user in a dictionary
user_dict = {}
def store_user():
    user_dict[username_var] = category_dict
    return user_dict

# actual code that is ran
username_var = input("Username: ")
done = 0
while True:    
    if done != 3:
        if username_var not in user_dict:
            # runs when a the username isnt recognized 
            inc = get_inc()
            cat_num = get_cat_num()
            name_lis = get_cat(cat_num)
            make_dict()
            perc_lis = gather_perc()
            place_holder_var = 0
        else: 
            category_dict = user_dict[username_var]
            name_lis.extend(category_dict.keys())
            for key in category_dict:
                perc_lis.append(user_dict[username_var][key][-1])
            r = 0
            for key, value in category_dict.items():
                print(f"Category - {name_lis[r]} :: Max budget - {value[0]} :: Budget spent - {value[1]} :: Budget left - {value[2]}")
                r += 1

        # code that is ran to perform every transactoin 
        deposit_location = get_location()
        deposit_amt = get_amt()
        username = Budget(inc, username_var)   
        category_value_list = username.transaction()
        place_holder_var += 1
        user_dict = store_user()


    while True:
        try:
            done = int(input("Option 1 - Restart as new/different user \n"
                    "Option 2 - Restart as same user\n"
                    "Option 3 - Continue as same user\n"
                    "Option 4 - Quit\n"
                    "Enter option number: "))
            break
        except ValueError:
            print("Invalid Input : Please enter the number corresponding to your choice")
            continue
# resets all data that applies the current user so it can create new data
    if done == 1:
        username_var = input("Username: ")
        perc_lis = []
        name_lis = []
        category_dict = {}

# same thing as above but doesn't reset the user, just all of the current users data
    elif done == 2: 
        user_dict.pop(username.username)
        perc_lis = []
        name_lis = []
        category_dict = {}
        continue
# allows you to continue to make transactions as the current user without changing any of the data
    elif done == 3:
        deposit_location = get_location()
        deposit_amt = get_amt()
        category_value_list = username.transaction()
        store_user()
        continue

    elif done == 4:
        print("Thank you")
        break
    else:
        print("Invalid Input")
        continue

