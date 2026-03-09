from fastapi import APIRouter

router = APIRouter()

@router.post('/')
async def list_jobs():
    return {'message': []}

@router.get('/{job_id}')
async def get_job_id(job_id: int):
    return {'Job id': job_id}