from fastapi import FastAPI


app  = FastAPI()

@app.get('/')
def index():
    return {
        "data": {
            "name": "index"
        }
    }


@app.get('/about')
def about():
    return {
        "data": {
            "name": "about"
        } 
    }