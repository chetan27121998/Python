class Food:
    def __init__(self,f_id,f_name,f_type,f_price):
        self.f_id = f_id
        self.f_name = f_name
        self.f_type = f_type
        self.f_price = f_price

    def __str__(self):
        return f'food[{self.f_id},{self.f_name},{self.f_type},{self.f_price}]'

    def __repr__(self):
        return f'food[{self.f_id},{self.f_name},{self.f_type},{self.f_price}]'
