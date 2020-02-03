#!/usr/bin/python3
""" a Python script that, using a REST API, for a given
# employee ID, returns information about his/her TODO list progress. """
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    fin = [f.get("title") for f in todo if f.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(fin), len(todo)))
    [print("\t {}".format(i)) for i in fin]