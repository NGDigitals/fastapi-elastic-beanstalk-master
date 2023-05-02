from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'name': 'fastapi-songs'}

@app.get('/test')
def read_root():
    return {'name': 'fastapi-songs-test'}