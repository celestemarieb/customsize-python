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
customers = update_customer_database()

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

def find_size(customerID):
    print('Enter the name of the retailer. We will find your size!')
    # query DB to find measurements
    a = customers.loc[(customers['CustomerID'] == customerID),'customer_bust']
    bust_measurement = a.iloc[0]
    b = customers.loc[(customers['CustomerID'] == customerID),'customer_waist']
    waist_measurement = b.iloc[0]
    c = customers.loc[(customers['CustomerID'] == customerID),'customer_hip']
    hip_measurement = c.iloc[0]
    customer_dimensions = Dimensions(bust_measurement,waist_measurement,hip_measurement)
    retailer_name_input = input("Retailer Name: ")
    selected_size_chart_ID = find_sizes_by_retailer(retailer_name_input)
    size_match = find_size_within_retailer(selected_size_chart_ID,customer_dimensions)
    print('We found your size!')
    print(f'At {retailer_name_input} the size which would match you best is {size_match}')
    return size_match

# feature 2 : check fit 

def check_fit_dialogue(customerID):
    print('Enter the retailer and size. We will check your fit!')
    a = customers.loc[customers['CustomerID'] == customerID,'customerUserName']
    customer_user_name = a.iloc[0]
    customer_measurements = find_body_measurements(customer_user_name)
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
    while True:
        try:
            size_id = get_size_id(current_retailer_name_input,size_name_input)
            size_dimensions = get_dimensions_of_size(size_id)
            break
        except Exception:
            print("Add this size to our database to complete conversion")
            break
    new_retailer_name_input = input("Retailer Name: ")
    while True:
        try:
            size_match = convert_size_between_retailers(size_dimensions,new_retailer_name_input)
            print('We found your size!')
            print(f'{size_name_input} at {current_retailer_name_input} is equivalent to a {size_match} at {new_retailer_name_input}')
            break
        except Exception:
            print('An converted size could not be found! Please try again later')
            size_match = 'nil'
            break
    return size_match


# id generation

def generate_id():
    generated_id = uuid.uuid4()
    return generated_id

# username generation 

def generate_new_username():
    generated_username = generate_username()
    return generated_username

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
    a = customers.loc[customers['customerUserName'] == customerUserName,'CustomerID']
    customerID = a.iloc[0]
    b = customers.loc[customers['customerUserName'] == customerUserName,'customer_bust']
    customer_bust = b.iloc[0]
    c = customers.loc[customers['customerUserName'] == customerUserName,'customer_waist']
    customer_waist = c.iloc[0]
    d = customers.loc[customers['customerUserName'] == customerUserName,'customer_hip']
    customer_hip = d.iloc[0]
    body_information = Body (customerID,customer_bust,customer_waist,customer_hip)
    return body_information

# create new customer

def create_customer():
    id_input = generate_id()
    username_input = generate_new_username()
    print(f'Your username will be {username_input}')
    #password_input = input("password: ")
    password_input = ""
    new_customer = Customer(id_input,username_input,password_input)
    customers.loc[id_input] = [id_input,username_input,password_input,"","",""]
    update_customer_database()
    return new_customer.customerID


# find existing customer 

def find_customer(customerUserName):
    while True:
        try:
            a = customers.loc[customers['customerUserName'] == customerUserName,'customerUserName']
            customer_match = a.iloc[0]
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
        current_customer_id = create_customer()
        collect_body_measurements(current_customer_id)
    elif existing_customer_search_result == True:
        # populate current customer object from database
        current_customer_id = customers.getvalue(name_input,'CustomerID')
    return current_customer_id

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
    while True:
        try:
            a = retailers.loc[(retailers['retailerName'] == retailer_name_input)]
            b = a.head()
            size_chart_id = b['sizeChartID'].values[0]
            break
        except Exception:
            print("Retailer not found, please add retailer details before creating a size")
            new_retailer = create_retailer()
            size_chart_id = new_retailer.sizeChartID
    size_bust = collect_bust_measurement()
    size_waist = collect_waist_measurement()
    size_hip = collect_hip_measurement()
    newSize = Size(name_input,size_chart_id,id_input,size_bust,size_waist,size_hip)
    sizing.loc[id_input] = [id_input,size_chart_id,name_input,size_bust,size_waist,size_hip]
    update_sizing_database()
    return newSize

# evaluate fit

def evaluate_fit(customer,dimensions):
    fit = True  
    if customer.bust == dimensions.bust and customer.waist == dimensions.waist and customer.hip == dimensions.hip:
        fit = True 
    else: fit = False
    return fit

# search 

def find_sizes_by_retailer(retailerName):
    size_chart_ID = 0
    while True:
        try:
            filtered_values = retailers.loc[retailers['retailerName']==retailerName]
            size_chart_ID = filtered_values['sizeChartID'].values[0]
            break
        except Exception:
            print("No sizes available for this retailer")
            size_chart_ID = 0
            break
    return size_chart_ID

def find_size_within_retailer(sizeChartID,Dimensions):
    while True:
        try:
            a = sizing.loc[(sizing['sizeChartID'] == sizeChartID) & (sizing['size_bust'] == Dimensions.bust) & (sizing['size_waist'] == Dimensions.waist) & (sizing['size_hip'] == Dimensions.hip),'sizeName']
            size_match = a.iloc[0]
            break
        except Exception:
            print("Match could not be found")
            main()
    return size_match

# retrieval 

def get_size_id(retailerName,sizeName):
    a = find_sizes_by_retailer(retailerName)
    b = sizing.query('(sizeChartID == @a) and (sizeName == @sizeName)')
    c = b.head()
    size_id_match = c['sizeID'].values[0]
    return size_id_match

def get_dimensions_of_size(sizeID):
    a = sizing.loc[(sizing['sizeID'] == sizeID),'size_bust']
    bust_measurement = a.iloc[0]
    b = sizing.loc[(sizing['sizeID'] == sizeID),'size_waist']
    waist_measurement = b.iloc[0]
    c = sizing.loc[(sizing['sizeID'] == sizeID),'size_hip']
    hip_measurement = c.iloc[0]
    size_dimensions = Dimensions(bust_measurement,waist_measurement,hip_measurement)
    return size_dimensions

# conversion  

def convert_size_between_retailers(Dimensions,retailerName):
    a = find_sizes_by_retailer(retailerName)
    b = find_size_within_retailer(a,Dimensions)
    return b

#size_measurements = create_size()

#new_dimensions = Dimensions(size_measurements.bust,size_measurements.waist,size_measurements.hip)

#size_match = convert_size_between_retailers(new_dimensions,'asos')

# interface
# main menu

def main():
    options = ["0 : Add Profile","1 : Find Size ", "2 : Check Fit", "3 : Convert Size","4 : Add Retailer","5 : Add Size","6 : View All Sizes","7 : Quit"]
    terminal_menu = TerminalMenu(options,title='Size O Matic')
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    selection = options[menu_entry_index]
    if selection == options[0]:
        current_customer_id = create_customer()
        current_customer_measurements = collect_body_measurements(current_customer_id)
        main()
    elif selection == options[1]:
        current_customer_id = check_customer()
        find_size(current_customer_id)
        main()
    elif selection == options[2]:
        current_customer_id = check_customer()
        check_fit_dialogue(current_customer_id)
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

