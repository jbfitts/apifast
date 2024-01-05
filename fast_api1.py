from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def hello_world():
    return "Hi Leah, this is my web app. Headed to get your script, then to Lidl"