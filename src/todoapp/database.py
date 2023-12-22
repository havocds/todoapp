from typing import Any

import motor.motor_asyncio
from schemas import Task

from .config.core import settings

client: Any = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URI)

database = client.schemas.TaskList

collection = database.task


async def fetch_one_task(title: str) -> Task:
    document = await collection.find_one({"title": title})
    return document


async def fetch_all_tasks() -> list:
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks


async def create_task(task: Task) -> Task:
    document = task
    await collection.insert_one(document)
    return document


async def update_task(title: str, description: str) -> Task:
    await collection.update_one({"title": title}, {"$set": {"description": description}})
    document = await collection.find_one({"title": title})
    return document


async def remove_task(title: str) -> bool:
    await collection.delete_one({"title": title})
    return True
