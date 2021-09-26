import os
import random
import pickle as pk
import json

def load_products():
    absolute_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'config'))
    file_path = absolute_path + '/products.py'
    return file_path


def read_products():
    with open(load_products(), 'r') as products:
        product = json.load(products)
    return random.choice(product)



