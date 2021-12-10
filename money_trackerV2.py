place_holder_var = 0

# class for creating each budget and user
class Budget():
    def __init__(self, monthtly_income, username):
        self.username = username_var
        self.monthly_income = monthtly_income
        self.perc_lis = perc_lis 
        self.value_lis = []
        self.category_name_lis = name_lis
        self.category_obj_lis = []
 
       
# obtains and stores categories 
    def get_class_cat(self):

        # creates category objects and adds them to a list
        for i in range(len(self.category_name_lis)):
            self.category_obj_lis.append("")                                                     
            self.category_obj_lis[i] = Category(self.category_name_lis[i])


# actual transaction logic, displays transaction details, adds the data from each transaction to value_lis
    def transaction(self):
        self.dep_loc = dep_loc
        self.dep_amt = dep_amt
        self.value_lis = self.dep_loc

        for index, y in enumerate(self.category_obj_lis):
            if username_var in user_dict:
                try:
                    y.max = user_dict[username_var][dep_loc][0]
                    y.amt = user_dict[username_var][dep_loc][1]
                except UnboundLocalError:
                    pass
            else:
                y.max = (y.perc_lis[index] / 100) * y.monthly_income 
            if self.dep_loc in self.category_name_lis[index]:
                self.dep_amt = dep_amt
                pass
            else:
                self.dep_amt = 0
                pass 
            y.amt += self.dep_amt
            y.left = y.max - y.amt
            self.max = y.max
            self.amt = y.amt
            self.left = y.left
            self.value_lis = [y.max, y.amt, y.left, y.perc_lis[index]]
            self.value_lis.extend([y.max, y.amt, y.left, y.perc_lis[index]])
            if len(self.value_lis) > 4:
                del self.value_lis[:4]

            if name_lis[index] == dep_loc:
                self.category_dict =  get_category_data(name_lis[index], self.value_lis)
            elif place_holder_var == 0:
                lis = [y.max, 0, y.max, y.perc_lis[index]]
                self.category_dict =  get_category_data(name_lis[index], lis)
            if self.dep_amt != 0:
                print(f"Amount spent on {y.name}: ${y.amt} \nAmount left to spend: ${round(y.left,2)}")


# Class that defines a category object

class Category():
    def __init__(self, name):
        self.name = name
        self.perc = 0
        self.amt = 0
        self.left = 0
        self.max = 0
        self.perc_lis = perc_lis
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
name_lis = []
def get_cat(cat_num):
    num = 0
    while num < cat_num:
        num += 1
        cat = input(f"Catetgory {num}: ")
        name_lis.append(cat)
    return name_lis

# retrieves and adds each categories percentages to a list
perc_lis = []
def gather_perc():
    print("Enter desired percentage of income spent for each category (do not include %): ")
    x = 0
    y = 0
    while x < len(name_lis):
        y = 0
        for i in name_lis:
            try:
                if y == 0:
                    perc = float(input(f"{i}: "))
            except ValueError:
                    print("Invalid Input : Please enter a number")
                    y = 1
                    continue
            if y == 0:
                perc_lis.append(perc)
        # makes sure the percentages sum from 95-105  
            if len(perc_lis) == cat_num:
                if sum(perc_lis) not in range(95, 105):
                    print("Invalid Input : Must add to 100%")
                    perc_lis.clear()
                    x = 0
                    continue
                else:
                    return perc_lis


# gets the deposit location
def get_loc():

    while True:
        try:
            dep_loc = ""
            dep_loc = input("Where would you like to deposit? ")
            if dep_loc not in name_lis:
                print("Invalid Input : Must be valid category")
                continue
            else:
                return dep_loc
        except ValueError:
            print("Invalid Input : Must be valid category")
            continue

# gets the deposit amount
def get_amt():
    while True:
        try:
            dep_amt = 0
            dep_amt = float(input("Deposit amount: "))
            return dep_amt
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
def get_category_data(dep_loc_var, value_lis_var):
    category_dict[dep_loc_var] = value_lis_var
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
        dep_loc = get_loc()
        dep_amt = get_amt()
        username = Budget(inc, username_var)   
        username.get_class_cat()
        value_lis = username.transaction()
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
        dep_loc = get_loc()
        dep_amt = get_amt()
        value_lis = username.transaction()
        store_user()
        continue

    elif done == 4:
        print("Thank you")
        break
    else:
        print("Invalid Input")
        continue

