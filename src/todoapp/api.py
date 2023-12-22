import importlib.metadata

from fastapi import APIRouter, HTTPException, status
from loguru import logger

from todoapp.config.core import settings
from todoapp.database import (
    create_task,
    fetch_all_tasks,
    fetch_one_task,
    remove_task,
    update_task,
)
from todoapp.schemas import Healthz, Task

api_router = APIRouter()


@api_router.get("/healthz", response_model=Healthz, status_code=status.HTTP_200_OK)
async def get_health() -> dict:
    health = Healthz(name=settings.APP_NAME, api_version=importlib.metadata.version("todoapp"))
    return health.model_dump()


@api_router.get("/task")
async def get_task() -> list:
    logger.info("Fetching tasks")
    response = await fetch_all_tasks()
    return response


@api_router.get("/task/{title}", response_model=Task)
async def get_task_by_title(title: str) -> Task:
    logger.info(f"Fetching task: {title}")
    response = await fetch_one_task(title)
    if not response:
        detail = f"There is no task with the title: {title}"
        logger.warning(detail)
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail)
    return response


@api_router.post("/task", response_model=Task)
async def post_task(task: Task) -> Task:
    response = await create_task(task.model_dump())  # type: ignore
    if not response:
        detail = f"Bad Request for task: {task}"
        logger.warning(detail)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail)
    return response


@api_router.put("/task/{title}", response_model=Task)
async def put_task(title: str, desc: str) -> Task:
    response = await update_task(title, desc)
    if not response:
        detail = f"There is no task with the title: {title}"
        logger.warning(detail)
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail)
    return response


@api_router.delete("/task/{title}")
async def delete_task(title: str) -> dict[str, object]:
    response = await remove_task(title)
    if not response:
        detail = f"There is no task with the title: {title}"
        logger.warning(detail)
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail)
    return {"message": "Successfully deleted task!", "success": True}
