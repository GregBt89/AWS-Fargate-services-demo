# **Deploying an application on AWS Elastic Container Service.**

A guide on how to deploy an container-based application on [AWS Elastic Container Serivce](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html). The goal is to demonstrate that the APIs of a demo application can receive http(s) requests and communicate with each other. The APIs sit behind an nginx web server acting as a reverse proxy. The nginx reverse proxy corresponds to the applications frontend while the APIs to the applications backend.

## **Prequisites:**

- [Docker](https://www.docker.com/) is used to create the API and Reverse Proxy images 
- [AWS](https://aws.amazon.com/) account for deploying the application in ECS.

## **Repository Structure.**

The code is organised in two folders: [*Infrastructure*](Infrastructure\infra.md) and [*Application*](Application\application.md). The former includes an yaml file with a template configuration of the AWS infrastructure that is needed for our application to run. The latter contains the code for an elementary API written in python using the [FastAPI](https://fastapi.tiangolo.com/) library.