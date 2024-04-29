# system packages 
import csv
import os.path

# external packages 

import numpy as np
import pandas as pd

# import functions 

# create objects 

class Dimensions:
    def __init__(self, bust, waist, hip):
        self.bust = bust
        self.waist = waist
        self.hip = hip

class Body(Dimensions):
    def __init__(self, customerID, bust, waist, hip):
        super().__init__(bust, waist, hip)
        self.customerID = customerID

class Size(Dimensions):
    def __init__(self, sizeName, sizeChartID, sizeID, bust, waist, hip):
        super().__init__(bust, waist, hip)
        self.sizeName = sizeName
        self.sizeChartID = sizeChartID
        self.sizeID = sizeID

class Retailer:
    def __init__(self, sizeChartID, retailerID, retailerName):
        self.sizeChartID = sizeChartID
        self.retailerID = retailerID 
        self.retailerName = retailerName

class Customer:
    def __init__(self, customerID, customerUsername, customerPassword):
        self.customerID = customerID
        self.customerUsername = customerUsername 
        self.customerPassword = customerPassword

class SizeChart:
    def __init__(self, sizeChartID, sizeNames):
        self.sizeChartID = sizeChartID
        self.sizeNames = sizeNames

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

def updateRetailerDatabase():
    retailers.to_csv('retailers.csv',sep=',',index=False,encoding='utf-8')
    return retailers

retailers = createRetailerDatabase()

# store sizing information 

def createSizingDatabase():
    sizing_columns = ['sizeID','sizeChartID','sizeName','size_bust','size_waist','size_hip']
    sizing = pd.DataFrame(columns=sizing_columns)
    sizing['sizeID'] = sizing.index
    sizing.to_csv('sizing.csv',sep=',',index=False,encoding='utf-8')
    return sizing

def updateSizingDatabase():
    sizing.to_csv('sizing.csv',sep=',',index=False,encoding='utf-8')
    return sizing

sizing = createSizingDatabase()




# create new customer

def createCustomer():
    id_input = input("ID: ")
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

# evaluate 'fit' 

def evaluateFit(customer_measurements,size_measurements):
    fit = True  
    if customer_measurements.bust == size_measurements.bust and customer_measurements.waist == size_measurements.waist and customer_measurements.hip == size_measurements.hip:
        fit = True 
    else: fit = False
    return fit

fit_determination = evaluateFit(customer_measurements,size_measurements)

print(fit_determination)


