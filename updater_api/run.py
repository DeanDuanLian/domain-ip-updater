import uvicorn

host='0.0.0.0'
port=8681

if __name__ == '__main__':
    # & uvicorn run:app --reloadをターミナルで打っても可
    uvicorn.run('main:app', 
                host=host, 
                port=port, 
                reload=True,
                ssl_keyfile='certs/key.pem',
                ssl_certfile='certs/cert.pem'
                )