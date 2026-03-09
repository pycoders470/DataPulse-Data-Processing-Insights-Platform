from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def list_datasets():
    return {"datasets": []}


@router.post("/upload")
async def upload_dataset():
    return {"message": "upload endpoint placeholder"}