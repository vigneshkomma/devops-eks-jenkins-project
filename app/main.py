from fastapi import FastAPI, HTTPException
from app.schemas import URLCreate, URLResponse, CheckResult
from app import service

#intiate app
app = FastAPI(
    title = "URL Health checker API",
    description= "A simple DevOps-style API that monitors service uptime and response time.",
    version= "1.0.6"
)

@app.get("/")
def root():
    return {
        "message": "URL Health Checker API is running: version:1.0.1",
        "docs": "/docs"
    }


@app.post("/checks", response_model=URLResponse)
def add_check(data: URLCreate):
    return service.add_url(data)

@app.get("/checks", response_model=list[URLResponse])
def list_checks():
    return service.get_urls()

@app.get("/checks/run", response_model=list[CheckResult])
def run_checks():
    return service.run_all_checks()

@app.get("/checks/{url_id}", response_model=URLResponse)
def get_check(url_id: int):
    
    item = service.get_url(url_id)

    if item is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return item

@app.delete("/checks/{url_id}")
def remove_check(url_id: int):
    
    item = service.delete_url(url_id)

    if item is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return {
        "message": "URL removed successfully",
        "removed": item
    }


