from fastapi import FastAPI
from app.api import auth_routes, dataset_routes, job_routes, report_routes

app = FastAPI(
    title = 'DataPulse',
    description = 'Asyncronous Data processing platform',
    version = '1.0.0',
)


@app.get('/health')
async def health():
    return {'Health':'Health endpoint'}

# register routes
app.include_router(router=auth_routes.router, prefix="/auth",tags=["Auth"])
app.include_router(router=dataset_routes.router, prefix="/datasets", tags=["Datasets"])
app.include_router(job_routes.router, prefix="/jobs", tags=["Jobs"])
app.include_router(report_routes.router, prefix="/reports", tags=["Reports"])
