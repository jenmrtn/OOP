class Customer:

    def __init__(self, id, name, add, email, phone, ms):
        self.customerid=id
        self.name=name
        self.address=add
        self.email=email
        self.phone=phone
        self.member_status=ms

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.customerid

    def get_phone(self):
        return self.phone

    def get_status(self):
        return self.member_status

class Transaction:
    
    def __init__(self, d, n, c, id):
        self.date=d
        self.item_name=n
        self.cost=c
        self.customerid=id

    def get_item(self):
        return self.item_name

    def get_cost(self):
        return self.cost


