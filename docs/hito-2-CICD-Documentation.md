# Hito 2 - PoDeMaster CI

## Overview
I decided to use FastAPI for our project to allow users to perform operations such as login, registration, and functionality like trading. It relies on JWT authentication, password hashing, and an in-memory database for user storage. This project uses an in-memory database for user storage, defined in `app/models/user.py`. The database (`fake_users_db`) stores user information temporarily while the application is running. I am using GitHub Actions for CI/CD in order to automate the testing and deployment processes.

---
## Content
1. [Choose Task Manager](#1-task-manager)
2. [Choose Testing System and Assertion Library](#2-assertion-library)
3. [Writing Tests](#3-writing-tests)
4. [Continous Integration](#4.-continous-integration)
5. [Verify CI Github](#5.-verify-ci-github )

## 1. Task Manager
I chose Make as the task manager for task automation in this project. Using Makefile allows me to define a consistent set of commands for common project tasks, simplifying setup, testing, and running the application both locally and in CI environments. I chose it, because Mark is lightweight, does not require additional dependencies, and most importantly is widely used in Python projects, which is important for me since I am using FastAPI (python-based).  

I created a Makefile that includes commands for:
- Install all Dependencies: make install uses pip to install the requirements from `requirements.txt`
    - **FastAPI**: For building the API.
    - **Uvicorn**: For serving the FastAPI application.
    - **Pydantic**: For data validation and serialization.
    - **pytest**: For running the test suite.
    - **pytest-asyncio**: For testing asynchronous code.
    - **python-multipart**: Required for form data parsing (used in user login).
    - **passlib**: For password hashing and verification.
    - **jose**: For creating and verifying JWT tokens. 
    - **httpx**: For async-compatible HTTP
- Running Tests: make test runs the test defined with pytest.
- Starting the Server: make run starts the application locally using Uvicorn.

### 2. Testing System and Assertion Library
I decided to use pytest as Testing System, since it uses a user-friendly syntax, making it easy to use and maintain. Furttermore it has a robust ecosystem of plugins (like pytest-asyncio for asynchronous testing) that align well with FastAPI’s asynchronous nature. In addition it is recommended by FastAPI to use pytest as a testing framework. 
I chose to use pytest with pytest-asyncio for async testing to provide support for asynchronous test functions. Asynchronous functions were used in order to handle HTTP requests and responses. I added it of course to the `requirements.txt`.

No further setup was necessary for the Assertion Library, since pytest uses assert statements from python standard library.

To use pytest, I installed it in our environment and set up assertions for checking the application’s expected behaviors. I defined both synchronous and asynchronous tests and utilized pytest's fixture system to manage test dependencies.

### 3. Writing Tests
Testing is crucial to validate that the application functions as expected and handles both expected and edge cases correctly. I focused on two main types of tests:
- Unit Tests: To validate individual functions, focusing on isolated components like data validation, password hashing, and token creation.
- Integration Tests: To ensure that API endpoints respond correctly to HTTP requests.

I used pytest fixtures to set up reusable dependencies, such as a test client for interacting with the API.
Test Cases: Each test case checks the output against expected values, covering core features like user login, registration, and creating Pokémon. 
Error Handling: I included tests for invalid data inputs, confirming that the application returns appropriate error messages.

### 4. Continuous Integration
I chose GitHub Actions for CI/CD integration to automate testing on each code push. It allows for a seamless integration with GitHub repositories and a easy set up of workflows. Since my code is already hosted on GitHub, this allows us to set up aotmated workflows triggered by events like push requests directly within the Github environment.

For this to work, we need to have the test files in the folder test and named something with `"test_*"`.
Furthermore it is necessary to create a GitHub Workflow File to define the CI Workflow. The file ci.yml will be having the path from root `.github/workflows/ci.yml` with 
```python
name: Continuous Integration
on:
  push:
    branches:
      - main  
  pull_request:
    branches:
      - main  # This triggers CI on pull requests as well

jobs:
  test:
    runs-on: ubuntu-latest  # This runs the workflow on a Linux environment

    steps:
    # Step 1: Check out the code from the repository
    - name: Checkout code
      uses: actions/checkout@v2

    # Step 2: Set up Python
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    # Step 3: Install dependencies
    - name: Install dependencies
      run: make install

    # Step 4: Run tests using pytest
    - name: Run tests
      run: make test
```

### 5. Verify CI Github 
In order to test if the CI configuration is working, I pushed the changes to GitHub and thus triggered the workflow. 
Under the tab 'Actions' we can monitor the status of our workflow. At the beginning I had some wrong version numbers or missing packages in the `requirements.txt` which is the reason why the first pushes did not work. After fixing everything I confirmed that everything ran sucessfully and the project was built without anything failing, since all the tests passed. 
<img src="../images/hito-2-CI.png" alt="hito-2-CI" style="width:100%;">
