# DevOps CI/CD Pipeline with Jenkins, Docker, Kubernetes & Helm

A DevOps project demonstrating a modern CI/CD pipeline using **Jenkins**, **Docker**, **Docker Hub**, **Kubernetes (k3s)**, and **Helm** hosted on **AWS EC2**.

This project automatically builds a Docker image on every GitHub push, pushes the image to Docker Hub, and deploys the latest application to a Kubernetes cluster using Helm.

---

# Architecture

```text
                   GitHub
                      │
          GitHub Webhook Trigger
                      │
                      ▼
              Jenkins Controller
                      │
        Schedules Pipeline on Worker
                      │
                      ▼
              Jenkins Worker Node
       ┌─────────────────────────────┐
       │ Checkout Source Code        │
       │ Build Docker Image          │
       │ Test Container              │
       │ Push to Docker Hub          │
       └─────────────────────────────┘
                      │
                      ▼
                 Docker Hub
                      │
                      ▼
              Deploy Pipeline
                      │
                      ▼
         Kubernetes Cluster (k3s)
                      │
                 Helm Upgrade
                      │
                      ▼
             FastAPI Application
```

---

# Tech Stack

- Git
- GitHub
- Jenkins
- Jenkins Worker Node
- Docker
- Docker Hub
- Kubernetes (k3s)
- Helm
- AWS EC2
- FastAPI
- Python

---

# Project Structure

```
devops-eks-jenkins-project/
│
├── app/
│   ├── main.py
│   └── ...
│
├── kubernetes/
│   └── helm/
│       └── devops-app/
│           ├── Chart.yaml
│           ├── values.yaml
│           └── templates/
│               ├── deployment.yaml
│               └── service.yaml
│
├── Dockerfile
├── requirements.txt
├── Jenkinsfile.build
├── Jenkinsfile.deploy
├── logs
└── README.md
```


# Infrastructure

## AWS EC2 Instances
![alt text](<Screenshot From 2026-06-20 12-35-50-1.png>)
### Jenkins Controller

Responsibilities:

- Jenkins UI
- Pipeline orchestration
- GitHub Webhook receiver

Installed Software

- Jenkins
- Java
- Git

---

### Jenkins Worker

Responsibilities

- Build Docker images
- Run tests
- Push images
- Deploy to Kubernetes

Installed Software

- Git
- Docker
- kubectl
- Helm

---

### Kubernetes Server

Responsibilities

- Host Kubernetes Cluster
- Run application pods
- Manage deployments

Installed Software

- Docker
- k3s
- kubectl
- Helm

---

# CI Pipeline

The build pipeline is triggered automatically whenever code is pushed to GitHub.
![alt text](<Screenshot From 2026-06-20 13-46-01.png>)
Pipeline stages:

```
Checkout Code
      │
      ▼
Build Docker Image
      │
      ▼
Run Test Container
      │
      ▼
Push Image to Docker Hub
```

---

# CD Pipeline

Triggered automatically after a successful build.
![alt text](<Screenshot From 2026-06-20 13-46-24.png>)
Pipeline stages:

```
Check Kubernetes Cluster
        │
        ▼
Clean Failed Pods
        │
        ▼
Deploy using Helm
        │
        ▼
Verify Rollout
        │
        ▼
Application Available
```

---

# Kubernetes Deployment

Application is deployed using Helm.
![alt text](<Screenshot From 2026-06-20 13-46-53.png>)
Features:

- Rolling Updates
- Replica management
- Resource Requests
- Resource Limits
- NodePort Service
- Image Pull Policy
- Helm Release Management

---

# Docker

Docker image is built automatically by Jenkins.
![alt text](<Screenshot From 2026-06-20 13-07-45.png>)
Image format:

```
vigneshop/devops-app:<build-number>
```

Example

```
vigneshop/devops-app:24
```

Latest tag is also maintained.

---

# Helm

Deployment is managed through Helm.

Benefits:

- Easy upgrades
- Rollbacks
- Configurable deployments
- Reusable templates

---

# Deployment Workflow

```
Developer
    │
git push
    │
    ▼
GitHub
    │
Webhook
    ▼
Jenkins Build
    │
Build Docker Image
    │
Push Docker Hub
    ▼
Jenkins Deploy
    │
Helm Upgrade
    ▼
Kubernetes
    │
Pods Updated
```

---

# Running the Project

## Clone

```bash
git clone https://github.com/vigneshkomma/devops-eks-jenkins-project.git

cd devops-eks-jenkins-project
```

---

## Build Docker Image

```bash
docker build -t devops-app .
```

---

## Run Docker Container

```bash
docker run -d -p 8000:8000 devops-app
```

---

## Deploy using Helm

```bash
helm upgrade --install devops-app kubernetes/helm/devops-app
```

---

# Jenkins Pipelines

## Jenkinsfile.build

Responsibilities

- Checkout code
- Build Docker image
- Test container
- Push image to Docker Hub

---

## Jenkinsfile.deploy

Responsibilities

- Connect to Kubernetes
- Deploy using Helm
- Verify rollout
- Print deployment status





# Pipeline console outputs

Console outputs for the two(Build and Deploy) pipelines are available in `logs/` directory


# Accessing API at EC2 IP

![alt text](<Screenshot From 2026-06-20 14-52-08.png>)