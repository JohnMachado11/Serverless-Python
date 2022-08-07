from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import datetime
import requests

app = FastAPI()


@app.get('/')
def home():
    return {"Hello": "LinkedIn!"}

@app.get('/time')
def current_time():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return {"Current Time UTC": now}

@app.get('/dog-image')
def image():
    
    response={
        200: {
            "content": {"image/png": {}},
            "description": "Return image."
        }
    }
    return FileResponse("images/dog.png", media_type="image/png")

@app.get('/zen')
def zen_quotes():

    response = requests.get(url="https://zenquotes.io/api/random") 
    response.raise_for_status()
    data = response.json()

    html_content = f"""
    <html>
        <head>
            <title>Zen Quotes!</title>
        </head>
        <body>
            <h1> {data[0]['q']} </h1>
            <h2> - {data[0]['a']} </h2>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get('/user/{custom}')
def post_test(custom):
    
    html_content = f"""
    <html>
        <head>
            <title>Custom Page!</title>
        </head>
        <body>
            <h1> {custom} </h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
