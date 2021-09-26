import os
import json
def load_users():
    absolute_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'config'))
    file_path = absolute_path + '/users.json'
    return file_path


def read_users():
    with open(load_users()) as users:
        userdata = json.load(users)
    return userdata


read_users()['username']
