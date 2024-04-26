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
    def __init__(self, sizeName, sizeChartID, bust, waist, hip):
        super().__init__(bust, waist, hip)
        self.sizeName = sizeName
        self.sizeChartID = sizeChartID

class Retailer:
    def __init__(self, sizeChartID, retailerID, retailerName):
        self.sizeChartID = 0
        self.retailerID = 0 
        self.retailerName = name

class Customer:
    def __init__(self, customerID, customerUsername, customerPassword):
        self.customerID = customerID
        self.customerUsername = customerUserName 
        self.customerPassword = customerPassword

class SizeChart:
    def __init__(self, sizeChartID, sizeNames):
        self.sizeChartID = 0
        self.sizeNames = []


# create an instance of a body 

defaultBody = Body ('defaultCustomerID', 'dbust', 'dwaist', 'dhip')

print(defaultBody)

# create an instance of a size 

defaultSize = Size('dsizename','dsizechartID','dbust','dwaist','dhip')

# evaluate 'fit' 

fit = True 

if defaultBody.bust == defaultSize.bust and defaultBody.waist == defaultSize.waist and defaultBody.hip == defaultSize.hip:
    fit = True 
else: fit = False

# print result 

print(fit)


