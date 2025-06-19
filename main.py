from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def hellow():
    return {'data':{'name':'srinivas'}}

@app.get('/about')
def about():
    return {'data':{'about oage'}}