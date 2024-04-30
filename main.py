# system packages 

# external packages 

import typer
import numpy as np
import pandas as pd
from rich.console import Console
from rich.table import Table

# import schema 

from schema import *

# import functions 

from functions import *

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

# create new customer

def createCustomer():
    id_input = input("User ID: ")
    username_input = input("username: ")
    password_input = input("password: ")
    newCustomer = Customer(id_input,username_input,password_input)
    customers.loc[id_input] = [id_input,username_input,password_input,"","",""]
    updateCustomerDatabase()
    return newCustomer

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

# collect new customer information

customerInformation = createCustomer()
customer_bust = collectBustMeasurement()
customer_waist = collectWaistMeasurement()
customer_hip = collectHipMeasurement()
customer_measurements = collectBodyMeasurements(customerInformation.customerID,customer_bust,customer_waist,customer_hip)

# create new retailer 

def createRetailer():
    id_input = input("Retailer ID: ")
    name_input = input("Retailer Name: ")
    size_chart_id = input("Size Chart ID:")
    newRetailer = Retailer (size_chart_id,id_input,name_input)
    retailers.loc[id_input] = [id_input,size_chart_id,name_input]
    updateRetailerDatabase()
    return newRetailer

retailerInformation = createRetailer()

# create size chart  

def createSizeChart():
    id_input = input("Size Chart ID: ")
    size_names_input = []
    newSizeChart = SizeChart (id_input,size_names_input)
    return newSizeChart 

sizeChartInformation = createSizeChart()

def getSizeChartID(sizeChartInformation):
    sizeChartID = sizeChartInformation.sizeChartID
    return sizeChartID

newSizeChartID = getSizeChartID(sizeChartInformation)
    
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

size_measurements = createSize()

new_dimensions = Dimensions(size_measurements.bust,size_measurements.waist,size_measurements.hip)

# evaluate fit

def evaluateFit(customer,dimensions):
    fit = True  
    if customer.bust == dimensions.bust and customer.waist == dimensions.waist and customer.hip == dimensions.hip:
        fit = True 
    else: fit = False
    return fit

fit_determination = evaluateFit(customer_measurements,new_dimensions)

print(fit_determination)


# feature 1: find size

def find_sizes_by_retailer(retailerName):
    val1 = retailers.loc[retailers['retailerName']==retailerName]
    val2 = val1['sizeChartID'].values[0]
    return val2


selected_size_chart = float(find_sizes_by_retailer(retailerInformation.retailerName))

def find_size_within_retailer(sizeChartID,customer_measurements):
    w = float(sizeChartID)
    x = float(customer_measurements.bust)
    y = float(customer_measurements.waist)
    z = float(customer_measurements.hip)
    a = sizing.query('(sizeChartID==@w) and (size_bust == @x) and (size_waist == @y) and (size_hip == @z)')
    b = a.head()
    size_match = b['sizeName'].values[0]
    return size_match

print(find_size_within_retailer(selected_size_chart,customer_measurements))

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

a = get_size_id(retailerInformation.retailerName,size_measurements.sizeName)
print(a)

def get_dimensions_of_size(sizeID):
    x = float(sizeID)
    a = sizing.query('(sizeID==@sizeID)')
    b = a.head()
    bust = b[b['size_bust']]
    waist = b[b['size_waist']]
    hip = b[b['size_hip']]
    size_dimensions = Dimensions(bust,waist,hip)
    return size_dimensions

b = get_dimensions_of_size(a)
print(b)

def convert_size(dimensions,retailerName):
    a = float(find_sizes_by_retailer(retailerName))
    b = find_size_within_retailer(a,customer_measurements=dimensions)
    return b

c =convert_size(b,retailerInformation.retailerName)

# interface : 

#console = Console()

#app = typer.Typer()

#@app.command(short_help='adds user')
#def add(Customer:str):
    #typer.echo(f"adding {customerInformation}")

#@app.command(short_help='shows all sizing')
#def show(sizing:str):
    #console.print("[bold magenta]Sizing Database[/bold magenta]!")

    #table = Table(show_header=True,header_style="bold blue")
    #table.add_column("#",style="dim",width=6)
    #table.add_column("retailer",min_width=20)
    #table.add_column("size name", min_width=12,justify="right")

    #for idx, size_measurements in enumerate(sizing[1]):
        #table.add_row(str(idx),size_measurements[0])

#if __name__ == "__main__":
    #app()