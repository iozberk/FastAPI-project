import requests
from requests.auth import HTTPBasicAuth

login_url = 'https://fastapi-test1-iozberk.herokuapp.com/login'
usernames = ["fastapi@fastapi.com", "fastapi1@fastapi.com","fastapi12@fastapi.com", "fastapi123@fastapi.com", "fastapi1234@fastapi.com", "fastapi12345@fastapi.com", "fastapi123456@fastapi.com", "fastapi1234567@fastapi.com", "fastapi12345678@fastapi.com", "fastapi123456789@fastapi.com"]
payload = {'username':'fastapi@fastapi.com','password':'Password1!'}

# User Login

response = requests.post(login_url,data=payload)
access_token = response.json()["access_token"]
print(access_token)


# Vote posts

vote_data = {"post_id": 21,"dir": 1}

import requests
vote_url = "https://fastapi-test1-iozberk.herokuapp.com/vote"
vote_data = {"post_id": 21,"dir": 1}

headers = {'Authorization': 'Bearer ' + access_token}
auth_response = requests.post(vote_url, json=vote_data, headers=headers)

print(auth_response.json())




# ------------------------------------------------------------


login_url = 'https://fastapi-test1-iozberk.herokuapp.com/login'
vote_url = "https://fastapi-test1-iozberk.herokuapp.com/vote"
usernames = ["fastapi@fastapi.com", "fastapi1@fastapi.com","fastapi12@fastapi.com", "fastapi123@fastapi.com", "fastapi1234@fastapi.com", "fastapi12345@fastapi.com", "fastapi123456@fastapi.com", "fastapi1234567@fastapi.com", "fastapi12345678@fastapi.com", "fastapi123456789@fastapi.com"]

for i in range(0,10):
    payload = {'username':usernames[i],'password':'Password1!'}
    response = requests.post(login_url,data=payload)
    access_token = response.json()["access_token"]
    print(access_token)
    for k in range(0,50):
        vote_data = {"post_id": k+1,"dir": 1}
        headers = {'Authorization': 'Bearer ' + access_token}
        auth_response = requests.post(vote_url, json=vote_data, headers=headers)
        print(auth_response.json())

