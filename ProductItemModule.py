class ProductItem:
    dbId = 0
    artikul = "z0000qw"
    name = "Test"
    price = 100.00
    
    def __init__(self, dbId, art, nm, p):
        self.dbId = dbId
        self.artikul = art
        self.name = nm
        self.price = p
        
    def set_price(self, dbId, price):
        pass