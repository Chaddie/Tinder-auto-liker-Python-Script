import requests
import json
facebook_token = 'token' #get this from the api explorer or something
facebook_id = 'id' #your numerical facebook id

loginCredentials = {'facebook_token':facebook_token, 'facebook_id' : facebook_id}
headers = {'Content-Type' : 'application/json', 'User-Agent' : 'Tinder Android Version 3.2.0'}

r = requests.post('https://api.gotinder.com/auth', data=json.dumps(loginCredentials), headers=headers)
x_auth_token = r.json()['token']

while True:
    headers2 = {'User-Agent' : 'Tinder Android Version 3.2.0', 'Content-Type' : 'application/json', 'X-Auth-Token' : x_auth_token}
    r2 = requests.get('https://api.gotinder.com/user/recs', headers=headers2)
    hoes = r2.json()['results']
for hoe in hoes:
        _id = hoe['_id']
        name = hoe['name']
        headers3 = {'X-Auth-Token' : x_auth_token, 'User-Agent' : 'Tinder Android Version 3.2.0'}
        r3 = requests.get('https://api.gotinder.com/like/' + _id, headers=headers3)
        print(_id)
        print(r3.status_code)
        print(name)


