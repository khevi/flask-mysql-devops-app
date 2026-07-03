# Flask MySQL DevOps Application Platform

A hands-on DevOps engineering project demonstrating the automated deployment of a containerized Flask and MySQL application using Jenkins, Docker, Kubernetes, Nginx, and Prometheus.

The project was built as a multi-stage home lab to practice application delivery, CI/CD automation, container orchestration, reverse proxy configuration, and infrastructure monitoring.

## Project Objectives

- Build a Python Flask application connected to MySQL
- Containerize application workloads using Docker
- Deploy multi-container services using Docker Compose
- Automate application deployment with Jenkins
- Configure Nginx as a reverse proxy
- Define application workloads using Kubernetes manifests
- Deploy MySQL workloads to Kubernetes
- Integrate Prometheus monitoring
- Practice production-style DevOps deployment workflows

## Technology Stack

| Area | Technologies |
|---|---|
| CI/CD | Jenkins |
| Containers | Docker, Docker Compose |
| Orchestration | Kubernetes |
| Reverse Proxy | Nginx |
| Monitoring | Prometheus, Node Exporter |
| Application | Python, Flask |
| Database | MySQL |
| Operating System | Ubuntu Linux |
| Version Control | Git, GitHub |

## Repository Structure

```text
flask-mysql-devops-app/
├── k8s/
│   └── Kubernetes application and MySQL manifests
│
├── monitoring/
│   └── prometheus/
│       └── Prometheus monitoring configuration
│
├── nginx/
│   └── Nginx reverse proxy configuration
│
├── Dockerfile
├── Jenkinsfile
├── app.py
├── docker-compose.yml
└── requirements.txt

                    GitHub Repository
                           |
                           v
                        Jenkins
                           |
                           v
                    Docker Build
                           |
                           v
                  Container Deployment
                           |
              +------------+------------+
              |                         |
              v                         v
            Nginx                    Flask App
       Reverse Proxy                      |
                                          v
                                        MySQL

Monitoring
    |
    v
Prometheus
    |
    v
Node Exporter Metrics

docker compose up -d
Nginx Reverse Proxy

Nginx is used as a reverse proxy for the application workload.

Nginx configuration is maintained under:
nginx/
The reverse proxy layer demonstrates:

Application traffic routing
Separation of frontend traffic from application services
Container-based Nginx deployment
Automated Nginx deployment through Jenkins
Kubernetes Workloads

Kubernetes manifests are maintained under:

k8s/
The Kubernetes configuration includes application and MySQL workload definitions.

This phase demonstrates:

Declarative application deployment
Kubernetes workload configuration
MySQL deployment patterns
Version-controlled Kubernetes manifests
Monitoring with Prometheus

Prometheus configuration is maintained under:

monitoring/prometheus/

The monitoring environment was configured to collect infrastructure metrics using Node Exporter.

The home-lab monitoring stack included:

Prometheus
Node Exporter
Grafana

Prometheus was used for metrics collection, while Grafana provided dashboard visualization for infrastructure monitoring.

DevOps Practices Demonstrated

This project demonstrates hands-on experience with:

CI/CD pipeline automation
Jenkins Pipeline-as-Code
Docker containerization
Docker Compose
Kubernetes workload management
Nginx reverse proxy configuration
Flask application deployment
MySQL integration
Prometheus monitoring
Linux infrastructure
Git-based application delivery
Project Status
Completed
Flask application deployment
Flask-to-MySQL database connectivity
Docker application containerization
Docker Compose application stack
Jenkins deployment automation
Nginx reverse proxy configuration
Kubernetes application manifests
Kubernetes MySQL configuration
Prometheus monitoring configuration
Node Exporter metrics collection
Future Improvements
Add automated application testing to the Jenkins pipeline
Add Docker image security scanning
Add Kubernetes health probes
Add Kubernetes resource limits
Add centralized logging
Expand Grafana dashboards
Add alerting rules
Integrate a container registry
Implement GitOps deployment workflows
Author

Kossi Hevi-Doglan
Senior DevOps Engineer | Platform Engineer | Cloud Infrastructure Engineer

GitHub: @khevi

