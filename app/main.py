from fastapi import FastAPI , APIRouter
import uvicorn

app = FastAPI()
router = APIRouter()

@app.get('/')
async def root():
    return "Welcome to DataPulse"
@app.get('/health')
async def health():
    return {'Health':'Health endpoint'}

app.get('/auth')
async def auth():
    return "Auth router"

app.get('/datasets')
async def auth():
    return "datasets router"

app.get('/jobs')
async def auth():
    return "jobs router"

app.get('/reports')
async def auth():
    return "reports router"

if __name__ == "__main__":
    uvicorn.run(app)