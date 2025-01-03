# Hito 4 - PoDeMaster Container

## Overview
In this milestone we containerized the PoDeMaster API and Database in order to test its functionality, and ensure it operates as expected.


## Application Structure
The cluster is structured with the following main services:
- **API Service (api):** Built on FastAPI, it handles all application logic and API routes.
- **Database Service (db):** A PostgreSQL database for persistent data storage.
- **nginx:** An Nginx reverse proxy container to handle incoming requests and forward them to the FastAPI application.



## Run Application with Docker
- Ensure Docker and Docker Compose are installed.
- Clone the repository: `git clone https://github.com/omiidos/CC24-PoDeMaster.git`
- Go the Root Directory
- Build and start the container cluster:`docker-compose up --build`

We used the Base Image `python:3.10-slim` because:
- Lightweight image reduces container size and deployment time.
- Official Python image ensures security and regular updates.
- Python 3.9 is modern and compatible with required dependencies.


## Container Design
#### API Service 
Hosts the application and exposes the FastAPI endpoints.
- Configuration:
    - Ports: Exposes port 8000 for external access.
    - Volumes: Maps source code for development flexibility.
    - Dependencies: Relies on db and redis services.
- Base Image: python:3.10-slim

#### Database Service
Provides persistent data storage for the application.
- Configuration:
    - Image: postgres:14-alpine
    - Ports: Exposes port 5432 for local or inter-container communication.
    - Volumes: Ensures database persistence across container restarts.
- PostgreSQL is reliable, scalable, and efficient for relational data.

### CI/CD and Automatic Updates
This project uses GitHub Actions to build and publish Docker images to GitHub Container Registry. We automate builds, ensuring the latest image is available upon each push.


## File Overview
### Dockerfile
The dockerfile is a script that contains a series of instructions on how to build a Docker image for our own application. 
We define the environment in which PoDeMaster will run, including which base image to use. Furthermore we first need to copy all the requirements and install all the dependencies we need. Then we need to copy the code into the container, and expose the API port (8000) and run the application. 

### Docker-Compose.yaml
We use the `docker-compose.yaml` to define and manage our multi-container Docker application. 
It allows us to configure the aspects of PoDeMaster's environment, including which containers to run, and how they should interact.
We then can use `docker-compose up --build` to build and update the docker image. 
We used `docker login ghcr.io -u omiidos` to login into GitHub Packages.
We then used `docker tag pokemon-api ghcr.io/omiidos/cc24-podemaster:latest` to tag our docker image.
With `docker push ghcr.io/omiidos/cc24-podemaster:latest` we pushed our docker image to GitHub Packages.

### docker-publish.yml
We created a Workflow File to automate the process of building and publishing our Docker image to the GitHub Container Registry (GHCR) whenever changes are pushed to the main branch of our repository.
Furthermore we define in this file the steps within the job. After getting the code from the repository we set up Docker Buildx and login to GitHub Container Registry.
Important to note is, that we used a Personalized Access Token (PAT) which we saved as a secret in the repository. This allows the workflow to authenticate to GHCR and push the build images.


