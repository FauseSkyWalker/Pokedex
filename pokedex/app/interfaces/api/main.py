from fastapi import FastAPI


app = FastAPI(title="Pokemon CRUD API")

@app.get("/health")
def health_check():
    return {"status": "ok"}