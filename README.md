# Boilerplate Todo-App for FastAPI, MongoDB, Motor Projects

## Pre-Requisites
* Python 3.11+
* [Poetry](https://python-poetry.org/docs/#installation) installed
* Docker installed

## Getting started

Rename the `.env.sample` file to `.env` within the project folder or export the `MONGODB_URI` environment variable manually with `$ export MONGODB_URI=<YOUR_URI>`. The simplest way to start the production-ready application is via docker-compose.

```bash
docker-compose up
docker-compose down
```

The application can be started in development mode via Poetry.

```bash
poetry run start
```

## Running tests locally using Tox

If you want to run tests and checks locally in an isolated environment. Useful if you want to make sure that all tests pass before passing new code to a CI/CD pipeline.

```bash
- pip install tox
```

Run all tests and stylechecks.

```bash
- tox
```

Run tests and stylechecks seperately.

```bash
- tox -e test_app
- tox -e checks
```

## Credits

* [`Py-Pkgs`](https://py-pkgs.org)
* [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
