from fastapi import Depends, FastAPI, HTTPException
import requests, urllib
import schemas
from  base64 import b64encode
from requests.structures import CaseInsensitiveDict
tags_metadata = [
    {
        "name": "IP-Updater",
        "description": "Update IP",
    },
]

app = FastAPI(
        docs_url = "/",
        title="IP-Updater-API",
        description="This is the API for IP updating",
        version="0.0.1",
        openapi_tags=tags_metadata,
        ssl_keyfile='certs/key.pem',
        ssl_certfile='certs/cert.pem'
)

{
  "hostname": "test.deanlord.net",
  "myip": "1.1.1.1",
  "username": "1BPyjKAyK1quFkoR",
  "password": "AKFhYOjTlFo9K6YA"
}
# import os
# from glob import glob
@app.get('/test/')
# def test(update_info: schemas.UpdateInfo):
def test(hostname, myip, username, password):
    # hostname = update_info.hostname
    # myip = update_info.myip
    # username = update_info.username
    # password = update_info.password
    # print(os.curdir)
    # print(glob('*'))
    # with open('certs/cert.pem', 'r') as f:
    #     print(f.read())
    params = {
       "hostname": hostname,
       "myip": myip,
       "username":   username,
       "password": password,
       'return': 'Oh, you made it!'
    }
    print(params)
    return params
    

@app.post('/update_google_ip/', tags=['IP-Updater'])
def update_google_ip(update_info: schemas.UpdateInfo):
    hostname = update_info.hostname
    myip = update_info.myip
    username = update_info.username
    password = update_info.password
    AUTH = f'Basic {str(b64encode(b"user:pass"))[2:-1]}'
    params = {
       "hostname": hostname,
       "myip": myip,
       "username":   username,
       "password": password
    }
    headers = {
        'User-Agent': 'DDNS Update Python Script',
        'Host':'domains.google.com',
        'Authorization': AUTH
    }
    # params = urllib.parse.urlencode(params)
    # print(params)
    # headers = CaseInsensitiveDict()
    # headers["Accept"] = "application/json"
    # update_url = f"https://domains.google.com/nic/update?hostname={hostname}&myip={myip}&username={username}&password={password}"
    # print(f"https://domains.google.com/nic/update?hostname={hostname}&myip={myip}&username={username}&password={password}")
    update_url = f"https://domains.google.com/nic/update"
    r = requests.post(url=update_url, params=params)
    if not r.ok:
        raise Exception(f'POST failed with code {r.status_code}')
    # print(r.content.decode())
    # print('all done')
    return r.text
