# system packages 
from sys import argv

# external packages 
import numpy as np
import pandas as pd
from simple_term_menu import TerminalMenu
import uuid
from random_username.generate import generate_username
from rich import print as rprint

# import schema 
from schema import *

# databases 
# store customer information
def create_customer_database():
    customer_columns = ['CustomerID','customerUserName','customerPassword','customer_bust','customer_waist','customer_hip']
    customers = pd.DataFrame(columns=customer_columns)
    customers['CustomerID'] = customers.index
    customers.to_csv('customers.csv',sep=',',index=False,encoding='utf-8')
    return customers

def update_customer_database():
    customers.to_csv('customers.csv',sep=',',index=False,encoding='utf-8')
    return customers

customers = create_customer_database()

# store retailer information
def create_retailer_database():
    retailer_columns = ['retailerID','sizeChartID','retailerName']
    retailers = pd.DataFrame(columns=retailer_columns)
    retailers['retailerID'] = retailers.index
    retailers.to_csv('retailers.csv',sep=',',index=False,encoding='utf-8')
    return retailers

def populate_retailer_database():
    retailers = pd.read_csv("retailers_data.csv")
    return retailers

def update_retailer_database():
    retailers.to_csv('retailers.csv',sep=',',index=False,encoding='utf-8')
    return retailers

retailers = create_retailer_database()
retailers = populate_retailer_database()
retailers = update_retailer_database()

# store sizing information 

def create_sizing_database():
    sizing_columns = ['sizeID','sizeChartID','sizeName','size_bust','size_waist','size_hip']
    sizing = pd.DataFrame(columns=sizing_columns)
    sizing['sizeID'] = sizing.index
    sizing.to_csv('sizing.csv',sep=',',index=False,encoding='utf-8')
    return sizing

def populate_sizing_database():
    sizing = pd.read_csv("sizing_data.csv")
    return sizing

def update_sizing_database():
    sizing.to_csv('sizing.csv',sep=',',index=False,encoding='utf-8')
    return sizing

sizing = create_sizing_database()
sizing = populate_sizing_database()
sizing = update_sizing_database()

def view_sizing():
    sizing_snapshot = rprint(sizing)
    return sizing_snapshot

# key features 
# feature 1 : find size

def find_size(Body):
    print('Enter the name of the retailer. We will find your size!')
    customer_details = Customer
    customer_measurements = Body(customer_details.customerID,customer_details.bust,customer_details.waist,customer_details.hip)
    retailer_name_input = input("Retailer Name: ")
    selected_size_chart_ID = find_sizes_by_retailer(retailer_name_input)
    size_match = find_size_within_retailer(selected_size_chart_ID,customer_measurements)
    print('We found your size!')
    print(f'At {retailer_name_input} the size which would match you best is {size_match}')
    return size_match

# feature 2 : check fit 

def check_fit_dialogue(Customer):
    print('Enter the retailer and size. We will check your fit!')
    customer_details = Customer
    customer_measurements = Body(customer_details.customerID,customer_details.bust,customer_details.waist,customer_details.hip)
    retailer_name_input = input("Retailer Name: ")
    size_name_input = input("Size Name: ")
    fit = check_fit(customer_measurements,retailer_name_input,size_name_input)
    if fit == True:
        print('We checked the fit!')
        print(f'{size_name_input} at {retailer_name_input} is a good fit!')
    else: 
        print('We checked the fit!')
        print(f'{size_name_input} at {retailer_name_input} is not a good fit!')
    return fit

def check_fit(customer_measurements,retailerName,sizeName):
    a = get_size_id(retailerName,sizeName)
    b = get_dimensions_of_size(a)
    c = evaluate_fit(customer_measurements,b)
    return c


# feature 3 : convert size 

def convert_size():
    print('Enter the retailers and size name. Then enter the name of the retailer you would like the size to be converted to. We will find your size!')
    current_retailer_name_input = input("Retailer Name: ")
    size_name_input = input("Size Name: ")
    #size_id = get_size_id(current_retailer_name_input,size_name_input)
    size_id = '111'
    size_dimensions = get_dimensions_of_size(size_id)
    new_retailer_name_input = input("Retailer Name: ")
    size_match = convert_size_between_retailers(size_dimensions,new_retailer_name_input)
    print('We found your size!')
    print(f'A {size_name_input} at {current_retailer_name_input} is equivalent to a {size_match} at {new_retailer_name_input}')
    return size_match


# id generation

def generate_id():
    generated_id = uuid.uuid4()
    return generated_id

# username generation 

def generate_new_username():
    generated_username = generate_username()
    return generated_username

# create new customer

def create_customer():
    id_input = generate_id()
    username_input = generate_new_username()
    print(f'Your username will be {username_input}')
    #password_input = input("password: ")
    password_input = ""
    newCustomer = Customer(id_input,username_input,password_input)
    body_information = collect_body_measurements(id_input)
    customers.loc[id_input] = [id_input,username_input,password_input,body_information.bust,body_information.waist,body_information.hip]
    update_customer_database()
    return [newCustomer,body_information]

# find existing customer 

def find_customer(customerUserName):
    a = customers.query('(customerUserName == @customerUserName)')
    b = a.head()
    while True:
        try:
            customer_match = b['customerUserName'].values[0]
            customer_exists = True
            break
        except Exception:
            print("Customer not found")
            customer_exists = False
            break
    return customer_exists

# customer 

def check_customer():
    name_input = str(input("Enter your username: "))
    existing_customer_search_result = find_customer(name_input)
    if existing_customer_search_result == False:
        current_customer = create_customer()
        print(current_customer)
    elif existing_customer_search_result == True:
        # populate current customer object from database
        current_customer = Customer("","nameinput","")
    return current_customer

# collect dimensions

measurement_input_warning = "Please enter the measurement in centimetres (e.g. 75.5)"

measurement_range_warning = "Hmm that number seems outside the usual range (between 0 and 500), double check your measurements"

def collect_bust_measurement():
    while True:
        try:
            bust_measurement = float(input("Bust (in centimetres): "))
            if bust_measurement < 0 or bust_measurement > 300:
                print(f"{measurement_range_warning}")
            else:
                break
        except Exception:
            print(f"{measurement_input_warning}")
    return bust_measurement

def collect_waist_measurement():
    while True:
        try:
            waist_measurement = float(input("Waist (in centimetres): "))
            if waist_measurement < 0 or waist_measurement > 300:
                print(f"{measurement_range_warning}")
            else:
                break
        except Exception:
            print(f"{measurement_input_warning}")
    return waist_measurement

def collect_hip_measurement():
    while True:
        try:
            hip_measurement = float(input("Hip (in centimetres): "))
            if hip_measurement < 0 or hip_measurement > 300:
                print(f"{measurement_range_warning}")
            else:
                break
        except Exception:
            print(f"{measurement_input_warning}")
    return hip_measurement

# collect customer measurements

def collect_body_measurements(customerId): 
    customer_bust = collect_bust_measurement()
    customer_waist = collect_waist_measurement()
    customer_hip = collect_hip_measurement()
    body_information = Body (customerId,customer_bust,customer_waist,customer_hip)
    customers.at[customerId,'customer_bust'] = customer_bust
    customers.at[customerId,'customer_waist'] = customer_waist
    customers.at[customerId,'customer_hip'] = customer_hip
    update_customer_database()
    return body_information

def find_body_measurements(customerUserName):
    a = customers.query('(customerUserName == @customerUserName)')
    b = a.head()
    customerID = b['customerID'].values[0]
    customer_bust = b['customer_bust'].values[0]
    customer_waist = b['customer_waist'].values[0]
    customer_hip = b['customer_hip'].values[0]
    body_information = Body (customerID,customer_bust,customer_waist,customer_hip)
    return body_information

# add new retailer to database

def create_retailer():
    id_input = generate_id()
    name_input = input("Retailer Name: ")
    size_chart_id = generate_id()
    newRetailer = Retailer (size_chart_id,id_input,name_input)
    retailers.loc[id_input] = [id_input,size_chart_id,name_input]
    update_retailer_database()
    return newRetailer
    
# add new size to database

def create_size():
    name_input = input("Size Name: ")
    id_input = generate_id()
    retailer_name_input = input("Retailer Name: ")
    a = retailers.query('(RetailerName == retailer_name_input)')
    b = a.head()
    size_chart_id = b['sizeChartID'].values[0]
    size_bust = collect_bust_measurement()
    size_waist = collect_waist_measurement()
    size_hip = collect_hip_measurement()
    newSize = Size(name_input,size_chart_id,id_input,size_bust,size_waist,size_hip)
    sizing.loc[id_input] = [id_input,size_chart_id,name_input,size_bust,size_waist,size_hip]
    update_sizing_database()
    return newSize

#size_measurements = createSize()

#new_dimensions = Dimensions(size_measurements.bust,size_measurements.waist,size_measurements.hip)

# evaluate fit

def evaluate_fit(customer,dimensions):
    fit = True  
    if customer.bust == dimensions.bust and customer.waist == dimensions.waist and customer.hip == dimensions.hip:
        fit = True 
    else: fit = False
    return fit

#fit_determination = evaluateFit(customer_measurements,new_dimensions)


# search 

def find_sizes_by_retailer(retailerName):
    val1 = retailers.loc[retailers['retailerName']==retailerName]
    val2 = val1['sizeChartID'].values[0]
    return val2

####
def find_size_within_retailer(sizeChartID,Dimensions):
    w = sizeChartID
    x = Dimensions.bust
    y = Dimensions.waist
    z = Dimensions.hip
    a = sizing.query('sizeChartID==@w and size_bust == @x and size_waist == @y and size_hip == @z')
    b = a.head()
    size_match = b['sizeName'].values[0]
    return size_match

# retrieval 
####
def get_size_id(retailerName,sizeName):
    a = find_sizes_by_retailer(retailerName)
    b = sizing.query('(sizeChartID == @a) and (sizeName == @sizeName)')
    c = b.head()
    size_id_match = c['sizeID'].values[0]
    return size_id_match


def get_dimensions_of_size(sizeID):
    x = float(sizeID)
    a = sizing.query('(sizeID==@sizeID)')
    b = a.head()
    bust = b[b['size_bust']]
    waist = b[b['size_waist']]
    hip = b[b['size_hip']]
    size_dimensions = Dimensions(bust,waist,hip)
    return size_dimensions

# conversion  

def convert_size_between_retailers(Dimensions,retailerName):
    a = float(find_sizes_by_retailer(retailerName))
    b = find_size_within_retailer(a,Dimensions)
    return b

# interface
# main menu

def main():
    options = ["0 : Add Profile","1 : Find Size ", "2 : Check Fit", "3 : Convert Size","4 : Add Retailer","5 : Add Size","6 : View All Sizes","7 : Quit"]
    terminal_menu = TerminalMenu(options,title='Size O Matic')
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    selection = options[menu_entry_index]
    if selection == options[0]:
        current_customer = create_customer()
        main()
    elif selection == options[1]:
        current_customer = check_customer() 
        find_size(current_customer)
        main()
    elif selection == options[2]:
        current_customer = check_customer()
        check_fit_dialogue(current_customer)
        main()
    elif selection == options[3]:
        convert_size()
        main()
    elif selection == options[4]:
        create_retailer()
        main()
    elif selection == options[5]:
        # check retailer -- pass retailer object 
        create_size()
        main()
    elif selection == options[6]:
        #view sizing database 
        view_sizing()
        main()
    elif selection == options[7]:
        quit()

if __name__ == "__main__":
    main()

