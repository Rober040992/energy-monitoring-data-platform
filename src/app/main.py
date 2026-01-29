from fastapi import FastAPI

app = FastAPI(title="Energy Monitoring Data Platform")

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/other")
def read_other():
    return {"message": "other from /other"}
    