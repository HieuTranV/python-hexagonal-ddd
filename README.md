# Python Hexagonal DDD

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)


## Introduction

This project demonstrates the principles of Hexagonal Architecture (Ports and Adapters) and Domain-Driven Design (DDD) using Python. It showcases how to design clean, maintainable, and scalable applications by focusing on domain logic, decoupling dependencies, and enhancing testability.

## Installation

To install the core services, clone the repository and install the dependencies:

```bash
git clone https://github.com/HieuTranV/python-hexagonal-ddd.git
pip install -r requirements.txt
```


## Usage
Before starting or testing, ensure that the necessary environment variables are loaded. You can do this by sourcing the `.env.demo` file:

```bash
source .env.demo
```

To test the services:

1. Ensure that all dependencies are installed as per the [Installation](#installation) section.
2. Set the `PYTHONPATH` environment variable to include the current directory:
  ```bash
  export PYTHONPATH="$PYTHONPATH:$pwd"
  ```
3. Run the tests using `pytest`:
  ```bash
  pytest
  ```

To start the services, use the following command:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8080
```

This command will start the application using Uvicorn, an ASGI server for Python web applications. The `--host 0.0.0.0` option makes the server accessible externally, and `--port 8080` specifies the port on which the server will listen.

The services will be available at `http://localhost:8080`.
