from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(title="My API")

# API endpoint for grading
@app.get("/ping")
def ping_pong():
    return "pong"
