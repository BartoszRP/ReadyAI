import requests

# wysylam GET
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")


# sprawdzamy, czy poszło dobrze
print(response.status_code)



# parsujemy odpowiedź jako JSON
data = response.json()

print(data)


# payload = {
#     "title": "Bartek testuje",
#     "body": "To jest przykładowy post",
#     "userId": 1
# }

# print(response.status_code)

# data = response.json()
# print(data)