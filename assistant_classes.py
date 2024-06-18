import random


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class NewUser:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Generator:
    @staticmethod
    def password_generator():
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        length = 6
        password = ''
        for i in range(length):
            password += random.choice(chars)
        return password

    @staticmethod
    def login_generator():
        chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        length = 5
        email = ''
        for i in range(length):
            email += random.choice(chars)
        email += '_test@ya.ru'
        return email

    @staticmethod
    def name_generator():
        chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        length = 4
        name = ''
        for i in range(length):
            name += random.choice(chars)
        return name
