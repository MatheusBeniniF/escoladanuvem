import requests

response = requests.get('https://randomuser.me/api/')
data = response.json()
user = data['results'][0]

nome = f"{user['name']['first']} {user['name']['last']}"
email = user['email']
pais = user['location']['country']

print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"País: {pais}")
