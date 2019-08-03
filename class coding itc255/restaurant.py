class Restaurant():
    def __init__(self, restaurantid, locationid, customerid, status ):
        self.restaurantid=restaurantid
        self.locationid=locationid
        self.customerid=customerid
        self.status='Open'

    def getRestaurantId(self):
        return self.restaurantid

    def getLocationId(self):
        return self.locationid
    
    def getCustomerId(self):
        return self.customerid

    def getStatus(self):
        return self.status



    def setStatus(self, status):
        self.status=status

    def __str__(self):
        return self.restaurantid + ' ' + self.status 