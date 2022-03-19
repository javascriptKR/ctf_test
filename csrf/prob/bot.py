import requests

url = "127.0.0.1:5000/profile?action=profile"

data = {'userip': '127.0.0.1', 'status': 'on'}

def check(content):
    print(content)

    res = requests.post(url, data=data)