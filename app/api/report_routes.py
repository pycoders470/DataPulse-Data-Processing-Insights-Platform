from fastapi import APIRouter

router = APIRouter()


@router.get("/{dataset_id}/summary")
async def dataset_summary(dataset_id: str):
    return {"dataset_id": dataset_id, "summary": {}}