import uvicorn
from loguru import logger


def main():
    logger.warning("Running in development mode. Do not run like this in production.")
    uvicorn.run("src.todoapp.main:app", host="0.0.0.0", port=8001, log_level="debug")


if __name__ == "__main__":
    main()
