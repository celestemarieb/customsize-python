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