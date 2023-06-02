# Jolted API

Jolted API is a Python backend application built with FastAPI, Pydantic, Beanie, MongoDB and managed with Poetry.

## Project Structure

The project's structure is as follows:

```
jolted_api/
  ├── jolted_api/
  │   ├── database/
  │   │   ├── __init__.py
  │   │   ├── connection.py
  │   ├── models/
  │   │   ├── __init__.py
  │   │   ├── notebook.py
  │   │   ├── organization.py
  │   │   ├── user.py
  │   │   ├── wiki_module.py
  │   ├── routes/
  │   │   ├── __init__.py
  │   │   ├── notebook_router.py
  │   │   ├── organization_router.py
  │   │   ├── user_router.py
  │   │   ├── wiki_module_router.py
  │   ├── services/
  │   │   ├── __init__.py
  │   │   ├── notebook_service.py
  │   │   ├── organization_service.py
  │   │   ├── user_service.py
  │   │   ├── wiki_module_service.py
  │   ├── __init__.py
  │   ├── api.py
  ├── tests/
  │   ├── __init__.py
  ├── poetry.lock
  ├── pyproject.toml
  ├── README.md
  ├── tutorial_template.json
  ├── wiki_template.json
```

## Technology Stack

- **FastAPI**: a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Pydantic**: data validation and settings management using Python type annotations.
- **Beanie**: an asynchronous Python object-document mapper (ODM) for MongoDB, built on top of Motor and Pydantic.
- **MongoDB**: a source-available cross-platform document-oriented database program, classified as a NoSQL database program.
- **Poetry**: a tool for dependency management and packaging in Python.

## Setup and Installation

### Requirements

- Python 3.9 or newer
- MongoDB installed and running on your local machine
- Poetry (Python package manager)

### Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/username/jolted_api.git
    cd jolted_api
    ```

2. **Set up a Python virtual environment** 

    For this project, we use `Poetry` as our Python dependency manager, which will also handle our virtual environment.

    To install Poetry, refer to the official [installation guide](https://python-poetry.org/docs/#installation).

    With Poetry installed, run the following command to create a new virtual environment:

    ```bash
    poetry shell
    ```

    This command will create a new virtual environment and automatically activate it.

3. **Install Python dependencies**

    After activating the virtual environment, install the required Python dependencies with:

    ```bash
    poetry install
    ```

4. **Setup MongoDB**

    This project uses MongoDB as its database. Make sure you have MongoDB installed and running on your system. For instructions on installing MongoDB, refer to the official [MongoDB installation guide](https://docs.mongodb.com/manual/installation/).

    Once MongoDB is running, update the MongoDB connection details in `jolted_api/database/connection.py` if necessary.

5. **Run the API server**

    With all dependencies installed and the database running, you can now run the FastAPI server:

    ```bash
    uvicorn jolted_api.api:app --reload
    ```

    This command starts the FastAPI server with hot-reload enabled. Your API server is now accessible at `http://localhost:8000`.

Remember to replace any placeholders (`username`, `repository name`, etc.) with your actual information. Also, the commands mentioned are for a Unix-based system, like Linux or MacOS. If you're using a different operating system, please adjust the commands accordingly.

## Usage

TODO: Instructions for using the project

## Tests

TODO: Information about running tests

## Contributing

TODO: Information about how to contribute to the project

## License

TODO: Information about the project's license
