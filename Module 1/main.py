from fastapi import FastAPI
import json
app=FastAPI()

# expenses.json is our database

def load_data():
    with open("expenses.json", "r") as f:
        data=json.load(f)
    return data

@app.get("/hello")
def view():
    return "Hello World"

@app.get("/about")
def view():
    return "This is the about section of our API"

@app.get("/view")
def view_expenses():
    data=load_data()
    return data