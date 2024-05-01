# system packages 

# external packages 

import numpy as np
import pandas as pd
from simple_term_menu import TerminalMenu

# import schema 

from schema import *

# databases 

# store customer information

def createCustomerDatabase():
    customer_columns = ['CustomerID','customerUserName','customerPassword','customer_bust','customer_waist','customer_hip']
    customers = pd.DataFrame(columns=customer_columns)
    customers['CustomerID'] = customers.index
    customers.to_csv('customers.csv',sep=',',index=False,encoding='utf-8')
    return customers

def updateCustomerDatabase():
    customers.to_csv('customers.csv',sep=',',index=False,encoding='utf-8')
    return customers

customers = createCustomerDatabase()

# store retailer information

def createRetailerDatabase():
    retailer_columns = ['retailerID','sizeChartID','retailerName']
    retailers = pd.DataFrame(columns=retailer_columns)
    retailers['retailerID'] = retailers.index
    retailers.to_csv('retailers.csv',sep=',',index=False,encoding='utf-8')
    return retailers

def populateRetailerDatabase():
    retailers = pd.read_csv("retailers_data.csv")
    return retailers

def updateRetailerDatabase():
    retailers.to_csv('retailers.csv',sep=',',index=False,encoding='utf-8')
    return retailers

retailers = createRetailerDatabase()
retailers = populateRetailerDatabase()
retailers = updateRetailerDatabase()

# store sizing information 

def createSizingDatabase():
    sizing_columns = ['sizeID','sizeChartID','sizeName','size_bust','size_waist','size_hip']
    sizing = pd.DataFrame(columns=sizing_columns)
    sizing['sizeID'] = sizing.index
    sizing.to_csv('sizing.csv',sep=',',index=False,encoding='utf-8')
    return sizing

def populateSizingDatabase():
    sizing = pd.read_csv("sizing_data.csv")
    return sizing

def updateSizingDatabase():
    sizing.to_csv('sizing.csv',sep=',',index=False,encoding='utf-8')
    return sizing

sizing = createSizingDatabase()
sizing = populateSizingDatabase()
sizing = updateSizingDatabase()

# key features 
# feature 1 

def find_size():
    print('Enter your user id and the name of the retailer. We will find your size!')
    customer_details = findCustomer()
    customerInformation = findBodyMeasurements(customer_details[1])
    retailer_name_input = input("Retailer Name: ")
    selected_size_chart_ID = find_sizes_by_retailer(retailer_name_input)
    size_match = find_size_within_retailer(selected_size_chart_ID,customerInformation)
    print('We found your size!')
    print(f'At {retailer_name_input} the size which would match you best is {size_match}')
    return size_match

# feature 2 

def check_fit():
    pass

# feature 3 

def convert_size():
    pass

# create new customer

def createCustomer():
    id_input = input("User ID: ")
    username_input = input("username: ")
    password_input = input("password: ")
    newCustomer = Customer(id_input,username_input,password_input)
    customers.loc[id_input] = [id_input,username_input,password_input,"","",""]
    updateCustomerDatabase()
    return newCustomer

# find existing customer 

def findCustomer():
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

def collectBustMeasurement():
    bust_measurement = input("Bust: ")
    return bust_measurement

def collectWaistMeasurement():
    waist_measurement = input("Waist: ")
    return waist_measurement

def collectHipMeasurement():
    hip_measurement = input("Hip: ")
    return hip_measurement

# collect customer measurements

def collectBodyMeasurements(customerId, customer_bust,customer_waist,customer_hip): 
    bodyInformation = Body (customerId,customer_bust,customer_waist,customer_hip)
    customers.at[customerId,'customer_bust'] = customer_bust
    customers.at[customerId,'customer_waist'] = customer_waist
    customers.at[customerId,'customer_hip'] = customer_hip
    updateCustomerDatabase()
    return bodyInformation

def findBodyMeasurements(customerID):
    a = customers.query('(customerID == customerID)')
    b = a.head()
    customerID = b['customerID'].values[0]
    customer_bust = b['customer_bust'].values[0]
    customer_waist = b['customer_waist'].values[0]
    customer_hip = b['customer_hip'].values[0]
    bodyInformation = Body (customerID,customer_bust,customer_waist,customer_hip)
    return bodyInformation

# collect new customer information

#customerInformation = createCustomer()
#customer_bust = collectBustMeasurement()
#customer_waist = collectWaistMeasurement()
#customer_hip = collectHipMeasurement()
#customer_measurements = collectBodyMeasurements(customerInformation.customerID,customer_bust,customer_waist,customer_hip)

# create new retailer 

def createRetailer():
    id_input = input("Retailer ID: ")
    name_input = input("Retailer Name: ")
    size_chart_id = input("Size Chart ID:")
    newRetailer = Retailer (size_chart_id,id_input,name_input)
    retailers.loc[id_input] = [id_input,size_chart_id,name_input]
    updateRetailerDatabase()
    return newRetailer

#retailerInformation = createRetailer()

# create size chart  

def createSizeChart():
    id_input = input("Size Chart ID: ")
    size_names_input = []
    newSizeChart = SizeChart (id_input,size_names_input)
    return newSizeChart 

#sizeChartInformation = createSizeChart()

def getSizeChartID(sizeChartInformation):
    sizeChartID = sizeChartInformation.sizeChartID
    return sizeChartID

#newSizeChartID = getSizeChartID(sizeChartInformation)
    
# create size 

def createSize():
    name_input = input("Size Name: ")
    id_input = input("Size ID: ")
    sizeChartInformation.sizeNames.append(name_input)
    size_bust = collectBustMeasurement()
    size_waist = collectWaistMeasurement()
    size_hip = collectHipMeasurement()
    newSize = Size(name_input,newSizeChartID,id_input,size_bust,size_waist,size_hip)
    sizing.loc[id_input] = [id_input,newSizeChartID,name_input,size_bust,size_waist,size_hip]
    updateSizingDatabase()
    return newSize

#size_measurements = createSize()

#new_dimensions = Dimensions(size_measurements.bust,size_measurements.waist,size_measurements.hip)

# evaluate fit

def evaluateFit(customer,dimensions):
    fit = True  
    if customer.bust == dimensions.bust and customer.waist == dimensions.waist and customer.hip == dimensions.hip:
        fit = True 
    else: fit = False
    return fit

#fit_determination = evaluateFit(customer_measurements,new_dimensions)


# feature 1: find size

def find_sizes_by_retailer(retailerName):
    val1 = retailers.loc[retailers['retailerName']==retailerName]
    val2 = val1['sizeChartID'].values[0]
    return val2


#selected_size_chart = find_sizes_by_retailer(retailerInformation.retailerName)

def find_size_within_retailer(sizeChartID,Body):
    w = float(sizeChartID)
    x = float(Body.bust)
    y = float(Body.waist)
    z = float(Body.hip)
    a = sizing.query('(sizeChartID==@w) and (size_bust == @x) and (size_waist == @y) and (size_hip == @z)')
    b = a.head()
    size_match = b['sizeName'].values[0]
    return size_match

#print(find_size_within_retailer(selected_size_chart,customer_measurements))

# feature 2: check fit

def check_fit(customer_measurements,retailerName,sizeName):
    a = get_size_id(retailerName,sizeName)
    b = get_dimensions_of_size(a)
    c = evaluateFit(customer_measurements,b)
    return c

# feature 3: convert size

def get_size_id(retailerName,sizeName):
    a = find_sizes_by_retailer(retailerName)
    b = sizing.query('(sizeChartID == @a) and (sizeName == @sizeName)')
    c = b.head()
    size_id_match = c['sizeID'].values[0]
    return size_id_match

#a = get_size_id(retailerInformation.retailerName,size_measurements.sizeName)
#print(a)

def get_dimensions_of_size(sizeID):
    x = float(sizeID)
    a = sizing.query('(sizeID==@sizeID)')
    b = a.head()
    bust = b[b['size_bust']]
    waist = b[b['size_waist']]
    hip = b[b['size_hip']]
    size_dimensions = Dimensions(bust,waist,hip)
    return size_dimensions

#b = get_dimensions_of_size(a)
#print(b)

def convert_size_between_retailers(dimensions,retailerName):
    a = float(find_sizes_by_retailer(retailerName))
    b = find_size_within_retailer(a,customer_measurements=dimensions)
    return b

#c = convert_size_between_retailers(b,retailerInformation.retailerName)

# interface 

# main menu

def main():
    options = ["1 : Find Size ", "2 : Check Fit", "3 : Convert Size","4 : Quit"]
    terminal_menu = TerminalMenu(options,title='The Size Machine')
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

    selection = options[menu_entry_index]
    if selection == options[0]:
        found_size = find_size()
        print(found_size)
    elif selection == options[1]:
        fit_check = check_fit()
        print(fit_check)
    elif selection == options[2]:
        converted_size = convert_size()
        convert_size()
    elif selection == options[3]:
        quit()


if __name__ == "__main__":
    main()

