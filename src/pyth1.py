import requests

x = {
    'name' : "moomik",
    'quantity' : 12
}


x =requests.post("http://127.0.0.1:3030/v1/groceries",json=x)
print(x.content.decode("utf-8"))