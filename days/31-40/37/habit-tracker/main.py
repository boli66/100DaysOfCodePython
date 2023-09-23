import requests
apiKEY = "123pixela1234"
params = {
    "token": apiKEY,
    "username": "bolibompa1234",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post("https://pixe.la/v1/users", json=params)

print(response.text)