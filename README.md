# 🐳 Kubernetes Headless Microservices Demo

> A real-world example project demonstrating:
- Stateless frontend and backend microservices
- Stateful PostgreSQL database (headless StatefulSet)
- Ingress with nginx on a local Kind cluster
- Dockerized deployments end-to-end

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Kubernetes](https://img.shields.io/badge/kubernetes-v1.33+-blue)
![Docker](https://img.shields.io/badge/docker-build-green)

---

## 📦 Project Structure

k8-headless/
├── backend/ # Simple Python Flask backend
│ ├── app.py
│ └── Dockerfile
├── frontend/ # Simple HTML+JS frontend served by Nginx
│ ├── index.html
│ └── Dockerfile
├── services/ # Kubernetes YAMLs
│ ├── backend-deployment.yaml
│ ├── frontend-deployment.yaml
│ ├── postgres-statefulset.yaml
│ ├── ingress.yaml
│ └── ...
└── README.md



---

## 🚀 Features

✅ Stateless Frontend: served by Nginx  
✅ Stateless Backend: Python Flask API  
✅ Stateful PostgreSQL database with headless service  
✅ Ingress routing with `demo.local` domain  
✅ Fully Dockerized & works on Kind (local k8s)

---

## 🛠 Requirements

- Docker
- [Kind](https://kind.sigs.k8s.io/) (Kubernetes IN Docker)
- kubectl
- (Optional) Node.js / Python for local dev

---

## 🐳 Run locally with Docker

```bash
# Build images
cd frontend && docker build -t my-frontend:latest .
cd ../backend && docker build -t my-backend:latest .

# Run containers
docker run -d -p 8080:80 my-frontend:latest
docker run -d -p 5000:5000 my-backend:latest
docker run -d -p 5432:5432 --name pg-test -e POSTGRES_PASSWORD=postgres postgres:14


Then open:

Frontend → http://localhost:8080

Backend → http://localhost:5000


Run on Kubernetes (Kind)
1. Create Kind cluster:
 kind create cluster --name my-cluster

2. Load Docker images into Kind:

3. Deploy services:

 kubectl apply -f services/

4. Install ingress-nginx:

  kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.1/deploy/static/provider/kind/deploy.yaml

5. Wait for ingress controller to be Running:

 kubectl get pods -n ingress-nginx

6. Add to /etc/hosts:

 127.0.0.1 demo.local

7. Expose ingress (for local):

 kubectl port-forward -n ingress-nginx service/ingress-nginx-controller 8081:80


Then open: http://demo.local:8081
kind load docker-image my-frontend:latest
kind load docker-image my-backend:latest
