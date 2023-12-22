FROM python:3.11.5-slim

RUN groupadd -r nonadmins && useradd -r -g nonadmins notanadmin

WORKDIR /opt/backend

COPY ./src/requirements.txt /opt/backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /opt/backend/requirements.txt

COPY ./src /opt/backend

USER notanadmin

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]