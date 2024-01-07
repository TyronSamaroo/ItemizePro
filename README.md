# My FastAPI Project

This project is a web API developed using [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Requirements

To run this project, you need the following installed:

- Python 3.11
- FastAPI: A web framework for building APIs.
- Uvicorn: An ASGI server for hosting the application.
- SQLAlchemy: An SQL toolkit and ORM for Python.
- Pydantic: Data validation and settings management using Python type annotations.
- pytest: A framework for running tests on the application.

## Installation

Follow these steps to set up the project:

1. Clone this repository.
2. Activate the virtual environment:

    ```sh
    pipenv shell
    ```
3. Inside the project directory, install the dependencies using Pipenv:
    ```
    sh pipenv install
    ```


## Running the Application

To start the application with hot-reload (which allows the server to automatically restart upon code changes), use the following command:

```sh
uvicorn main:app --reload
```
