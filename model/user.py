import json

from pymarshaler.marshal import Marshal


class UserPhone:
    def __init__(self, id: str, home: str, mobile: str):
        self.id = id
        self.home = home
        self.mobile = mobile

class UserCar:
    def __init__(self, id: str, model: str, price: str):
        self.id = id
        self.model = model
        self.price = price        

class User:
    def __init__(self, id: str, first_name: str, last_name: str, phone: UserPhone, car: UserCar):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.car = car

def bind_user(data, phone, car):
    return User(data[0][0], data[0][1], data[0][2], phone, car)

def bind_car(data):
    return UserCar(data[0][0], data[0][1], data[0][2])

def bind_phone(data):
    return UserPhone(data[0][0], data[0][1], data[0][2])


def build_response(obj):
    marshal = Marshal()
    dat_json = marshal.marshal(obj)
    return dat_json
