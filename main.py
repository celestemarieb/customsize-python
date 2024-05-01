# system packages 

# external packages 

import numpy as np
import pandas as pd
from simple_term_menu import TerminalMenu

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

# key features 
# feature 1 : find size

def find_size():
    print('Enter your details and the name of the retailer. We will find your size!')
    # New Customer 
    customer_details = create_customer()
    customer_bust = collect_bust_measurement()
    customer_waist = collect_waist_measurement()
    customer_hip = collect_hip_measurement()
    customer_measurements = collect_body_measurements(customer_details.customerID,customer_bust,customer_waist,customer_hip)
    #Existing Customer
    #customer_details = find_customer()
    #customer_information = find_body_measurements(customer_details[1])
    retailer_name_input = input("Retailer Name: ")
    selected_size_chart_ID = find_sizes_by_retailer(retailer_name_input)
    size_match = find_size_within_retailer(selected_size_chart_ID,customer_measurements)
    print('We found your size!')
    print(f'At {retailer_name_input} the size which would match you best is {size_match}')
    return size_match

# feature 2 : check fit 

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

# customer management 
# create new customer

def create_customer():
    id_input = input("User ID: ")
    username_input = input("username: ")
    password_input = input("password: ")
    newCustomer = Customer(id_input,username_input,password_input)
    customers.loc[id_input] = [id_input,username_input,password_input,"","",""]
    update_customer_database()
    return newCustomer

# find existing customer 

def find_customer():
    customer_exists = True
    id_input = input("User ID: ")
    a = customers.query('(customerID == id_input)')
    b = a.head()
    customer_match = b['customerID'].values[0]
    if customer_match == id_input:
        customer_exists = True
    else: customer_exists = False
    return [customer_exists,customer_match]

# collect dimensions

def collect_bust_measurement():
    bust_measurement = input("Bust: ")
    return bust_measurement

def collect_waist_measurement():
    waist_measurement = input("Waist: ")
    return waist_measurement

def collect_hip_measurement():
    hip_measurement = input("Hip: ")
    return hip_measurement

# collect customer measurements

def collect_body_measurements(customerId, customer_bust,customer_waist,customer_hip): 
    bodyInformation = Body (customerId,customer_bust,customer_waist,customer_hip)
    customers.at[customerId,'customer_bust'] = customer_bust
    customers.at[customerId,'customer_waist'] = customer_waist
    customers.at[customerId,'customer_hip'] = customer_hip
    update_customer_database()
    return bodyInformation

def find_body_measurements(customerID):
    a = customers.query('(customerID == customerID)')
    b = a.head()
    customerID = b['customerID'].values[0]
    customer_bust = b['customer_bust'].values[0]
    customer_waist = b['customer_waist'].values[0]
    customer_hip = b['customer_hip'].values[0]
    bodyInformation = Body (customerID,customer_bust,customer_waist,customer_hip)
    return bodyInformation

# create new retailer 

def create_retailer():
    id_input = input("Retailer ID: ")
    name_input = input("Retailer Name: ")
    size_chart_id = input("Size Chart ID:")
    newRetailer = Retailer (size_chart_id,id_input,name_input)
    retailers.loc[id_input] = [id_input,size_chart_id,name_input]
    update_retailer_database()
    return newRetailer

#retailerInformation = createRetailer()

# create size chart  

def create_size_chart():
    id_input = input("Size Chart ID: ")
    size_names_input = []
    newSizeChart = SizeChart (id_input,size_names_input)
    return newSizeChart 

#sizeChartInformation = createSizeChart()

def get_sizechartID(sizeChart):
    sizeChartID = sizeChart.sizeChartID
    return sizeChartID

#newSizeChartID = getSizeChartID(sizeChartInformation)
    
# create size 

def create_size():
    name_input = input("Size Name: ")
    id_input = input("Size ID: ")
    sizeChartInformation.sizeNames.append(name_input)
    size_bust = collect_bust_measurement()
    size_waist = collect_waist_measurement()
    size_hip = collect_hip_measurement()
    newSize = Size(name_input,newSizeChartID,id_input,size_bust,size_waist,size_hip)
    sizing.loc[id_input] = [id_input,newSizeChartID,name_input,size_bust,size_waist,size_hip]
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


#search functions

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

# retrieval functions
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

# conversion functions 

def convert_size_between_retailers(Dimensions,retailerName):
    a = float(find_sizes_by_retailer(retailerName))
    b = find_size_within_retailer(a,Dimensions)
    return b

# interface
# main menu

def main():
    options = ["1 : Find Size ", "2 : Check Fit", "3 : Convert Size","4 : Quit"]
    terminal_menu = TerminalMenu(options,title='The Size Machine')
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

    selection = options[menu_entry_index]
    if selection == options[0]:
        find_size()
    elif selection == options[1]:
        check_fit()
    elif selection == options[2]:
        convert_size()
    elif selection == options[3]:
        quit()

if __name__ == "__main__":
    main()

