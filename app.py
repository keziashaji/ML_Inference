from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message":"Model Running"}

@app.post("/predict")
def predict(mark:int):

    result = model.predict([[mark]])[0]

    if result == 1:
        return {"prediction":"Pass"}

    return {"prediction":"Fail"}