from fastapi import Depends, FastAPI, HTTPException
import requests
import schemas

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
        openapi_tags=tags_metadata
)

@app.post('/update_google_ip/', tags=['IP-Updater'])
def update_google_ip(update_info: schemas.UpdateInfo):
    username = update_info.username
    password = update_info.password

    # requests.post()
    return f'{username}, {password}'
